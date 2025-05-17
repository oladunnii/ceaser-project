alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, direction):
    if direction == "encode":
        cipher_text = ""
        for letter in original_text:
            if letter in alphabet:
                shifted_position = (alphabet.index(letter) + shift_amount) % 26
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text += letter

        print(f"Here is the encoded result: {cipher_text}")
    elif direction == "decode":
        decipher_text = ""
        for letter in original_text:
            if letter in alphabet:
                shifted_position = (alphabet.index(letter) - shift_amount) % 26
                decipher_text += alphabet[shifted_position]
            else:
                decipher_text += letter
        print(f"Here is the decoded result: {decipher_text}")
    else:
        print("Wrong input try again with encode or decode.")

caesar(original_text=text,shift_amount=shift,direction=direction)
