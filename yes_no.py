def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()  # Get user input, strip whitespace, and convert to lowercase
        if user_input in ['yes', 'no']:  # Check if input is either 'yes' or 'no'
            return user_input
        else:
            print("Please enter 'yes' or 'no'.")

# Example usage:
response = get_yes_no_input("Do you want to proceed? (yes/no): ")
if response == 'yes':
    print("Proceeding...")
else:
    print("Exiting...")


def calculate(player_deal):
    player_score = 0
    if sum(player_deal) ==21 and len(player_deal) == 2 :
        return 0
    elif sum(player_deal) > 21 and 11 in player_deal:
        player_deal.remove(11)
        player_deal.append(1)
    return sum(player_deal)
deaaaal = [11,11]
print(calculate(deaaaal))

import bcrypt

# Sample password
password = "1qaz@WSX"

# Hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Print the hashed password
print(hashed_password)


