import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import json
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Restaurant Billing System",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for minimalistic design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #2d3748;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Ensure all text is visible */
    .stMarkdown, .stText, .stWrite {
        color: #2d3748 !important;
    }
    
    /* Main content area with white background */
    .main .block-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 12px;
        margin: 1rem;
        padding: 1rem;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    .stSelectbox > div > div {
        border-radius: 8px;
        border: 1px solid #e1e5e9;
        background: white;
    }
    
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #e1e5e9;
        background: white;
        color: #2d3748;
    }
    
    .stNumberInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #e1e5e9;
        background: white;
        color: #2d3748;
    }
    
    /* Dataframe styling */
    .stDataFrame {
        background: white;
        border-radius: 8px;
        padding: 1rem;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
        border: 1px solid #e1e5e9;
    }
    
    .bill-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        margin: 1rem 0;
        border: 1px solid #e1e5e9;
    }
    
    .header-text {
        color: #2d3748;
        font-weight: 600;
        margin-bottom: 1rem;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    
    .subheader-text {
        color: #4a5568;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    /* Chart containers */
    .stChart {
        background: white;
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #e1e5e9;
    }
    
    /* Info and success messages */
    .stAlert {
        background: white;
        border-radius: 8px;
        border: 1px solid #e1e5e9;
    }
    
    /* Ensure all text elements have proper contrast */
    p, h1, h2, h3, h4, h5, h6, span, div {
        color: #2d3748 !important;
    }
    
    /* Streamlit default elements */
    .stMarkdown > div {
        color: #2d3748 !important;
    }
</style>
""", unsafe_allow_html=True)

# Database setup
def init_database():
    conn = sqlite3.connect('restaurant.db')
    cursor = conn.cursor()
    
    # Create menu table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            gst REAL DEFAULT 5.0
        )
    ''')
    
    # Create orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_type TEXT NOT NULL,
            total_amount REAL NOT NULL,
            gst_amount REAL NOT NULL,
            discount_amount REAL DEFAULT 0,
            payment_method TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create order_items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            total_price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (id)
        )
    ''')
    
    # Insert sample menu items if table is empty
    cursor.execute("SELECT COUNT(*) FROM menu")
    if cursor.fetchone()[0] == 0:
        sample_menu = [
            ('Margherita Pizza', 'Pizza', 299.0, 5.0),
            ('Pepperoni Pizza', 'Pizza', 349.0, 5.0),
            ('Chicken Burger', 'Burger', 199.0, 5.0),
            ('Veg Burger', 'Burger', 149.0, 5.0),
            ('Pasta Carbonara', 'Pasta', 249.0, 5.0),
            ('Caesar Salad', 'Salad', 179.0, 5.0),
            ('Chicken Wings', 'Appetizer', 299.0, 5.0),
            ('French Fries', 'Appetizer', 99.0, 5.0),
            ('Coca Cola', 'Beverage', 49.0, 5.0),
            ('Coffee', 'Beverage', 79.0, 5.0)
        ]
        cursor.executemany(
            "INSERT INTO menu (name, category, price, gst) VALUES (?, ?, ?, ?)",
            sample_menu
        )
    
    conn.commit()
    conn.close()

# Initialize database
init_database()

# Session state initialization
if 'current_order' not in st.session_state:
    st.session_state.current_order = []
if 'order_type' not in st.session_state:
    st.session_state.order_type = 'Dine-In'

def get_menu_items():
    conn = sqlite3.connect('restaurant.db')
    df = pd.read_sql_query("SELECT * FROM menu ORDER BY category, name", conn)
    conn.close()
    return df

def add_to_order(item_name, price, quantity):
    # Check if item already exists in order
    for item in st.session_state.current_order:
        if item['name'] == item_name:
            item['quantity'] += quantity
            return
    
    # Add new item
    st.session_state.current_order.append({
        'name': item_name,
        'price': price,
        'quantity': quantity
    })

def remove_from_order(index):
    if 0 <= index < len(st.session_state.current_order):
        st.session_state.current_order.pop(index)

def calculate_bill():
    subtotal = sum(item['price'] * item['quantity'] for item in st.session_state.current_order)
    gst_rate = 5.0  # 5% GST
    gst_amount = subtotal * (gst_rate / 100)
    total = subtotal + gst_amount
    return subtotal, gst_amount, total

def save_order(payment_method, discount=0):
    if not st.session_state.current_order:
        return False
    
    subtotal, gst_amount, total = calculate_bill()
    final_total = total - discount
    
    conn = sqlite3.connect('restaurant.db')
    cursor = conn.cursor()
    
    # Save order
    cursor.execute('''
        INSERT INTO orders (order_type, total_amount, gst_amount, discount_amount, payment_method)
        VALUES (?, ?, ?, ?, ?)
    ''', (st.session_state.order_type, final_total, gst_amount, discount, payment_method))
    
    order_id = cursor.lastrowid
    
    # Save order items
    for item in st.session_state.current_order:
        cursor.execute('''
            INSERT INTO order_items (order_id, item_name, quantity, price, total_price)
            VALUES (?, ?, ?, ?, ?)
        ''', (order_id, item['name'], item['quantity'], item['price'], item['price'] * item['quantity']))
    
    conn.commit()
    conn.close()
    
    # Clear current order
    st.session_state.current_order = []
    return order_id

def get_sales_report():
    conn = sqlite3.connect('restaurant.db')
    
    # Daily sales
    daily_sales = pd.read_sql_query('''
        SELECT DATE(timestamp) as date, 
               COUNT(*) as orders,
               SUM(total_amount) as revenue
        FROM orders 
        GROUP BY DATE(timestamp)
        ORDER BY date DESC
        LIMIT 7
    ''', conn)
    
    # Most sold items
    popular_items = pd.read_sql_query('''
        SELECT item_name, SUM(quantity) as total_quantity, SUM(total_price) as total_revenue
        FROM order_items
        GROUP BY item_name
        ORDER BY total_quantity DESC
        LIMIT 10
    ''', conn)
    
    conn.close()
    return daily_sales, popular_items

# Main app
def main():
    st.title("🍽️ Restaurant Billing System")
    st.markdown("---")
    
    # Sidebar for navigation
    page = st.sidebar.selectbox(
        "Navigation",
        ["📋 New Order", "📊 Reports", "🍽️ Menu Management"]
    )
    
    if page == "📋 New Order":
        new_order_page()
    elif page == "📊 Reports":
        reports_page()
    elif page == "🍽️ Menu Management":
        menu_management_page()

def new_order_page():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="header-text">Create New Order</h2>', unsafe_allow_html=True)
        
        # Order type selection
        st.session_state.order_type = st.selectbox(
            "Order Type",
            ["Dine-In", "Takeaway"],
            key="order_type_select"
        )
        
        # Menu display
        menu_df = get_menu_items()
        
        st.markdown('<h3 class="subheader-text">Menu</h3>', unsafe_allow_html=True)
        
        # Group by category
        for category in menu_df['category'].unique():
            category_items = menu_df[menu_df['category'] == category]
            
            st.markdown(f"**{category}**")
            for _, item in category_items.iterrows():
                col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                
                with col1:
                    st.write(f"• {item['name']}")
                with col2:
                    st.write(f"₹{item['price']:.0f}")
                with col3:
                    quantity = st.number_input(
                        "Qty",
                        min_value=0,
                        max_value=10,
                        value=0,
                        key=f"qty_{item['id']}"
                    )
                with col4:
                    if st.button("Add", key=f"add_{item['id']}"):
                        if quantity > 0:
                            add_to_order(item['name'], item['price'], quantity)
                            st.success(f"Added {quantity}x {item['name']}")
                            st.rerun()
            
            st.markdown("---")
    
    with col2:
        st.markdown('<h3 class="subheader-text">Current Order</h3>', unsafe_allow_html=True)
        
        if not st.session_state.current_order:
            st.info("No items in order")
        else:
            subtotal, gst_amount, total = calculate_bill()
            
            # Display order items
            for i, item in enumerate(st.session_state.current_order):
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"{item['name']}")
                with col2:
                    st.write(f"x{item['quantity']}")
                with col3:
                    if st.button("❌", key=f"remove_{i}"):
                        remove_from_order(i)
                        st.rerun()
            
            st.markdown("---")
            
            # Bill summary
            st.markdown('<div class="bill-card">', unsafe_allow_html=True)
            st.markdown("**Bill Summary**")
            st.write(f"Subtotal: ₹{subtotal:.2f}")
            st.write(f"GST (5%): ₹{gst_amount:.2f}")
            st.write(f"**Total: ₹{total:.2f}**")
            
            # Payment section
            st.markdown("---")
            discount = st.number_input("Discount Amount", min_value=0.0, value=0.0, step=10.0)
            payment_method = st.selectbox("Payment Method", ["Cash", "Card", "UPI"])
            
            final_total = total - discount
            if discount > 0:
                st.write(f"**Final Total: ₹{final_total:.2f}**")
            
            if st.button("💳 Generate Bill", type="primary"):
                if st.session_state.current_order:
                    order_id = save_order(payment_method, discount)
                    if order_id:
                        st.success(f"Order #{order_id} saved successfully!")
                        st.balloons()
                        st.rerun()
                else:
                    st.error("Please add items to the order")
            st.markdown('</div>', unsafe_allow_html=True)

def reports_page():
    st.markdown('<h2 class="header-text">Sales Reports</h2>', unsafe_allow_html=True)
    
    daily_sales, popular_items = get_sales_report()
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Total Orders", len(daily_sales))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Total Revenue", f"₹{daily_sales['revenue'].sum():.2f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        avg_order = daily_sales['revenue'].sum() / len(daily_sales) if len(daily_sales) > 0 else 0
        st.metric("Avg Order Value", f"₹{avg_order:.2f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Today's Orders", daily_sales.iloc[0]['orders'] if len(daily_sales) > 0 else 0)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<h3 class="subheader-text">Daily Sales (Last 7 Days)</h3>', unsafe_allow_html=True)
        if not daily_sales.empty:
            st.line_chart(daily_sales.set_index('date')['revenue'])
        else:
            st.info("No sales data available")
    
    with col2:
        st.markdown('<h3 class="subheader-text">Most Popular Items</h3>', unsafe_allow_html=True)
        if not popular_items.empty:
            st.bar_chart(popular_items.set_index('item_name')['total_quantity'])
        else:
            st.info("No order data available")
    
    # Detailed tables
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<h3 class="subheader-text">Daily Sales Details</h3>', unsafe_allow_html=True)
        st.dataframe(daily_sales, use_container_width=True)
    
    with col2:
        st.markdown('<h3 class="subheader-text">Popular Items Details</h3>', unsafe_allow_html=True)
        st.dataframe(popular_items, use_container_width=True)
    
    # Export options
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Export Sales Report (CSV)"):
            daily_sales.to_csv("sales_report.csv", index=False)
            st.success("Sales report exported as sales_report.csv")
    
    with col2:
        if st.button("📊 Export Popular Items (CSV)"):
            popular_items.to_csv("popular_items.csv", index=False)
            st.success("Popular items exported as popular_items.csv")

def menu_management_page():
    st.markdown('<h2 class="header-text">Menu Management</h2>', unsafe_allow_html=True)
    
    # Add new item
    st.markdown('<h3 class="subheader-text">Add New Menu Item</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        new_name = st.text_input("Item Name")
    with col2:
        new_category = st.selectbox("Category", ["Pizza", "Burger", "Pasta", "Salad", "Appetizer", "Beverage"])
    with col3:
        new_price = st.number_input("Price", min_value=0.0, value=0.0, step=10.0)
    with col4:
        new_gst = st.number_input("GST %", min_value=0.0, max_value=18.0, value=5.0, step=0.5)
    
    if st.button("➕ Add Item"):
        if new_name and new_price > 0:
            conn = sqlite3.connect('restaurant.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO menu (name, category, price, gst) VALUES (?, ?, ?, ?)",
                (new_name, new_category, new_price, new_gst)
            )
            conn.commit()
            conn.close()
            st.success(f"Added {new_name} to menu")
            st.rerun()
        else:
            st.error("Please fill all fields correctly")
    
    st.markdown("---")
    
    # Current menu
    st.markdown('<h3 class="subheader-text">Current Menu</h3>', unsafe_allow_html=True)
    menu_df = get_menu_items()
    st.dataframe(menu_df, use_container_width=True)
    
    # Delete item
    st.markdown('<h3 class="subheader-text">Delete Menu Item</h3>', unsafe_allow_html=True)
    item_to_delete = st.selectbox("Select item to delete", menu_df['name'].tolist())
    
    if st.button("🗑️ Delete Item"):
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM menu WHERE name = ?", (item_to_delete,))
        conn.commit()
        conn.close()
        st.success(f"Deleted {item_to_delete}")
        st.rerun()

if __name__ == "__main__":
    main()
