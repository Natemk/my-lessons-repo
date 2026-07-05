"""
try:
    number = int(input())
    
except ValueError:
    print("Please enter a valid integer.")
"""
'''
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    
    divide = num1 / num2
    
    
 
    print(f"Division: {divide}")
   
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
except ValueError:
    print("Error: Please enter valid integers.")
    
else:
    print("Division  successful.")
    '''
'''' 
try:
    number = int(input())

except:

    print("Error")

finally:
    
    print("Finished")


salary = int(input("Enter your salary: "))
 
try:
    if salary < 0:
        raise ValueError("Salary cannot be less than zero.")
    
except ValueError as e:
    print(f"Error: {e}")

'''


def load_users():
    """Reads the text file and returns a dictionary of users."""
    users = {}
    
    try:
        with open("bank_data.txt", "r") as f:
            for line in f:
                # Splitting the line: PIN,Name,Balance
                pin, name, balance = line.strip().split(",")
                users[pin] = {"name": name, "balance": float(balance)}
    except FileNotFoundError:
        # If the file doesn't exist, we just return an empty dict
        return {}
    return users

def save_users(users):
    """Writes the current dictionary back to the text file."""
    with open("bank_data.txt", "w") as f:
        
        for pin, info in users.items():
            f.write(f"{pin},{info['name']},{info['balance']}\n")

def atm():
    users = load_users()
    
    pin = input("Enter 4-digit PIN: ")
    if not (pin.isdigit() and len(pin) == 4):
        print("Invalid PIN format.")
        return
    elif pin not in users:
        print("New PIN. You will be registered." + '\n')
    else:
        print("PIN accepted.")

    # Check if user exists, if not, register
    if pin not in users and pin.isdigit() and len(pin) == 4:
        name = input("New account. Enter your full name: ")
        
        if name.isdigit():
            print("Invalid name. Registration failed.")
            return
        
        users[pin] = {"name": name, "balance": 0.0}
        save_users(users)
        print("Account created.")

    current_user = users[pin]

    while True:
        print(f"\n--- {current_user['name']}'s Account ---")
        print("1. Deposit | 2. Withdraw | 3. Balance | 4. Exit")
        choice = input("Select: ")

        try:
            if choice == '1':
                amount = float(input("Deposit amount: "))
                if amount <= 0: 
                    raise ValueError("Must be positive.")
                current_user['balance'] += amount
                save_users(users)
                print("Success.")

            elif choice == '2':
                try: 
                    amount = float(input("Withdrawal amount: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
                if amount <= 0: 
                    raise ValueError("Must be positive.")
                if amount > current_user['balance']: 
                    raise ValueError("Insufficient funds.")
                
                
                
                current_user['balance'] -= amount
                save_users(users)
                print("Success.")

            elif choice == '3':
                print(f"Balance: {current_user['balance']}")

            elif choice == '4':
                break
            else:
                print("Invalid option.")

        except ValueError as e:
            print(f"Input Error: {e}")

if __name__ == "__main__":
    atm()


'''
        An exception is an error that occurs while a program is running
        
        They crash the program if not handled properly
        
        Try acts as a safety net to catch exceptions and handle them gracefully
        
        Except acts as a recovery plan to handle the exception and prevent the program from crashing
        
        The difference between ExceptValueError and except
        except ValueError is specific; it only catches errors where the wrong data type is provided.
        
        except is a general catch-all; it will catch any type of exception, which can make debugging harder.
        
        The finally block runs no matter what. It is used to clean up resources, like ensuring a file is closed,
        even if the program crashed halfway through
        
        This happens if you try to perform math where a number is divided by zero (e.g., 10 / 0).
        
        This happens when you try to use open() on a filename that does not exist in the folder.
        
        You use raise to manually trigger an error. For example, even if the user types a valid number,
        you might want to "force" an error if they try to withdraw money they don't have, because that violates your banking rules.
'''