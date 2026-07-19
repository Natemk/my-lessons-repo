"""class Shop:
    def __init__(self, location, product, price):
        self.location = location
        self.product = product
        self.price = float(price)
        
class Construction:
    def __init__(self, machinery, contract, site):
        self.machinery = machinery
        self.contract = contract
        self.site = site


class Math:
    def __init__(self, divide, multiply, add, subtract):
        self.divide = divide
        self.multiply = multiply
        self.add = add
        self.subtract = subtract
    
job = Construction(" excavator", "building contract", "construction site")
shop = Shop("Mutare", "Cement",10.040 )

#print(f"Machinery: {job.machinery}, Contract: {job.contract}, Site: {job.site}")
print(f"Location: {shop.location}, Product: {shop.product}, Price: {shop.price}")
    
#shop - location, product, price
#construction -machinery, contract and site
#math -divide, multiply, add, subtract


class student:
    def __init__(self):
        print(self)
        
student1 = student()



class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = int(salary)
        
employee1 = Employee("John Doe", "Engineering", 75000)

print(f"Employee Name: {employee1.name}, Department: {employee1.department}, Salary: {employee1.salary}")
    
    
        
class Car:
    def __init__(self, name):
        self.name = name
        
    def drive(self):
            
            print(f"{self.name} is driving.")
            
toyota = Car("Toyota")
toyota.drive()

Mini Project 1 — Student Management

Create:

Student

Properties

Name
Age
Course

Method
introduce()
output:
Hi

My name is John

I study Python

I am 22 years old


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
      
    def introduce(self):
        print(f"Hi\nMy name is {self.name}\nI study {self.course}\nI am {self.age} years old")  
        
student1 = Student("John", 22, "Python")   
student1.introduce()       

Mini Project 2 — Bank Account

Class

BankAccount

Properties

Owner
Balance

Methods

Deposit

Withdraw

Check Balance

Example:
account.deposit(500)

account.withdraw(100)

account.check_balance()

Use validation so withdrawals cannot exceed the balance.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        
acc1 = BankAccount("Alice", 1000)
acc1.deposit(500)
acc1.withdraw(200)
acc1.check_balance()
acc1.withdraw(2000)  # Attempt to withdraw more than the balance


Mini Project 3 — Inventory Item

Class

InventoryItem

Properties

Name
Quantity
Price

Methods

Add stock
Remove stock
Calculate inventory value (quantity * price)

Instantiate multiple inventory items and display their values.


class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = float(price)

    def add_stock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Added {amount} to {self.name}. New quantity: {self.quantity}")
        else:
            print("Amount to add must be positive.")

    def remove_stock(self, amount):
        if amount > 0:
            if amount <= self.quantity:
                self.quantity -= amount
                print(f"Removed {amount} from {self.name}. New quantity: {self.quantity}")
            else:
                print("Insufficient stock to remove that amount.")
        else:
            print("Amount to remove must be positive.")

    def calculate_inventory_value(self):
        return self.quantity * self.price

doors = InventoryItem("Doors", 50, 20)
doors.add_stock(20)
doors.remove_stock(10)
print(doors.calculate_inventory_value())
==============================================

Homework Project — Library Management System

Build a console application using OOP.

Create at least three classes:

Book
Attributes: title, author, ISBN, available
Methods: borrow(), return_book()
Member
Attributes: name, member_id, borrowed_books
Methods: borrow_book(), return_book()
Library
Attributes: books, members
Methods:
add_book()
register_member()
list_available_books()
search_by_title()

Requirements:

Use constructors for initialization.
Store books and members in lists.
Prevent borrowing unavailable books.
Display clear status messages.
Organize the project into multiple modules (book.py, member.py, library.py, main.py).

This project reinforces every major concept from the lesson: classes, objects, constructors,
attributes, methods, object interaction, and modular code organization.
        
"""

    