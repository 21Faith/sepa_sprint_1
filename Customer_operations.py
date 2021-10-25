
#Enter customer data one by one(ID, name, address)
#Insert a new customer
#Delete a customer
#Update customer details using their ID
#Write customer data into a file

customer_list = [["34678912", "Caren", "2345"],
                ["35679021", "Peter", "4578"],
                ["27689045","Floice", "2000"]]



def menu():
    operations = input("Choose your operation: "
                       "1: customer "
                       "2: product")
    if operations == 1:
        c_operations = input("Choose your customer operation: "
                             "1: ")


def Customer_details():
    ID = input("Enter your ID: ")
    Name = input("Enter your name: ")
    Address = input("Enter your physical address: ")
    customer_data = [ID, Name, Address]
    customer_list.append(customer_data)
    return customer_list


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
    customer_data = [ID, Name, Address]
    customer_data[1:2] = ["New_Name", "New_Address"]
    print(customer_data)

update_info()

#file
def infile(customer_list):
    customers = open("customers.txt", "w")
    customers.write(str(customer_list))
    customers.close()
    print(customer_list)

infile()