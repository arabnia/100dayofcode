# Do you love/like me Zeinab?

def add(*numbers):
    return sum(numbers)
# print(add(1, 2, 3))

def calculate(n , **someone):
    print(type(someone))
    print(n)
    print(someone)

# calculate(5 , type1="value1", type2="value2")

def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)

class Car:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.price = kwargs.get("price")
car1 = Car(name="exocar"   )

print(car1.name)
print(car1.price)



