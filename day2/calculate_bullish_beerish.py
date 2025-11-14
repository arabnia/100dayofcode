init_value = int(input("Please enter your initial value: "))
change_percentage = input("Please enter your change percentage: ")
change_percentage = change_percentage.replace('%', '')
change_percentage = int(change_percentage)
changed_value = init_value * change_percentage / 100
final_value = changed_value + init_value
# print(final_value)
# calculate how much it must change to refer to first value
new_percentage = init_value / final_value
# print(new_percentage)
new_percentage = 1 - new_percentage
if new_percentage > 0:
    print(f"you must change {100 * new_percentage}% for retain original amount of value")
elif new_percentage < 0:
    print(f"you must change {100 * new_percentage}% for retain original amount of value")
else:
    print("you are on first step!")

