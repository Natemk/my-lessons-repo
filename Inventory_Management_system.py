inventory = []

def menu():
    print("\n----------- INVENTORY -----------")
    print("Options:")
    print("  add    - Add an item")
    print("  remove - Remove an item")
    print("  view   - View all items")
    print("  exit   - Exit the program")
    return


def options():
    while True:
        menu()
        choice = input("Enter your choice: ").lower()
        
        if choice == "add":
            item = input("Enter name the item to be added: ")
            inventory.append(item)
            print( item, "has been added to inventory")
            
        elif choice == "remove":
            item = input("Enter name the item to be removed: ")
            if item in inventory:
                inventory.remove(item)
                print( item, "has been removed from inventory")
            else:
                print( item, "is not in inventory")
                
        elif choice == "view":
            if inventory:
                print("Current inventory:")
                for item in inventory:
                    print("-", item)
            else:
                print("Inventory is empty.")
        elif choice == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
menu_inventory = menu()         
main = options()
