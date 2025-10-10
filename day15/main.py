from variable import resources, MENU
MONEY = 0
def inputs():
    while True:
        ans = input(f"What would you like? (press h for help or menu to show item: ").lower()
        if ans in '':
            print("null")
        elif ans in "h":
            print('''
 for show this menu: h
 for show available material: report
 Turn off the Coffee Machine by entering: off
 To get coffe in menu Type espresso/latte/cappuccino or so
 For print menu type: menu
            ''')
        elif ans in ("menu"):
            for k in MENU:
                print(f"{k}, for: {MENU[k]['cost']}$")
            print(" ")
        elif ans in ("off", "report", MENU):
            return ans
        elif ans in MENU:
            return ans
        else:
            print("You must answer in available options only!")

            
# Print report
def rep_resource():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"Money: {MONEY}$")

# Check resources sufficient
def res_suff(drink):
    is_enough = True
    for ingredients in MENU[drink]["ingredients"]:
        if resources[ingredients] <= MENU[drink]["ingredients"][ingredients]:
            print(f"Sorry there is not enough {ingredients}")
            is_enough = False
        return is_enough

def bank(drink):
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    global MONEY
    drink_price = MENU[drink]['cost']
    print(f"The price of {drink} is {drink_price}$\nplease insert coins!")
    user_money = round(int(input('how many quarters?')) * 0.25 + int(input('how many dimes?')) * 0.10 + int(input('how many nickles?')) * 0.05 + int(input('how many pennies?')) * 0.01, 2)
    if drink_price <= user_money:
        print(f"Here is {user_money - drink_price}$ in change.")
        MONEY += drink_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def coffe_machine():
    while True:
        user_input = inputs()
        if user_input == 'off':
            break
        elif user_input == 'report':
            rep_resource()
        elif user_input in MENU:
            if res_suff(user_input):
                if bank(user_input):
                    print(f"Here is your {user_input} ☕. Enjoy!")

if __name__ == "__main__":
    coffe_machine()