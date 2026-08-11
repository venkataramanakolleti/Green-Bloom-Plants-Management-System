import mysql.connector

def create_connection():

    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='YOUR_MYSQL-PASSWORD',
        database='green_bloom_db' 
    )
    return connection
