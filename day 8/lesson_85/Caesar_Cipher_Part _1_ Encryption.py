from operator import index
from tkinter.messagebox import QUESTION
from art import logo
from art import english_alphabet

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = english_alphabet.index(letter)
        if cipher_direction == "decode":
            shift_amount *= -1
            new_position = position + shift_amount
            new_letter = english_alphabet[new_position]
            end_text += new_letter
            shift_amount *= -1

        elif cipher_direction == "encode":
            new_position = position + shift_amount
            if new_position <= len(english_alphabet) - 1:
                new_letter = english_alphabet[new_position]
                end_text += new_letter
            else:
                new_letter = english_alphabet[new_position - len(english_alphabet)]
                end_text += new_letter
        print(f"The {cipher_direction}d text is {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
