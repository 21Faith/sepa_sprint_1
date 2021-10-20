
#Enter product data one by one
#Insert a new product
#Delete a product
#Update product details using product ID
#Write product data into a file
#purchase(should also check whether there are enough products to purchase)(customer ID, Product ID & amount )


def product_details():
    ID = input("Enter product ID: ")
    Name = input("Enter the product's name: ")
    Quantity = input("How many products do you wish to purchase: ")
    Price = input("Enter each product's price: ")
    product_data = ["ID", "Name", int("Quantity"), float("Price")]
    print(product_data)

product_details()


def delete():
    ID = input("Enter product ID: ")
    del ID
    print("Product has been deleted.")


def product_update():
    product = []
    ID = input("Enter product ID: ")
    Name = input("Enter the product's name: ")
    Quantity = input("How many products do you wish to purchase: ")
    Price = input("Enter each product's price: ")
    product_data = ["ID", "Name", int("Quantity"), float("Price")]
    for i in product_data:
        print(i)


product_update()


#File
product_file = open("products.txt", "w")
product_file.write()
product_file.close()

