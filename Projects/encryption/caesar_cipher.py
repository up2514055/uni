def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            result += chr(shifted)
        else:
            result += char
    return result
    
def decrypt(message, shift):
    return encrypt(message, -shift)
message = input("Enter a message: ")
shift = int(input("Enter a shift value: "))

encrypted= encrypt(message, shift)
print(f"encrypted: {encrypted}")

with open("encrypted.txt", "a") as f:
    f.write("=" * 30 + "\n")
    f.write(f"Initial Input: {message}\n")
    f.write(f"Shift Value:  {shift}\n")
    f.write(f"Encrypted Message: {encrypted}\n")
    f.write("=" * 30 + "\n\n")

print("Message has been saved to the specific txt file listed above")


userinput = str(input("Would you like to see the decrypted message: "))

if userinput.lower() == "yes":
    print(f"decrypted: {decrypt(encrypted, shift)}")
else:
    print("Okay, goodbye")