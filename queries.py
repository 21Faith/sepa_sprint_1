
#search for a product(with its price and amount)
#List all customers
#List all products
#list a customers; name,products purchased(amounts too), money spent
#Quit

#import Product_operations


product_list = [["00023", "Bread", 2, 50],
                ["00036", "Milk", 6, 65],
                ["00037", "soap", 1, 120]
                ]

def product_search():
    p_ID = input("Enter the product ID: ")
    #p_Name = input("Enter product name: ")
    #quantity = input("Enter amount: ")
    #price = input("Enter the product's price: ")
    #product_data = [p_ID, p_Name, quantity, price]
    #product_list.append(product_data)
    for n in range(len(product_list)):
        if p_ID in product_list[0]:
            search = int(input("Choose a search option: "
                                "1: Product name "
                                "2: Product quantity "
                                "3: Product price "))

            if search == 1:
                new_name = input("Enter a new product name:")
                product_list[n][1] = new_name
            elif search == 2:
                new_quantity = input("Enter the new amount: ")
                product_list[n][2] = new_quantity
            elif search == 3:
                new_price = input("Enter a new price: ")
                product_list[n][3] = new_price
            else:
                print("Invalid option.")
            print(product_list)


product_search()
