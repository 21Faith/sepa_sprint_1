#main.py
#This program illustrates various customer_product_operations in a sytstem.
#The program also goes further to illustrate the use of arrays in getting customer and product input details:
#Inserting of customer and product data, deleting customer and product information,
# updating both customer and product data and writing the data into a file.


from Customer_operations import *
from product_operations import *


customer_list = [["34678912", "Caren", "2345\n"],
                ["35679021", "Peter", "4578\n"],
                ["27689045","Floice", "2000\n"]
                 ]

product_list = [["00023", "Bread", 2, 50],
                ["\n00036", "Milk", 6, 65],
                ["\n00037", "soap", 1, 120]
                ]9


def main_menu():
    main_operation = int(input("Select your prefered operation: "
                       "1) = Customer operations"
                       "2) = Product operations"
                       "3 = Exit"))

    if main_operation == 1:
        customer_operation_menu()
    elif main_operation == 2:
        product_menu()
    elif main_operation == 3:
        exit()
    else:
        print("Invalid choice.")



def main():
   print("Welcome to our customer product system!")
   customer_operation_menu()
   product_menu()








