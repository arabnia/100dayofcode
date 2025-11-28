import pandas as pd
import random
data = pd.read_csv("translated_most_freq_word.csv")
def random_word():
    return random.choice(data["word"])

print(random_word())