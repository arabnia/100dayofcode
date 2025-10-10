# This app is for calculate leap year!
year = int(input("plz input your year!: "))

if year % 100 == 0:
 if year % 400 == 0:
    print ("this is Leap year")
 else:
    print( " this is not Leap year")
elif year % 4 == 0:
 print("this is Leap year")
else:
    print("this is not Leap year")