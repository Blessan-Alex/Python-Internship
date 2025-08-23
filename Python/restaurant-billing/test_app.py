"""
Test script for Restaurant Billing System
This script demonstrates the core functionality of the billing system.
"""

import sqlite3
import pandas as pd
from datetime import datetime

def test_database_connection():
    """Test database connection and table creation"""
    try:
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        
        # Check if tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print("✅ Database tables:", [table[0] for table in tables])
        
        # Check menu items
        cursor.execute("SELECT COUNT(*) FROM menu")
        menu_count = cursor.fetchone()[0]
        print(f"✅ Menu items count: {menu_count}")
        
        # Check orders
        cursor.execute("SELECT COUNT(*) FROM orders")
        orders_count = cursor.fetchone()[0]
        print(f"✅ Orders count: {orders_count}")
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def test_menu_data():
    """Test menu data retrieval"""
    try:
        conn = sqlite3.connect('restaurant.db')
        df = pd.read_sql_query("SELECT * FROM menu ORDER BY category, name", conn)
        conn.close()
        
        print("✅ Menu data retrieved successfully")
        print(f"   Total items: {len(df)}")
        print(f"   Categories: {df['category'].unique()}")
        
        # Display sample items
        print("\n📋 Sample Menu Items:")
        for _, item in df.head(5).iterrows():
            print(f"   • {item['name']} ({item['category']}) - ₹{item['price']}")
        
        return True
    except Exception as e:
        print(f"❌ Menu data test failed: {e}")
        return False

def test_bill_calculation():
    """Test bill calculation logic"""
    try:
        # Sample order items
        order_items = [
            {'name': 'Margherita Pizza', 'price': 299.0, 'quantity': 2},
            {'name': 'Coca Cola', 'price': 49.0, 'quantity': 2}
        ]
        
        # Calculate bill
        subtotal = sum(item['price'] * item['quantity'] for item in order_items)
        gst_rate = 5.0
        gst_amount = subtotal * (gst_rate / 100)
        total = subtotal + gst_amount
        
        print("✅ Bill calculation test:")
        print(f"   Subtotal: ₹{subtotal:.2f}")
        print(f"   GST (5%): ₹{gst_amount:.2f}")
        print(f"   Total: ₹{total:.2f}")
        
        return True
    except Exception as e:
        print(f"❌ Bill calculation test failed: {e}")
        return False

def test_sample_orders():
    """Test creating sample orders"""
    try:
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        
        # Sample order 1: Dine-in with multiple items
        cursor.execute('''
            INSERT INTO orders (order_type, total_amount, gst_amount, discount_amount, payment_method)
            VALUES (?, ?, ?, ?, ?)
        ''', ('Dine-In', 730.8, 34.8, 0.0, 'Card'))
        
        order_id = cursor.lastrowid
        
        # Add order items
        sample_items = [
            ('Margherita Pizza', 2, 299.0, 598.0),
            ('Coca Cola', 2, 49.0, 98.0)
        ]
        
        for item_name, quantity, price, total_price in sample_items:
            cursor.execute('''
                INSERT INTO order_items (order_id, item_name, quantity, price, total_price)
                VALUES (?, ?, ?, ?, ?)
            ''', (order_id, item_name, quantity, price, total_price))
        
        # Sample order 2: Takeaway with discount
        cursor.execute('''
            INSERT INTO orders (order_type, total_amount, gst_amount, discount_amount, payment_method)
            VALUES (?, ?, ?, ?, ?)
        ''', ('Takeaway', 375.85, 18.85, 20.0, 'UPI'))
        
        order_id2 = cursor.lastrowid
        
        sample_items2 = [
            ('Chicken Burger', 1, 199.0, 199.0),
            ('French Fries', 1, 99.0, 99.0),
            ('Coffee', 1, 79.0, 79.0)
        ]
        
        for item_name, quantity, price, total_price in sample_items2:
            cursor.execute('''
                INSERT INTO order_items (order_id, item_name, quantity, price, total_price)
                VALUES (?, ?, ?, ?, ?)
            ''', (order_id2, item_name, quantity, price, total_price))
        
        conn.commit()
        conn.close()
        
        print("✅ Sample orders created successfully")
        return True
    except Exception as e:
        print(f"❌ Sample orders test failed: {e}")
        return False

def test_reports():
    """Test sales reports generation"""
    try:
        conn = sqlite3.connect('restaurant.db')
        
        # Daily sales report
        daily_sales = pd.read_sql_query('''
            SELECT DATE(timestamp) as date, 
                   COUNT(*) as orders,
                   SUM(total_amount) as revenue
            FROM orders 
            GROUP BY DATE(timestamp)
            ORDER BY date DESC
        ''', conn)
        
        # Popular items report
        popular_items = pd.read_sql_query('''
            SELECT item_name, SUM(quantity) as total_quantity, SUM(total_price) as total_revenue
            FROM order_items
            GROUP BY item_name
            ORDER BY total_quantity DESC
        ''', conn)
        
        conn.close()
        
        print("✅ Reports generated successfully:")
        print(f"   Daily sales records: {len(daily_sales)}")
        print(f"   Popular items: {len(popular_items)}")
        
        if not daily_sales.empty:
            print(f"   Total revenue: ₹{daily_sales['revenue'].sum():.2f}")
        
        return True
    except Exception as e:
        print(f"❌ Reports test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Restaurant Billing System")
    print("=" * 50)
    
    tests = [
        ("Database Connection", test_database_connection),
        ("Menu Data", test_menu_data),
        ("Bill Calculation", test_bill_calculation),
        ("Sample Orders", test_sample_orders),
        ("Reports Generation", test_reports)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name} test...")
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} test failed")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The system is ready to use.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()
