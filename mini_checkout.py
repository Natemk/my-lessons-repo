def get_name():
    name = input ("Enter customer name:")
    return name

def get_item_price():
    price = float(input("Enter price of item :"))
    
    if price == 0:
        return 0
    
    # 2. Recursive Case: Add current price to the NEXT price captured
    else:
        return price + get_item_price()
     

def calculate_tax(subtotal):
    tax = subtotal * 0.3
    return tax

def display_receipt(name, subtotal, tax, total):
    print("\-----------RECEIPT------------")
    print("Customer Name:", name)
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Total:", total)

#Main Program
name = get_name()
subtotal = get_item_price()
tax = calculate_tax(subtotal)
total = subtotal + tax
display_receipt(name, subtotal, tax, total)