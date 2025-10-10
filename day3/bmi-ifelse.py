# This app is for calculate BIM and show result
height = float(input("plz input your height: "))
weight = float(input("plz input your weight: "))
bmi = weight / height ** 2 
print(bmi)
if bmi <= 18.5:
    print("UnderWeight")
elif bmi > 18.5 and bmi < 25:
    print ("Normal weight")
elif bmi > 25 and bmi < 30:
    print("OverWeight")
elif bmi < 30 and bmi > 35:
    print("Obese")
else: 
    print("clinically obese")