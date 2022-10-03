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

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
result = ""


def encrypt(plain_text, shift_amount):
    result = ""
    for i in range(0, len(plain_text)):
        for k in range(0, len(alphabet)):
            if len(alphabet) - k > shift_amount:
                if plain_text[i] == alphabet[k]:
                    result += alphabet[k + shift_amount]
                if plain_text[i] not in alphabet:
                    break
            else:
                break

    print(f"The encoded text is {result}")


encrypt(text, shift)
