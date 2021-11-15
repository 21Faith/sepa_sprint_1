#customer_class.py
#This program illustrates creation of classes and objects in customer operations system.

#import Customer_operations

class customer:

    def __init__(self, ID, name, Address):
        self.ID = ID
        self.name = name
        self.Address = Address


customer1 = customer(2356, "Daniel", 200)
customer2 = customer(3475, "pamela", 459)
customer3 = customer(4580, "Christine", 435)



