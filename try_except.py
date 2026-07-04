"""
try:
    age = int(input("Enter age:"))
    

except:
    print("Wakupenga here? Please enter a valid number.")

"""
"""
try:
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))

    print(num1/num2)

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division successful")

"""
"""
try:
     file = open("teams.txt")

except FileNotFoundError:
    print("File missing")

finally:
    print("Program Complete")

"""
'''
try:
    number = int(input())

except:

    print("Error")

finally:

    print("Finished")
'''
try:
    age =int(input())

except ValueError as error:
    print(error)

