# this app is for cacluate summation of even number in inputed range!
user_in = input("plz input expected range: ").split()
sum_even = 0
for i in range(int(user_in[0]), int(user_in[1])+1):
    if i % 2 == 0:
        sum_even += i

print(f"the sum of even number is: {sum_even}")