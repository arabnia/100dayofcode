# this kososher code is for calculate Love! va bokon bokon marhale ba'd
mashouq = input("Plz input bokon name: ")
mashouqeh = input ("Plz input mafool name: ")

concated_name = (mashouq + mashouqeh).lower()
t = concated_name.count("t")
r = concated_name.count("r")
u = concated_name.count("u")
e = concated_name.count("e")

total_true = t + r + u + e

l = concated_name.count("l")
o = concated_name.count("o")
v = concated_name.count("v")
e = concated_name.count("e")

total_love = l + v + o + e
total = int(str(total_love) + str(total_true))
print(total)
if total < 10 or total > 90:
 print(f"sharte aval, and your score is {total}")