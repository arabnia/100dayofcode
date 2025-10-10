# # who's bill go in pachash?
import random
name_of = input ("Plz input people name here: ")
sp_name = name_of.split(",")
random_per = random.randint(0,(len(sp_name)-1))
print(f"{sp_name[random_per]} will pay bill today!")
