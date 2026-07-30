#Object Oriented Programming.
"""
What problem does OOP actually try to address?
OOP (Object-Oriented Programming) addresses several problems in software development, including:
1. **Code Reusability**: OOP allows developers to create classes that can be reused across 
different parts of a program or even in different programs,    
reducing redundancy and improving maintainability.
2. **Encapsulation**: OOP promotes the bundling of data and methods that operate on that data 
within classes, which helps to hide the internal state of objects and protect it from unintended interference and misuse.
3. **Abstraction**: OOP enables developers to create abstract classes and interfaces, 
allowing them to define common behaviors and properties without exposing 
the underlying implementation details.
4. **Inheritance**: OOP allows classes to inherit properties and behaviors from other classes,
    which promotes code reuse and establishes a natural hierarchy between classes.
5. **Polymorphism**: OOP supports polymorphism, which allows objects of different classes to be treated 
as objects of a common superclass. This enables developers to write more flexible and extensible code, 
as they can use the same interface to interact with different types of objects.



Instead of creating millions of variables, 
OOP allows us to create classes that can be used to create objects.

#Class blueprint
class Student:
    pass

#Object creation

john = Student()  # Creating an object of the Student class
sarah = Student()  # Creating another object of the Student class

def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

john =Student("John", 20, "A")  # Creating an object of the Student class with attributes
sarah = Student("Sarah", 22, "B")  # Creating another object of the Student class with attributes

john = Student("John", 20, "A")  # Creating an object of the Student class with attributes
Whenever we create our object i.e John, the __init__ method is automatically called and the attributes
 are initialized with the values provided.

Methods: (objects can store values i.e parameteres but they can also perform actions i.e methods)
"""
import email
'''
class Student:

    def __init__(self, name):
        self.name = name

    def study(self):
        print(self.name, "is studying")

john = Student("John")

john.study()  # Output: John is studying
'''
'''
class ITSupport:
    def __init__(self, name, department, title):
        self.name = name
        self.department = department
        self.title = title

    def details(self):
        print(f"Name: {self.name}, Department: {self.department}, Title: {self.title}")

Nathaniel = ITSupport("Nathaniel", "IT Support", "Developer")

Nathaniel.details()  # Output: Name: Nathaniel, Department: IT Support, Title: Developer
'''
"""
class Users:
    '''
    def __init__(self, name, email, status,role):
        self.name = name
        self.email = email
        self.status = status
        self.role = role
    '''
    
    def create(self):
        self.name = input("Enter new user name: ")
        self.email = input("Enter new user email: ") 
        self.status = input("Enter new user status: ").lower()
        self.role = input("Enter new user role: ")

    def validation(self):
        if self.status != "active":
            print(f"HEllo {self.name}, your account is {self.status}. Please onboard to activate")
        else:
            print(f"Welcome {self.name}, your account is {self.status}. You have {self.role} access")

user = Users()
user.create()
user.validation()
"""
"""
#Object State

class Student:
    def __Init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

john = Student("John", 20, "A")

sarah = Student("Sarah", 22, "B")

"""
"""
class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

account = BankAccount(1000, "Kuda")  # Creating an object of the BankAccount class with an initial balance of 1000 

account.balance = 300
"""
class BankAccount:
    def deposit(self, amount, balance):
        self.amount = amount
        self.balance = balance
        self.balance += amount
        # account.deposit(500)  # Depositing 500 into the account

account = BankAccount()

account.deposit(1000, 500.09)  # Depositing 1000 into the account with an initial balance of 500)

print(account.balance)
"""

class Student:
    school = "Global AIAcademy"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

print(john.school)








