alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def dec_or_enc(question):
    while True:
        direction = input(f"{question}:\n").lower()
        if direction in ( "encode" , "decode"):
            return direction
        else:
            print("You must answer encode or decode ")
            
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount 
        if cipher_direction == "encode":
            new_position = new_position % 26
        end_text += alphabet[new_position]
    else:
        end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

### for todo1 ###
from art import caesar_logo
print(caesar_logo[0])

### for todo4 ###
stop_app = False
resum_app = "yes"
while stop_app == False  :
    direction = dec_or_enc("Type 'encode' to encrypt, type 'decode' to decrypt")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if resum_app in ( "yes" , "y"):
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        resum_app = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
        if resum_app in ("no", "n"):
            stop_app = True
        