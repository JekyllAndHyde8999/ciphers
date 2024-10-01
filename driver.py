import random
import string

from ciphers import Affine, Caesar, Hill, Playfair, RailFence, Vatsyayana, Vigenere

all_chars = string.ascii_letters + string.digits
TOTAL_LENGTH = 100


def message_len(message):
    return sum([char.isalnum() for char in message])


def print_message(text, cipher):
    print("Encoded message:", encoded := cipher.encode(text))
    print("Decoded message:", cipher.decode(encoded))


print(f"\n{' Sample Text ':#^{TOTAL_LENGTH}}\n")
message = "Ciphers are amazing. They can encode any piece of text."
print(message)

print(f"\n{' Monoalphabetic Ciphers ':#^{TOTAL_LENGTH}}")
print(f"{' Caesar ':#^{TOTAL_LENGTH}}\n")
caesar = Caesar(5)
print_message(message, caesar)


def create_pairs(s):
    # Convert the string to a list of characters
    characters = list(s)
    pairs = []

    # Continue until all characters are paired
    while characters:
        # Randomly select two characters
        pair = random.sample(characters, 2)
        pairs.append(tuple(pair))
        # Remove the selected characters from the list
        characters.remove(pair[0])
        characters.remove(pair[1])

    return pairs


print(f"\n{' Vatsyayana ':#^{TOTAL_LENGTH}}\n")
pairs = create_pairs(all_chars)
vatsyayana = Vatsyayana(pairs)
print_message(message, vatsyayana)

print(f"\n{' Affine ':#^{TOTAL_LENGTH}}\n")
affine = Affine(9, 3)
print_message(message, affine)

print(f"\n{' RailFence ':#^{TOTAL_LENGTH}}\n")
railfence = RailFence(2)
print_message(message, railfence)

print(f"\n{' Polyalphabetic Ciphers ':#^{TOTAL_LENGTH}}")
print(f"{' Playfair ':#^{TOTAL_LENGTH}}\n")
passphrase = "221B"
playfair = Playfair(passphrase)
print_message(message, playfair)

print(f"\n{' Hill ':#^{TOTAL_LENGTH}}\n")
key = "DFCH"
hill = Hill(key)
print_message(message, hill)

print(f"\n{' Vigenere ':#^{TOTAL_LENGTH}}\n")
key = "ciphers"
vigenere = Vigenere(key)
print_message(message, vigenere)
