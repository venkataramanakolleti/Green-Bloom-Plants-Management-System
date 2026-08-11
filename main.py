from plant_module import (add_plant,view_plants,search_plant,update_plant,delete_plant)
from supplier_module import (add_supplier,view_suppliers,update_suppliers,delete_supplier)
from customer_module import (add_customer,view_customers,track_purchase)
from billing_module import bill_details
from reports_module import (total_sales,available_stock,low_stock_plants,customer_purchase_history)

def plant_menu():
     
    while True:
        
        print('\n *************** PLANT MANAGEMENT ***************')
        print('1. Add Plant')
        print('2. View Plants')
        print('3. Search Plant')
        print('4. Update Plant')
        print('5. Delete Plant')
        print('6. Back')
        
        choice = input('Enter your choice what do you see the details :')
        
        if choice == '1':
            add_plant()
            
        elif choice == '2':
            view_plants()
        
        elif choice == '3':
            search_plant()
        
        elif choice == '4':
            update_plant()
        
        elif choice == '5':
            delete_plant()
        
        elif choice == '6':
            break
            
        else:
            print('Invalid choice. please try again.')
            
def supplier_menu():

    while True:

        print('\n************** SUPPLIER MANAGEMENT ***************')
        print('1. Add Supplier')
        print('2. View Suppliers')
        print('3. Update Supplier')
        print('4. Delete Supplier')
        print('5. Back')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_supplier()

        elif choice == '2':
            view_suppliers()

        elif choice == '3':
            update_suppliers()
            
        elif choice == '4':
            delete_supplier()

        elif choice == '5':
            break

        else:
            print('Invalid choice. Please try again.')


def customer_menu():

    while True:

        print('\n***************** CUSTOMER MANAGEMENT **************')
        print('1. Add Customer')
        print('2. View Customers')
        print('3. Track Purchases')
        print('4. Back')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_customer()

        elif choice == '2':
            view_customers()

        elif choice == '3':
            track_purchase()
            
        elif choice == '4':
            break

        else:
            print('Invalid choice. Please try again.')


def report_menu():

    while True:

        print('\n *************** REPORTS ***************')
        print('1. Total Sales')
        print('2. Available Stock')
        print('3. Low Stock Plants')
        print('4. Customer Purchase History')
        print('5. Back')

        choice = input('Enter your choice: ')

        if choice == '1':
            total_sales()

        elif choice == '2':
            available_stock()

        elif choice == '3':
            low_stock_plants()

        elif choice == '4':
            customer_purchase_history()

        elif choice == '5':
            break

        else:
            print('Invalid choice. Please try again.')


def main():

    while True:

        print('\n')
        print('****************************************')
        print('          GREEN BLOOM PLANTS')
        print('****************************************')
        print('1. Plant Management')
        print('2. Supplier Management')
        print('3. Customer Management')
        print('4. Billing / Sales')
        print('5. Reports')
        print('6. Exit')
        print('*********************************')

        choice = input('Enter your choice: ')

        if choice == '1':
            plant_menu()

        elif choice == '2':
            supplier_menu()

        elif choice == '3':
            customer_menu()

        elif choice == '4':
            bill_details()

        elif choice == '5':
            report_menu()

        elif choice == '6':
            print('Thank you for using Green Bloom Plants!')
            break

        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
        