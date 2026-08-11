from db_connection import create_connection

def total_sales():
    connection=create_connection()
    cursor=connection.cursor()
    
    query='''SELECT COUNT(*) AS total_orders,SUM(quantity) AS total_plants_sold,SUM(total_amount) AS total_sales FROM sales'''
    
    cursor.execute(query)
    
    result=cursor.fetchone()
    
    print('\n*********** TOTAL SALES ***********')
    
    print('Total orders :',result[0])
    print('Total plant sold :',result[1])
    print('Total sales :₹',result[2])
    
    cursor.close()
    connection.close()
    
def available_stock():
    connection=create_connection()
    cursor=connection.cursor()
    
    query='''SELECT plant_id,plant_name,category,price,quantity 
    FROM plants ORDER BY plant_name'''
    
    cursor.execute(query)
    plants=cursor.fetchall()
    
    print('\n ********* AVAILABLE PLANT STOCK ***********')
    if plants:
        for plant in plants:
            print('ID         :', plant[0],
                  ' | Plant    :', plant[1],
                  ' | Category :', plant[2],
                  ' | Price    : ₹', plant[3],
                  ' | Avilable : ', plant[4]
                  )
    else:
        print('NO plants avilable')
        
    cursor.close()
    connection.close()
    
def low_stock_plants():
    connection=create_connection()
    cursor=connection.cursor()
    
    query='''SELECT plant_id,plant_name,category,quantity FROM plants WHERE quantity<=10 ORDER BY quantity'''
    
    cursor.execute(query)
    
    plants=cursor.fetchall()
    
    if plants:
        for plant in plants:
            print(plant)
    else:
        print('plant is not found')
    cursor.close()
    connection.close()
    
def customer_purchase_history():
    connection=create_connection()
    cursor=connection.cursor()
    
    customer_id=int(input('Enter the customer ID to see the purchase history: '))
    
    query='''SELECT s.sales_id,c.customer_name,p.plant_name,p.category,s.quantity,p.price,s.total_amount,s.sales_date 
    FROM sales s JOIN customer c ON s.customer_id = c.customer_id JOIN plants p ON s.plant_id=p.plant_id 
    WHERE s.customer_id = %s 
    ORDER BY s.sales_Date DESC'''
    
    cursor.execute(query,(customer_id,))
    purchases=cursor.fetchall()
    
    print('\n ************ CUSTOMER PURCHASE HISTORY *************')
    
    if purchases:
        
        for purchase in purchases:
            
            print(purchase)
            
    else:
        print(f'No purchase history found of this customer id is = {customer_id}')
    
    cursor.close()
    connection.close()
        