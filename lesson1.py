while True:
    name = input("Enter customer name: ")
    item_1 = float(input("Enter price of item 1: "))
    item_2 = float(input("Enter price of item 2: "))
    item_3 = float(input("Enter price of item 3: "))

    sub_total = item_1 + item_2 + item_3
    tax = sub_total * 0.13
    total = sub_total + tax

    print("------RECEPT------" + '\n'
          +"Welcome to Munya's Grocery Store" + '\n'
          + '\n' 
          + "Customer :" + (name) + '\n'
          + "Sub Total: $" + str(sub_total) + '\n'
          + "Tax: $" + str(tax) + '\n'
          + "Total: $" + str(total) + '\n'
          + "------------------" + '\n'
          + '\n'     
          )

    next_process=input("Do you want to process another customer? (yes/no): ")

    if next_process.lower() != "yes":
        print("Done.")
        break


