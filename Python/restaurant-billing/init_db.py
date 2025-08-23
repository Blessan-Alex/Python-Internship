import sqlite3
import pandas as pd

def init_database():
    """Initialize the restaurant billing database"""
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
        print("✅ Sample menu items added")
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")

if __name__ == "__main__":
    init_database()
