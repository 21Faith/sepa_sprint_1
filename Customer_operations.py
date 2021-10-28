
#Customer_operations.py
#This program illustrates various customer operations in a sytstem.
#The program also goes further to illustrate the use of arrays in getting customer input details:
# New customer data, deleting customer information, updating customer data and writing the customer data into a file.

customer_list = [["34678912", "Caren", "2345"],
                ["35679021", "Peter", "4578"],
                ["27689045","Floice", "2000"]
                 ]


def menu():
    operations = input("Choose your operation: "
                       "1: customer "
                       "2: product")
    if operations == 1:
        c_operations = input("Choose your customer operation: "
                             "1: Input customer data: "
                             "2: Delete customer data: "
                             "3: Updating customer data : "
                             "4: Add customer data to file: ")
    elif operations == 2:
        p_operations = input("Choose a product operation: "
                             "1: Enter product data: "
                             "2: Delete product data: "
                             "3: Update product data: "
                             "4: Add product data to file: "
                             "5: Purchase a product: ")
    else:
        print("Invalid operation try again.")


def Customer_details():
    ID = input("Enter your ID: ")
    Name = input("Enter your name: ")
    Address = input("Enter your physical address: ")
    customer_data = [ID, Name, Address]
    customer_list.append(customer_data)
    return customer_list

def delete(customer_list):
    ID = input("Enter your ID: ")
    Name = input("Enter your name: ")
    Address = input("Enter your physical address: ")
    customer_data = [ID, Name, Address]
    for c in customer_list():
        if c == (ID):
            del customer_data
            print("Your data has been deleted!")

def update_info():

    customer_list = []
    ID = input("Enter your ID: ")
    Name = input("Enter your name: ")
    Address = input("Enter your Address: ")
    customer_data = [ID, Name, Address]
    #customer_data = customer_data2
    New_Name = ""
    New_Address = ""
    customer_data2 = [ID, New_Name, New_Address]
    customer_data2.append(customer_list)
    print("Your updated information is: ",ID, New_Name, New_Address)


def infile(customer_list):
    customers = open("customers.txt", "w")
    customers.write(str(customer_list))
    customers.close()
    print(customer_list)
