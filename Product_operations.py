
#product_operations.py
#This program shows various product operations for the various products in a system.
#The program also goes further to illustrate the use of arrays in getting product input details:
#Inserting new product data, delete deleting the product data entered, updating product data,
#writing the product data into a file and making a purchase.

product_list = [["00023", "Bread", 2, 50],
                ["00036", "Milk", 6, 65],
                ["00037", "soap", 1, 120]
                ]

def product_menu():
    p_operations = int(input("Choose a product operation: "
                             "1: Insert product data: "
                             "2: Delete product data: "
                             "3: Update product data: "
                             "4: Add product data to file: "
                             "5: Purchase a product: "))
    if p_operations == 1:
        product_details()
    elif p_operations == 2:
        delete()
    elif p_operations == 3:
        product_update()
    elif p_operations == 4:
        file(product_list)
    elif p_operations == 5:
        purchase()
    else:
        print("Invalid operation try again.")

def product_details():
    p_ID = input("Enter the product ID: ")
    p_Name = input("Enter product name: ")
    quantity = input("Enter amount: ")
    price = input("Enter the product's price: ")
    product_data =[p_ID, p_Name, quantity, price]
    product_list.append(product_data)
    print(product_list)
    products = open("product.txt", "w")
    products.write(str(product_list))
    return product_list


def delete():
    p_ID = int(input("Enter the product ID: "))
    for n in range(len(product_list)):
        if product_list[n][0] == p_ID:
            product_list.remove(product_list[n])
            break
    print(product_list)


def product_update():
    p_ID = int(input("Enter the product ID: "))
    for n in range(len(product_list)):
        if p_ID in product_list[0]:
            options = int(input("Choose what to change: "
                            "1: Name " 
                            "2: Quantity"
                            "3: Price"))
            if options == 1:
                new_name = input("Enter a new product name:")
                product_list[n][1] = new_name
            elif options == 2:
                new_quantity = input("Enter the new amount: ")
                product_list[n][2] = new_quantity
            elif options == 3:
                new_price = input("Enter a new price: ")
            else:
                print("Invalid option.")
            print(product_list)
            exit()


def file(product_list):
    product = open("products.txt", "w")
    product.write(str(product_list))
    product.close()
    print(product_list)


def purchase():
    customer_id = input("Enter customer id: ")
    p_id = input("Enter product id: ")
    p_quantity = int(input("Enter the number of products you wish to purchase: "))
    for n in range(len(product_list)):
        if p_id in product_list[n]:
            print(product_list[n][3])
            if p_quantity <= product_list[n]:
                New_amount = product_list[n] - p_quantity
                product_list[n] = New_amount
            else:
                print("product out of stock.")
        else:
            print("Product unavailable.")
    return product_list


product_menu()