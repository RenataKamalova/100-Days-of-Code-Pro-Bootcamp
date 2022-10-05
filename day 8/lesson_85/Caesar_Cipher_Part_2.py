from operator import index
from art import logo
from art import english_alphabet


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in english_alphabet:

            position = english_alphabet.index(char)
            if cipher_direction == "decode":
                shift_amount *= -1
                new_position = position + shift_amount
                new_letter = english_alphabet[new_position]
                end_text += new_letter
                shift_amount *= -1
            else:
                new_position = (position + shift_amount) % len(english_alphabet)
                new_letter = english_alphabet[new_position]
                end_text += new_letter
        else:
            end_text += char

    print(f"The {cipher_direction}d text is {end_text}")


continue_flag = True

while continue_flag == True:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % len(english_alphabet)
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    answer_to_question = input("Do you want to encode or decode something again? Y/N ")
    if answer_to_question == "Y":
        continue_flag = True
    else:
        continue_flag = False
        print("Goodbye!")
