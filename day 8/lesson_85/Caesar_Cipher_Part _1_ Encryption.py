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
# print(len(alphabet), alphabet[21])


def encrypt(plain_text, shift_amount):
    ciphertext = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position <= len(alphabet) - 1:
            new_letter = alphabet[new_position]
            ciphertext += new_letter
        else:
            new_letter = alphabet[new_position - len(alphabet)]
            ciphertext += new_letter

    print(f"The encoded text is {ciphertext}")


def decrypt(plain_text, shift_amount):
    deciphered_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        deciphered_text += new_letter
        # if new_position > 0:
        #     new_letter = alphabet[new_position]
        #     deciphered_text += new_letter
        # else:
        #     new_letter = alphabet[new_position - 1]
        #     deciphered_text += new_letter

    print(f"The decoded text is {deciphered_text}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
