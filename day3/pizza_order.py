# this app is for calculate pizza order!
# prepareing for being AI engineer in US! very soon!

print("Welcome to Python pizza Deliveris!")
bill = 0
size = input("What size of pizza you want? S , M or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
add_cheese = input("Do you want cheese? Y or N : ") 

if size == "S":
 bill = 15
 if add_pepperoni == "Y":
    bill = bill + 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
     bill = bill + 3
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
     bill = bill + 3

if add_cheese == "Y":
    bill = bill + 1 

print(f"Your final bill is: ${bill}")
