# number_list='1 2 3 4 5 6 7 8 9'
# number_list = number_list.split(" ")
# number_list = join(map(str, number_list))
# print(number_list)
# class Student:
#     school = "OpenAI Academy"  # class variable shared by all objects
#
#     def __init__(self, name):
#         self.name = name       # instance variable
#
# s = Student("Ali")
# print(f"{s.school}, {s.name}")


# im writing inherit class in python code
class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    def speak(self):
        print("Dog")


p1 = Dog()
p1.speak()