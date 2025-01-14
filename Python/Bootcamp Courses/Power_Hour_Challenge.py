#!/usr/bin/env python
# coding: utf-8

# In[3]:


financial = {}
class User:
    def __init__(self, name, amount, payment, product):
        self.name = name
        self.amount = amount
        self.payment = payment
        self.product = product

#pre-populate data with a test
test = User('TEST', 0.0, True, 'PRODUCT')
financial['TEST'] = test.name, test.amount, test.payment, test.product

decision = int(input("How many customers would you like to add today? Enter 0 to print the list of existing customers and -1 to search from the existing database: "))
while(decision > 0):
    nm = str(input("What is this person's full name? "))
    amt = float(input("How much does this person owe? "))
    pay = bool(input("Has this person paid? Enter True or False. "))
    prod = str(input("What product(s) did this person buy? "))
    customer = User(nm, amt, pay, prod)
    financial[nm] = customer.name, customer.amount, customer.payment, customer.product
    decision = decision - 1
    
if(decision == -1):
    search = str(input("Enter the full name of the customer you are searching for: "))
    if search in financial.keys():
        print(financial[search])
    else:
        print("No customer exists in the current database using that name.")

decision = input("Enter -1 to search a customer, 0 to print the database, or the number of customers you would like to add to the database. ")

print("Thank you for using the system today. Here is a dictionary of all of the customers currently on file. The first customer is a test and should be disregarded.")
print("----------------------- DICTIONARY OF CURRENT CUSTOMERS ------------------------")
print(financial)


# In[ ]:




