from operator import index


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(plain_text, shift_amount, direction):
    ciphertext = ""
    deciphered_text = ""

    for letter in plain_text:
        position = alphabet.index(letter)

        if direction == "encode":
            new_position = position + shift_amount
            if new_position <= len(alphabet) - 1:
                new_letter = alphabet[new_position]
                ciphertext += new_letter
            else:
                new_letter = alphabet[new_position - len(alphabet)]
                ciphertext += new_letter
        print(f"The encoded text is {ciphered_text}")
        
        else:            
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            deciphered_text += new_letter

        print(f"The decoded text is {deciphered_text}")

caesar()