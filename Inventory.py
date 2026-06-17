Inventory =[]

def security():
    name = input("Enter username :")
    pass_word = input("Enter your password")
    
    if name.lower =="Boss" and pass_word =="Pass123":
        print(f"Welcome ",{name})
        return
    elif name.lower =="Employee" and pass_word=="Pass123" :
         print(f"Welcome ",{name})
         return
    else:
        print("Unautorized")
        exit
    return

def opts(add, remove, veiw):
    optss=["Add","Remove","Veiw"]
    
    print("Welcome to DL hardware Inventory" +'\n') 
    for opt in optss:
        print(opt)
        return
    
    choice = input("Enter choice:")
    
    if choice == "Add":
        Inventory.append("Enter item to be added :")
    elif choice == "Remove
              