import pandas as pd
user_input = input("Enter a word: ")
data = pd.read_csv("nato_phonetic_alphabet.csv")
# list_item = {row.letter:row.code for (index, row) in data.iterrows()}

data_list = [data[data["letter"] == key.upper()].code.iloc[0] for key in user_input]
print(data_list)
