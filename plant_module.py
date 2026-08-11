from db_connection import create_connection
import mysql.connector

def add_plant():
    
    
    try:
    
        plant_id=int(input('Enter plant ID:'))
        plant_name=input('Enter plant name:')
        category=input('Enter category:')
        price=float(input('ENTER price:'))
        quantity=int(input('Enter quantity :'))
        supplier_id=int(input('Enter supplier ID:'))
        
        connection=create_connection()
        cursor=connection.cursor()
        
        query='''INSERT INTO plants
        (plant_id,plant_name,category,price,quantity,supplier_id)
        VALUES(%s,%s,%s,%s,%s,%s)'''
        
        values=(
            plant_id,
            plant_name,
            category,
            price,
            quantity,
            supplier_id
        )
        
        cursor.execute(query,values)
        connection.commit()
        
        print('plant added successfully')
        
        cursor.close()
        connection.close()
    except ValueError:
        print('please enter valid numeric values...')
    
    except mysql.connector.Error as error:
        print('Dtabase error:',error)
    
def view_plants():
    connection=create_connection()
    cursor=connection.cursor()
    
    query='''SELECT p.plant_id,p.plant_name,p.category,p.price,p.quantity,s.supplier_name FROM plants p JOIN suppliers s ON p.supplier_id=s.supplier_id'''
    
    cursor.execute(query)
    plants=cursor.fetchall()
    
    for plant in plants:
        print(plant)
        
    cursor.close()
    connection.close()

def search_plant():
    connection=create_connection()
    cursor=connection.cursor()
    
    plant_name=input('Enter plant name to search :')
    
    query='''SELECT p.plant_id,p.plant_name,p.category,p.price,p.quantity,s.supplier_name
    FROM plants p JOIN suppliers s ON p.supplier_id = s.supplier_id
    WHERE p.plant_name LIKE %s'''
    
    cursor.execute(query,(f'%{plant_name}%',))
    
    plants=cursor.fetchall()
    
    if plants:
        for plant in plants:
            print(plant)
    else:
        print('plant not found')
    
    cursor.close()
    connection.close()
    
def update_plant():
    connection=create_connection()
    cursor=connection.cursor()
    
    plant_id=input('Enter plant ID to update the details of plant :')
    new_price=float(input('Please Enter new price of the plant : '))
    new_quantity=int(input('Please Enter the new quantity count : '))
    
    query='''UPDATE plants SET price = %s,quantity=%s WHERE plant_id=%s'''

    values=(plant_id,new_price,new_quantity)
    
    cursor.execute(query,values)
    connection.commit()
    
    if cursor.rowcount > 0 :
        print('Plant updated successfully ...!')
        
    else:
        print('Plant ID is not found to update...?')
        
        
    cursor.close()
    connection.close()
    
def delete_plant():
    connection=create_connection()
    cursor=connection.cursor()
    
    plant_id=int(input('Enter the plant ID details to delete the plant information...?'))
    
    query='''DELETE FROM plant WHERE plant_id=%s'''
    cursor.execute(query,(plant_id,))
    connection.commit()
    
    if cursor.rowcount > 0:
        print('Plant is deleted successfully...!')
    else:
        print('Plant ID is not found...?')
        
    cursor.close()
    connection.close()
    