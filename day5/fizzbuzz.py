# this app run fizzBuzz game in expected range!
user_in = input("plz input expected range: ").split()
for i in range(int(user_in[0]), int(user_in[1])+1):
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print(i) 

pri("slfjslkdfj")