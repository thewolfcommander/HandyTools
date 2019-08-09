"""
Reverse Cipher
"""

def reverse_cipher():
    message = input("Enter the text ... ")
    encrypted_message = ""
    for i in message[::-1]:
        encrypted_message += i
    
    print("The encrypted message is ... \n", encrypted_message)

reverse_cipher()