# this app calculate how many can of color is require for paint a wall
import math
height = int(input("Height of wall in meters: "))
width = int(input("Width of wall in meters: "))

# coverage of each can
coverage = 5

def can_cal(height, width, coverage):
    color = (height * width)/coverage
    print(f"amount of color is: {color}")
    print(f"amount of can is: {math.ceil(color)}")

can_cal(height, width, coverage)


# number = 20 
# divisors = [2, 4, 5, 10]
# print(" ".join(map(str, divisors)))

# # print(f"{number} is not prime. It's divisible by {divisors_str}")

