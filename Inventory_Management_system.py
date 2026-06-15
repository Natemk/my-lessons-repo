inventory =[]

def add():
    add_new = inventory.append(input("Enter product: "))
    
    if add_new =="":
        return
    
    return

def remove():
    remove_item =inventory.pop("Enter the name of the item to be removed :")
    
    if remove_item =="":
        return
    
    return

def quantity():
    quant = len(inventory)
    
    if quant =="":
        return
    
    return

def veiw_all():
   for inventor in  inventory:
       print("\nCurrent inventory : ",inventory)
       return
   return


