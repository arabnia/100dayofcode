# this is code that generate csv file with 5000 most frequent English word
# and translate it into Persian
# this code also use only relevant column! Are you ready to see it? lets Go with me!

import pandas as pd
from googletrans import Translator
translator = Translator()

# data = pd.read_csv("wordFrequency/lemmas_table.csv") # full 5000 words
data = pd.read_csv("wordFrequency/sample_word.csv")
columns = ["id", "word", "translation"]
pd.DataFrame(columns=columns).to_csv("translated_most_freq_word.csv", index=False)

# for chunks in range(0, len(data) - 1, 5): # disable unsuccessful memory management for large file
rows = []
for i in range(0, len(data) - 1):
    rows.append([i, data["lemma"].iloc[i], translator.translate(data["lemma"].iloc[i], dest="fa").text])
    # rows.append([i, data["lemma"].iloc[i], data["lemma"].iloc[i]]) # this is for test to bypass googletrans request
df = pd.DataFrame(rows, columns=columns)
df.to_csv("translated_most_freq_word.csv", mode="a", index=False, header=False)

