fruits = ["apple", "banana", "cherry"]
def make_pi(index):
    try:
        selected_fruit = fruits[index]
    except IndexError:
        selected_fruit = "fruit"
    print(f"{selected_fruit} pie")
make_pi(4)