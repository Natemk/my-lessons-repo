contact_book ={
    "Name" : input("Name : "),
    "Phone" : input("Phone Number : "),
    "Email" : input("Email : "),
    "City" : input("City : ")
}

for key, value in contact_book.items():
    print(f"{key}: {value}")

update = input("Enter feild to be name of updated : ")

