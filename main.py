from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            cipher_text += alphabet[new_position]
        else:
            chiper_text += char
    print(f"The {cipher_direction}d text is {cipher_text}")
    
    choice = input("Type 'yes' to restart the program\n")
    if choice == "yes":
        start()
    else:
        print("Goodbye!")

def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if shift > 26:
        shift %= 26
    caesar(text, shift, direction)

print(f"{logo}")
start()