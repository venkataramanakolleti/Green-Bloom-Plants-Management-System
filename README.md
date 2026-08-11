# 🌱 Green Bloom Plants Management System

## 📌 Project Overview

Green Bloom Plants Management System is a **Python and MySQL based console application** developed to manage plant inventory, suppliers, customers, sales, and business reports.

The application uses **Python for the application logic** and **MySQL for storing and managing data**.

The project follows a modular structure where different operations are separated into different Python modules.

---

## 🎯 Project Objectives

* Manage plant information
* Manage supplier information
* Manage customer information
* Process plant sales
* Automatically calculate total sales amount
* Automatically reduce plant stock after a sale
* Track customer purchase history
* Generate business reports
* Connect Python application with MySQL database

---

## 🛠️ Technologies Used

* Python
* MySQL
* MySQL Connector/Python
* SQL
* VS Code
* MySQL Workbench

---

## 🗄️ Database Design

The project contains four tables:

### 1. Suppliers

Stores supplier information.

Main columns:

* supplier_id
* supplier_name
* phone_num
* city

### 2. Plants

Stores plant and inventory information.

Main columns:

* plant_id
* plant_name
* category
* price
* quantity
* supplier_id

### 3. Customers

Stores customer information.

Main columns:

* customer_id
* customer_name
* phone
* email
* city

### 4. Sales

Stores customer purchase information.

Main columns:

* sales_id
* customer_id
* plant_id
* quantity
* total_amount
* sales_date

---

## 🔗 Database Relationships

The database uses foreign keys to establish relationships.

```text
Suppliers
    |
    | supplier_id
    ↓
Plants
    |
    | plant_id
    ↓
Sales
    ↑
    | customer_id
    |
Customers
```

### Relationships

* One supplier can supply multiple plants.
* One customer can make multiple purchases.
* One plant can appear in multiple sales records.

---

## 🔄 Sales Workflow

The billing process follows these steps:

```text
1. Customer selects plant
          ↓
2. User enters quantity
          ↓
3. Calculate total amount
          ↓
4. Store sales record
          ↓
5. Reduce stock quantity
```

For example:

```text
Plant Price = ₹150
Quantity = 3

Total Amount = ₹150 × 3
             = ₹450
```

After the sale, the available plant quantity is automatically reduced.

---

## 📊 Reports

The application generates the following reports:

### Total Sales

Displays:

* Total number of orders
* Total plants sold
* Total sales amount

### Available Stock

Displays:

* Plant ID
* Plant name
* Category
* Price
* Available quantity

### Low Stock Plants

Displays plants whose available quantity is **10 or less**.

### Customer Purchase History

Displays the purchase history of a selected customer, including:

* Sale ID
* Customer name
* Plant name
* Category
* Quantity
* Price
* Total amount
* Sales date

---

## 📁 Project Structure

```text
Green_Bloom_Project/
│
├── main.py
│
├── db_connection.py
│
├── plant_module.py
├── supplier_module.py
├── customer_module.py
├── billing_module.py
├── reports_module.py
│
├── database.sql
├── requirements.txt
└── README.md
```

---

## 📄 Module Description

### `main.py`

Controls the main application menu and connects all modules.

### `db_connection.py`

Creates the connection between Python and MySQL.

### `plant_module.py`

Handles plant management operations such as:

* Add plant
* View plants
* Search plant
* Update plant
* Delete plant

### `supplier_module.py`

Handles supplier management operations.

### `customer_module.py`

Handles customer management and customer purchase tracking.

### `billing_module.py`

Handles sales and billing operations.

### `reports_module.py`

Generates business reports such as:

* Total sales
* Available stock
* Low stock plants
* Customer purchase history

### `database.sql`

Contains the SQL commands required to create the database and tables.

### `requirements.txt`

Contains the Python dependency required by the project.

---

## ⚙️ Installation

### Step 1: Install Python

Install Python on your computer.

### Step 2: Clone or download the project

Open the project folder in VS Code.

### Step 3: Install required Python package

Open the terminal and run:

```bash
pip install -r requirements.txt
```

### Step 4: Create the database

Open MySQL Workbench and create the `green_bloom_db` database and its four tables using `database.sql`.

### Step 5: Configure database connection

Open:

```text
db_connection.py
```

Update the MySQL connection details:

```python
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='YOUR_MYSQL_PASSWORD',
    database='green_bloom_db'
)
```

### Step 6: Run the application

From the project folder:

```bash
python main.py
```

---

## 🖥️ Main Menu

The application provides the following main options:

```text
========================================
          GREEN BLOOM PLANTS
========================================

1. Plant Management
2. Supplier Management
3. Customer Management
4. Billing / Sales
5. Reports
6. Exit
```

---

## 📌 Key Features

* Modular Python architecture
* MySQL database integration
* CRUD operations
* Foreign key relationships
* Sales and billing management
* Automatic stock reduction
* Customer purchase tracking
* Business reports
* Exception handling
* SQL queries with parameterized values

---

## 🚀 Future Enhancements

Possible future improvements include:

* Graphical user interface
* Web-based application
* User authentication
* Online payment integration
* Sales dashboard
* Advanced inventory alerts
* Export reports to Excel or PDF

---

## 👨‍💻 Developer

**Venkata Ramana Kolleti**

B.Tech – Computer Science and Engineering
