def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, d, n):
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

e = int(input("Enter the public key exponent (e): "))
n = int(input("Enter the modulus (n): "))
d = int(input("Enter the private key exponent (d): "))

message = input("Enter the message to encrypt: ")

ciphertext = encrypt(message, e, n)
print("Encrypted message:", ciphertext)

decrypted_message = decrypt(ciphertext, d, n)
print("Decrypted message:", decrypted_message)