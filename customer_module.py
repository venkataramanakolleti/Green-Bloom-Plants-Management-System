from db_connection import create_connection

def add_customer():
    connection=create_connection()
    cursor=connection.cursor()
    
    customer_name=input('Enter the customer name: ')
    phone=input('Enter the phone number of customer:')
    email=input('Enter the customer email:')
    city=input('Enter the city:')
    
    query='''INSERT INTO customers(customer_name,phone,email,city)VALUES(%s,%s,%s,%s)'''
    values=(customer_name,phone,email,city)
    
    cursor.execute(query,values)
    connection.commit()
    
    cursor.close()
    connection.close()
    
def view_customers():
    connection=create_connection()
    cursor=connection.cursor()
    
    query='''SELECT * FROM customers'''
    cursor.execute(query)
    
    customers=cursor.fetchall()
    for customer in customers:
        print(customer)
        
    cursor.close()
    connection.close()
    
def track_purchase():
    connection=create_connection()
    cursor=connection.cursor()
    
    customer_id=int(input('Enter the customer ID to see the purchase history:'))
    query='''SELECT s.sales_id,p.plant_name,p.category,s.quantity,p.price,s.total_amount,s.sales_date 
    FROM sales s JOIN plants p ON s.plant_id = p.plant_id WHERE s.customer_id=%s ORDER BY s.sales_date'''
    
    cursor.execute(query,(customer_id,))
    purchases=cursor.fetchall()
    
    if purchases:
        
        print('\n ************ PURCHASE HISTORY OF CUSTOMER BY ************')
        
        for purchase in purchases:
            print(purchase)
    else:
        print('For this customer id there is no purchases...!')
        
    cursor.close()
    connection.close()
    

            
