import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
print(art.logo)
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def caesar(direction, original_text, shift_amount):
    if direction == ("encode"):
        encrypt(original_text, shift_amount)
    elif direction == ("decode"):
        decrypt(original_text, shift_amount)
    else:
        print("You must type 'encode' or 'decode'!")


while True:
    while True:
        direction = input("Type 'encode' to encrypt. Type 'decode' to decrypt.").lower()
        if direction == 'encode' or direction == 'decode' :
            break
        else:
            print("You must type either 'encode' or 'decode'")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)

    while True:
        retry = input("Would you like to try again? type 'yes' for yes and 'no' for no").lower()
        if retry == ('yes'):
            break
        elif retry == ('no'):
            print("Have a Lovely Afternoon!")
            exit()
        else:
            print("You must type either 'yes' or 'no'")

