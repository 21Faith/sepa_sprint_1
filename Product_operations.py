
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
    p_operations = input("Choose a product operation: "
                             "1: Enter product data: "
                             "2: Delete product data: "
                             "3: Update product data: "
                             "4: Add product data to file: "
                             "5: Purchase a product: ")
    if p_operations == 1:
        product_details()
    elif p_operations == 2:
        delete(product_list)
    elif p_operations == 3:
        product_update()
    elif p_operations == 4:
        file(product_list)
    elif p_operations == 5:
        purchase
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
    product_id = input("Enter product id: ")
    product_quantity = int(input("Enter the number of products you wish to purchase: "))
    for i in range(len(product_list)):
        if product_id in product_list[i]:
            print(product_list[i][3])
            if product_quantity <= product_list[i]:
                New_amount = product_list[i] - product_quantity
                product_list[i] = New_amount
            else:
                print("product out of stock.")
        else:
            print("Product unavailable.")
    print(product_list)

purchase()

