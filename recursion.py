
"""
def factorial(num):
    
    if num ==1:
        return 1
    else:
        return num * factorial(num -1)
    
print(factorial(5))
"""

def walk(steps):
    
    if steps <= 0:
        return
    else:
        # recursive call first to print steps in ascending order
        walk(steps - 1)
    print(f"Step {steps}")

walk(10)