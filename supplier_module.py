from db_connection import create_connection

def add_supplier():
    connection=create_connection()
    cursor=connection.cursor()
    
    supplier_name=input('Enter the supplier name: ')
    phone_num=input('Enter supplier phone number: ')
    city=input('Enter the supplier city: ')
    
    query='''INSERT INTO suppliers(supplier_name,phone_num,city)VALUES(%s,%s,%s)'''
    values=(supplier_name,phone_num,city)
    
    cursor.execute(query,values)
    connection.commit()
    
    print('Supplier added successfully...')
    
    cursor.close()
    connection.close()
    
def view_suppliers():
    connection=create_connection()
    cursor=connection.cursor()
    
    query='''SELECT supplier_id,supplier_name,phone_num,city FROM suppliers'''
    cursor.execute(query)
    suppliers=cursor.fetchall()
    
    print('\n ********** supplier details are *********')
    
    for supplier in suppliers:
        
        print(supplier)
    
    cursor.close()
    connection.close()
    
def update_suppliers():
    connection=create_connection()
    cursor=connection.cursor()
    
    supplier_id=int(input('Enter the supplier ID to update details: '))
    new_phone=input('Enter the new phone number of supplier: ') 
    new_city=input('Enter new city: ')
    
    query='''UPDATE suppliers SET phone_num=%s,city=%s WHERE supplier_id =%S'''
    values=(supplier_id,new_phone,new_city)
    cursor.execute(query,values)
    connection.commit()
    
    if cursor.rowcount > 0:
        print('Supplier details update successfully....!')
        
    else:
        print('Supplier ID not found')
        
    cursor.close()
    connection.close()
    
def delete_supplier():
    connection=create_connection()
    cursor=connection.cursor()
    
    supplier_id=int(input('Enter the supplier ID to delete: '))
    
    query='''DELETE FROM suppliers WHERE supplier_id = %s'''
    cursor.execute(query,(supplier_id,))
    connection.commit()
    
    if cursor.rowcount > 0:
        print('Supplier deleted successfully..!')
    else:
        print('Supplier ID not found')
        
    cursor.close()
    connection.close()
    
    
    
    