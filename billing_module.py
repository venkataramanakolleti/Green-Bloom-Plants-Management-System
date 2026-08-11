from db_connection import create_connection

def bill_details():
    connection=create_connection()
    cursor=connection.cursor()
    
    customer_id=int(input('Enter the customer ID : '))
    plant_id=int(input('Enter the plant ID : '))
    quantity=int(input('Enter the quantity of plant: '))
    
    query='''SELECT plant_name,price,quantity
    FROM plants WHERE plant_id = %s '''
    
    cursor.execute(query,(plant_id,))
    plant=cursor.fetchone()
    
    if plant is None:
        print('The Plant is not found...?')
        cursor.close()
        connection.close()
        return
    
    plant_name=plant[0]
    price=plant[1]
    available_quantity=plant[2]
    
    if quantity > available_quantity:
        print('The Plant is insufficient stock...?')
        cursor.close()
        connection.close()
        return
    
    total_amount=price * quantity
    
    sales_query='''INSERT INTO sales (customer_id,plant_id,quantity,total_amount,sales_date)VALUES(%s,%s,%s,%s,CURDATE())'''
    cursor.execute(sales_query,(customer_id,plant_id,quantity,total_amount))
    
    stock_query='''UPDATE plants SET quantity = quantity - %s WHERE plant_id = %s'''
    cursor.execute(stock_query,(quantity,plant_id))
    connection.commit()
    
    print('\n ********** BILL DETAILS **********')
    
    print('plant name: ',plant_name)
    print('price     : ₹', price)
    print('Quantity  :',quantity)
    print('Total amount :',total_amount)
    print('****************************')
    print('Plant Sale is completed successfully...')
    
    cursor.close()
    connection.close()