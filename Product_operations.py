
#product_operations.py
#This program shows various product operations for the various products in a system.
#The program also goes further to illustrate the use of arrays in getting product input details:
#Inserting new product data, delete deleting the product data entered, updating product data,
#writing the product data into a file and making a purchase.

product_list = [["00023", "Bread", 2, 50],
                ["00036", "Milk", 6, 65],
                ["00037", "soap", 1, 120]
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



def product_details():
    ID = input("Enter product ID: ")
    Name = input("Enter the product's name: ")
    Quantity = input("How many products do you wish to purchase: ")
    Price = input("Enter each product's price: ")
    product_data = [ID, Name, Quantity, float(Price)]
    product_list.append(product_data)
    return product_list


def delete():
    ID = input("Enter product ID: ")
    Name = input("Enter the product's name: ")
    Quantity = input("How many products do you wish to purchase: ")
    Price = input("Enter each product's price: ")
    product_data = [ID, Name, Quantity, float(Price)]
    for p in product_list():
        if p == (ID):
            del ID
            print("Product data has been deleted!")


def product_update():
    product_list = []
    ID = input("Enter product ID: ")
    Name = input("Enter the product's name: ")
    Quantity = input("How many products do you wish to purchase: ")
    Price = input("Enter each product's price: ")
    product_data = [ID, Name, Quantity, float(Price)]
    New_name = ""
    New_Quantity = ""
    New_Price = ""
    product_data[1:4] = [New_name, New_Quantity, New_Price]
    product_data.append(product_list)
    print("New product details are: \n",  ID, New_name, New_Quantity, New_Price)


def file():
    product_file = open("products.txt", "w")
    product_file.write("product_list")
    product_file.close()

def purchase():
    customer_id = input("Enter customer id: ")
    product_name = input("Enter product to purchase: ")
    product_quantity = int(input("Enter the number of products you wish to purchase: "))
    for i in range(len(product_list)):
        if product_name in product_list[i]:
            if product_quantity <= int(product_list[i]):
                New_amount = int(product_list[i]) - product_quantity
                product_list[i] = New_amount
            else:
                print("product out of stock.")
        else:
            print("Product unavailable.")
    print(product_list)

purchase()
