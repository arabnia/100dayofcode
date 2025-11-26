import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
# list_item = {row.letter:row.code for (index, row) in data.iterrows()}
while True:
    user_input = input("Enter a word: ")
    try:
        data_list = [data[data["letter"] == key.upper()].code.iloc[0] for key in user_input]
        break
    except IndexError:
        print("Invalid input, retry...")

print(data_list)