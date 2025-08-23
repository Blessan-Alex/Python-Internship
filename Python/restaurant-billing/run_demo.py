#!/usr/bin/env python3
"""
Demo script for Restaurant Billing System
This script shows how to run the application and demonstrates its features.
"""

import os
import sys

def main():
    print("🍽️ Restaurant Billing System - Demo")
    print("=" * 50)
    
    # Check if required files exist
    required_files = ['app.py', 'requirements.txt', 'README.md']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return
    
    print("✅ All required files found")
    
    # Check if database exists
    if os.path.exists('restaurant.db'):
        print("✅ Database file exists")
    else:
        print("⚠️  Database file not found. Run 'python3 init_db.py' first")
        return
    
    print("\n🚀 To run the application:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run the app: streamlit run app.py")
    print("3. Open browser at: http://localhost:8501")
    
    print("\n📋 Features available:")
    print("• 📋 New Order - Create dine-in or takeaway orders")
    print("• 📊 Reports - View sales analytics and export data")
    print("• 🍽️ Menu Management - Add/remove menu items")
    
    print("\n🎯 Sample test orders created:")
    print("• Order #1: Dine-in with Margherita Pizza and Coca Cola")
    print("• Order #2: Takeaway with Chicken Burger, French Fries, and Coffee")
    
    print("\n📊 Reports available:")
    print("• Daily sales summary")
    print("• Popular items analysis")
    print("• Export to CSV functionality")
    
    print("\n✨ Beautiful minimalistic UI features:")
    print("• Clean, modern design with gradient backgrounds")
    print("• Smooth hover animations")
    print("• Professional color scheme")
    print("• Responsive layout")
    print("• Google Fonts (Inter) integration")
    
    print("\n🎉 The system is ready to use!")

if __name__ == "__main__":
    main()
