# A simple text encryption exercise using the Caesar Cipher technique.
# The Caesar Cipher for `shift = 3` cyclically shifts every letter of the word by 3 positions:
# a -> d, b -> e, c -> f, ..., x -> a, y -> b, z -> c

# Implement the encryption logic by shifting each alphabet character

def encrypt_text(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted+=chr((ord(char)-65+shift)%26+65)
            else:
                encrypted+=chr((ord(char)-97+shift)%26+97)
        else:
            encrypted+=char
    return encrypted


# Example text to encrypt (paste any line below as original_text)
original_text = "Hello, Python!"

encrypted_text = encrypt_text(original_text, 3)
print(encrypted_text)  # For "Hello, Python!" expected: 'Khoor, Sbwkrq!'
