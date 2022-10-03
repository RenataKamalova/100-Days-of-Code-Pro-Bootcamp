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


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
            shift_amount *= -1
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
            shift_amount *= -1

        elif cipher_direction == "encode":
            new_position = position + shift_amount
            if new_position <= len(alphabet) - 1:
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                new_letter = alphabet[new_position - len(alphabet)]
                end_text += new_letter

        # end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
