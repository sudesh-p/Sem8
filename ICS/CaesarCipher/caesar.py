#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def decrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result
#check the above function
text = input("Enter Plain Text: ")
s = int(input("Enter the Shift Value: "))
print()
print ("Entered Plain Text : " + text)
print ("Entered Shift : " + str(s))
print ("Encrypted Text : " + encrypt(text,s))
print("Decrypted Text: " + decrypt(encrypt(text,s),s))
