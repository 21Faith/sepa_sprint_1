
#Customer_operations.py
#This program illustrates various customer operations in a sytstem.
#The program also goes further to illustrate the use of arrays in getting customer input details:
# New customer data, deleting customer information, updating customer data and writing the customer data into a file.

from customer_class import customer
customer_list = customer



customer_list = [[2300685,"Trevor", 567],
                 [4567045, "Bernice", 235],
                 [3456775, "Amanda", 800]
                 ]


def customer_operation_menu():
    c_operations = int(input("Choose your customer operation: "
                             "1: Input customer data: "
                             "2: Delete customer data: "
                             "3: Updating customer data : "
                             "4: Add customer data to file: "))


    if c_operations == 1:
            Customer_details()
    elif c_operations == 2:
            delete()
    elif c_operations == 3:
            update_info()
    elif c_operations == 4:
            infile(customer_list)
    else:
            print("Invalid operation try again.")


def Customer_details():
    ID = input("Enter your ID: ")
    Name = input("Enter your name: ")
    Address = input("Enter your physical address: ")
    customer_data = [ID, Name, Address]
    customer_list.append(customer_data)
    print(customer_list)
    customers = open("customers.txt", "w")
    customers.write(str(customer_list))
    return customer_list


def delete():
    ID = int(input("Enter your ID: "))
    for c in range(len(customer_list)):
        if customer_list[c][0] == ID:
            customer_list.remove(customer_list[c])
            break
    print(customer_list)


def update_info():
    ID = int(input("Enter your ID: "))
    for i in range(len(customer_list)):
        if ID in customer_list[0]:
            options = int(input("Choose what to change: "
                            "1: Name " 
                            "2: Address"))
            if options == 1:
                new_name = input("Enter the new name:")
                customer_list[i][1] = new_name
            elif options == 2:
                new_address = input("Enter the new address: ")
                customer_list[i][2] = new_address
            else:
                print("Invalid option.")
            print(customer_list)
            exit()


def infile(customer_list):
    customers = open("customers.txt", "w")
    customers.write(str(customer_list))
    customers.close()
    print(customer_list)


customer_operation_menu()
