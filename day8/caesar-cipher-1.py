alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def dec_or_enc(question):
    while True:
        direction = input(f"{question}:\n").lower()
        if direction in ( "encode" , "decode"):
            return direction
        else:
            print("You must answer encode or decode ")

direction = dec_or_enc("Type 'encode' to encrypt, type 'decode' to decrypt")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# direction = "encode"
# text = "hello"
# shift = 5

def caesar(text, shift_amount, direction):
    # print(f"All the variable is {text}, {shift_amount}, {direction}")
    final_text = []
    if direction == "decode":
        shift_amount *= -1
    for i in text:
        char_num = (alphabet.index(i) + shift_amount)
        if char_num > 26:
            char_num = char_num % 26
        final_text.append(alphabet[char_num])
    print(f"Here's the {direction} result: {''.join(final_text)}")
 
caesar(text, shift, direction)