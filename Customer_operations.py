
#Enter customer data one by one(ID, name, address)
#Insert a new customer
#Delete a customer
#Update customer details using their ID
#Write customer data into a file

customer_list = [ID: 34]

def Customer_details():
    ID = input("Enter your ID: ")
    Name = input("Enter your name: ")
    Address = input("Enter your physical address: ")
    customer_data = ["ID", "Name", "Address"]
    for a in customer_data:
        print(a)

Customer_details()

def delete():
    ID = input("Enter your ID: ")
    del ID
    print("Your data has been deleted!")

delete()

def update_info():
    customers = []
    ID = input("Enter your ID: ")
    Name = input("Enter your name: ")
    Address = input("Enter your Address: ")
    customer_data = ["ID", "Name", "Address"]
    customer_data[1:2] = ["New_Name", "New_Address"]
    print(customer_data)

update_info()

#file
def infile():
customers = open("customers.txt", "w")
customers.write(customers)
customers.close()

infile()