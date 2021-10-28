
#search for a product(with its price and amount)
#List all customers
#List all products
#list a customers; name,products purchased(amounts too), money spent
#Quit

customer_list = [["34678912", "Caren", "2345"],
                ["35679021", "Peter", "4578"],
                ["27689045","Floice", "2000"]]

product_list = [["00023", "Breadd", 2, 50],
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

def search():
    for i in product_list(:



