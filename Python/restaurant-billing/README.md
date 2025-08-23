# 🍽️ Restaurant Billing System

A beautiful, minimalistic restaurant billing system built with Python and Streamlit. This application provides a complete solution for restaurant order management, billing, and sales reporting.

## ✨ Features

### 📋 Order Management
- **Dine-In & Takeaway Support**: Handle both dine-in and takeaway orders
- **Interactive Menu**: Easy item selection with quantity controls
- **Real-time Bill Calculation**: Automatic GST calculation and discount application
- **Multiple Payment Methods**: Support for Cash, Card, and UPI payments
- **Order History**: Complete transaction tracking with timestamps

### 📊 Sales Reports
- **Daily Sales Analytics**: Track revenue and order counts
- **Popular Items Analysis**: Identify best-selling menu items
- **Visual Charts**: Interactive line and bar charts for data visualization
- **Export Functionality**: Export reports as CSV files

### 🍽️ Menu Management
- **Add/Remove Items**: Dynamic menu management
- **Category Organization**: Organized menu by food categories
- **Price & GST Management**: Flexible pricing with customizable GST rates

### 🎨 Beautiful UI
- **Minimalistic Design**: Clean, modern interface
- **Responsive Layout**: Works on different screen sizes
- **Smooth Animations**: Hover effects and transitions
- **Professional Color Scheme**: Elegant gradient backgrounds

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Database**: SQLite3 (Lightweight, file-based database)
- **Data Processing**: Pandas (Data manipulation and analysis)
- **Styling**: Custom CSS with Google Fonts (Inter)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd restaurant-billing
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   - The application will open automatically at `http://localhost:8501`
   - If not, manually navigate to the URL shown in the terminal

## 🚀 Usage

### Creating Orders
1. Navigate to "📋 New Order" in the sidebar
2. Select order type (Dine-In or Takeaway)
3. Browse the menu and add items with desired quantities
4. Review your order in the right panel
5. Apply any discounts if needed
6. Select payment method
7. Click "Generate Bill" to complete the order

### Viewing Reports
1. Go to "📊 Reports" in the sidebar
2. View summary metrics and charts
3. Export data as CSV files if needed

### Managing Menu
1. Access "🍽️ Menu Management" in the sidebar
2. Add new items with name, category, price, and GST
3. View current menu items
4. Delete items as needed

## 📁 Project Structure

```
restaurant-billing/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── restaurant.db         # SQLite database (created automatically)
├── sales_report.csv      # Exported sales reports
└── popular_items.csv     # Exported popular items data
```

## 🗄️ Database Schema

### Menu Table
- `id`: Primary key
- `name`: Item name
- `category`: Food category
- `price`: Item price
- `gst`: GST percentage

### Orders Table
- `id`: Primary key
- `order_type`: Dine-In or Takeaway
- `total_amount`: Final bill amount
- `gst_amount`: GST amount
- `discount_amount`: Applied discount
- `payment_method`: Payment type
- `timestamp`: Order timestamp

### Order Items Table
- `id`: Primary key
- `order_id`: Foreign key to orders
- `item_name`: Item name
- `quantity`: Item quantity
- `price`: Unit price
- `total_price`: Total price for this item

## 🎯 Sample Data

The application comes with pre-loaded sample menu items:
- **Pizza**: Margherita Pizza (₹299), Pepperoni Pizza (₹349)
- **Burger**: Chicken Burger (₹199), Veg Burger (₹149)
- **Pasta**: Pasta Carbonara (₹249)
- **Salad**: Caesar Salad (₹179)
- **Appetizer**: Chicken Wings (₹299), French Fries (₹99)
- **Beverage**: Coca Cola (₹49), Coffee (₹79)

## 📊 Features in Detail

### Bill Generation
- Automatic GST calculation (5% by default)
- Optional discount application
- Itemized bill display
- Multiple payment method support
- Order confirmation with unique ID

### Sales Analytics
- Daily revenue tracking
- Order count monitoring
- Average order value calculation
- Popular items identification
- Export capabilities for further analysis

### User Experience
- Intuitive navigation
- Real-time updates
- Success/error notifications
- Responsive design
- Clean, professional appearance

## 🔧 Customization

### Adding New Categories
Edit the category list in the menu management section to add new food categories.

### Modifying GST Rates
Change the default GST rate in the `calculate_bill()` function or set per-item GST rates.

### Styling Changes
Modify the CSS in the `st.markdown()` section to customize colors, fonts, and layout.

## 📝 License

This project is created for educational purposes as part of an internship project.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Note**: This is a complete restaurant billing solution that meets all the requirements specified in the project guide, with a focus on beautiful, minimalistic design and user experience.
