# check input number is prime or not
number = int(input("your number: "))
def isprime(number):
    number_isprime = False
    divison = []
    for i in range(2, number):
        if number % i == 0:
            divison.append(i)
            number_isprime = True
    print(divison)
    if number_isprime == True:
        divisors_str = ", ".join(map(str, divison))
        print(f"{number} is not prime, It's divisble by {divisors_str} ")
    else:
        print(f"{number} is prime!")

isprime(number)