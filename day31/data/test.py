import pandas as pd
import random
data = pd.read_csv("translated_most_freq_word.csv")
def random_word():
    return data.sample(n=1, random_state=random.seed(1))

output = random_word()
print(output)
data = data.drop(index=output.index)
data.to_csv("translated_most_freq_word_deleted.csv")
