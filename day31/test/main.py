from googletrans import Translator

translator = Translator()

# def generate_sentence(word):
#     prompt = f"Write a simple English example sentence using the word '{word}'."
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content.strip()
#
# words = open("5000_words.txt").read().splitlines()

# data = []
#
# for w in words:
#     sentence = generate_sentence(w)
#     translation = translator.translate(sentence, dest="fa").text
#     data.append([w, sentence, translation])
#
# df = pd.DataFrame(data, columns=["word", "english_sentence", "persian"])
# df.to_csv("5000_words_output.csv", index=False)

result = translator.translate('안녕하세요.')
print(result)
