#First Function 
"""
def greet(name):
    print("Hello", name)

greet("John") 



def add(num1, num2):
    return(num1 + num2)



result = add(3,4)

print(result)


def calculate_tax(amount):
    return amount * 0.3

subtotal =int(input("Enter subtotal"))

tax = int( calculate_tax (subtotal))

print(tax)



def get_name():
    pass
def calculate_tax(amount):
    pass
def display_receipt(name, subtotal, tax, total):
    pass

Use the above functions together to build a mini checkout system

In class work:

Create a function that converts Celsius to Fahrenheit.
Create a function that calculates the area of a rectangle.
Create a function that determines whether a number is even or odd.
Create a function that calculates the average of three numbers.
Create a function called is_adult(age) that returns True if age is 18 or older and False otherwise.
"""


def get_name():
    name = input ("Enter customer name:")
    return name

def calculate_tax(amount):
    tax = amount * 0.3
    return tax

def display_receipt(name, subtotal, tax, total):
    print("\-----------RECEIPT------------")
    print("Customer Name:", name)
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Total:", total)

#Main Program
name = get_name()

subtotal = float(input("Enter subtotal:"))
tax = calculate_tax(subtotal)
total = subtotal + tax
display_receipt(name, subtotal, tax, total)
