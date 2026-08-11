CREATE DATABASE IF NOT EXISTS green_bloom_db;

USE green_bloom_db;

CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(100),
    phone_num VARCHAR(15),
    city VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS plants (
    plant_id INT PRIMARY KEY,
    plant_name VARCHAR(100),
    category VARCHAR(50),
    price FLOAT,
    quantity INT,
    supplier_id INT,
    FOREIGN KEY (supplier_id)
        REFERENCES suppliers(supplier_id)
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS sales (
    sales_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    plant_id INT NOT NULL,
    quantity INT NOT NULL,
    total_amount FLOAT,
    sales_date DATE,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),
    FOREIGN KEY (plant_id)
        REFERENCES plants(plant_id)
);