import mysql.connector

def create_connection():

    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='YOUR_MYSQL_PASSWORD',
        database='green_bloom_db' 
    )
    return connection
