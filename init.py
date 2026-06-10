'''
x = "45"
y = int(x) + 5
z = float(y) * 2
print(f"y: {y}, z: {z}")


name=float(input("Enter number: "))
print(name)


username = "Munya"
score = 1500
print(f"Player {username} finished with a total score of {score}")



name = input("Enter name : ")
birth_year = int(input("Enter birth year : "))
this_year = 2026
age =  (this_year - birth_year)
print(f"Welcome back,{name}! You are turning {age} years old.")

'''
import datetime
name = input("Enter customer name : ")
date = datetime

roofing = input("Enter Roof type(0.30, 0.40, 0.27) :")
quant_1 = input("Enter quantity: ")

cement = input("Enter cement type (SupSet 42.5R):")
quant_2 = input("Enter quantity: ")

windowpan = input("Enter item (3 pan, 6 pan, 8 pan, 9 pan, 12 pan) :")
quant_3 = input("Enter quantity: ")

polypipe = input("Enter item (15mm, 20mm, 25mm, 32mm, 40mm) :")
quant_4 = input("Enter quantity: ")

if roofing=="0.30":
       r_price=13
elif roofing=="0.27":
      r_price = 7
elif roofing=="0.40":
      r_price = 18
elif roofing=="":
      r_price =  0
else:
      price = 0
      
s_price=13.5

if windowpan=="3 pan":
      w_price=15
elif windowpan=="6 pan":
      w_price=18
elif windowpan=="8 pan":
      w_price=30
elif windowpan=="9 pan":
      w_price=35
elif windowpan=="12 pan":
      w_price=40
elif windowpan=="":
      w_price=0
else:
      w_price = 0
      


      
if polypipe=="15mm":
      p_price=15
elif polypipe=="20mm":
      p_price=20
elif polypipe=="25mm":
      p_price=25
elif polypipe=="32mm":
      p_price=35
elif polypipe=="40mm":
      p_price=45
elif polypipe=="":
      p_price=0
else:
      p_price = 0
      
      
      
      

try:
      quant_1 = int(quant_1)
except ValueError:
      quant_1 = 0

try:
      quant_2 = int(quant_2)
except ValueError:
      quant_2 = 0

try:
      quant_3 = int(quant_3)
except ValueError:
      quant_3 = 0

try:
      quant_4 = int(quant_4)
except ValueError:
      quant_4 = 0

t1 = float(r_price) * quant_1
t2 = float(s_price) * quant_2
t3 = float(w_price) * quant_3
t4 = float(p_price) * quant_4

sub_total = t1 + t2 + t3 + t4
tax = sub_total * 0.12
total = sub_total + tax

receipt = (
      f"Welcome to DL Hardware\n"
      f"--------RECEIPT--------\n"
      f"Customer Name : {name}\n"
      f"Products bought:\n"
      f"  {roofing}       {quant_1} x {r_price} = {t1:.2f}\n"
      f"  {cement}       {quant_2} x {s_price} = {t2:.2f}\n"
      f"  {windowpan}       {quant_3} x {w_price} = {t3:.2f}\n"
      f"  {polypipe}       {quant_4} x {p_price} = {t4:.2f}\n"
      f"---------------------------------\n"
      f"Subtotal:      {sub_total:.2f}\n"
      f"Tax     :      {tax:.2f}\n"
      f"Total   :      {total:.2f}\n\n"
      f"---------------------------------\n"
      f"Thank you for buying from DL Hardware"
)

print(receipt)