# this app is for generateing strong pass!
import random
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sp_char = ["!", "#", "$", "%", "&", "*", "(", ")", "+"]
nu_char = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Welcome to the PyPassword Generator!")

###########

nr_letters = int(input("How many letter would you like in your password!: "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

###########
cahr_list = ["char", "sp_char", "nr_numbers"]
output_string = []
# simple mode 
for i in range(nr_letters - nr_numbers - nr_symbols):
    output_string.append(random.choice(char))
for i in range(nr_symbols):
    output_string.append(random.choice(sp_char))
for i in range(nr_numbers):
    output_string.append(random.choice(nu_char))

# print(output_string)
random.shuffle(output_string)
# print(output_string)
output_password = ""
for i in output_string:  
     output_password += i

print(output_password)