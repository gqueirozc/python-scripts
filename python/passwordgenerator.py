import secrets
import string
import time
import pyperclip

#ascii = letters | digits = number | punctuation = special
alphabet = string.ascii_letters + string.digits + string.punctuation

password_length = int(input("Select the size of the password: "))
specialCharacterAmount = int(input("Select minimum amount of special characters: "))
numericDigitsAmount = int(input("Select minimum amount of numeric characters: "))

seconds = int(input("Maximum execution time in seconds: "))
start_time = time.time()
print("Maximum time limit: " + str(seconds) + " seconds")

UP = "\x1B[3A"
CLR = "\x1B[0K"
print("\n\n")
def executionTimeElapsed():
    current_time = time.time()
    elapsed_time = current_time - start_time
    return elapsed_time

def getCharacter():
    character = secrets.choice(alphabet)
    print(f"{UP}Elapsed Time: {str(executionTimeElapsed())}{CLR}\nGenerating: {password + character}{CLR}\n")
    return character

while True:
    if executionTimeElapsed() > seconds:
        print("Failed to generate password with specified parameters")
        break
    
    password = ''
    for i in range(password_length):
        password  += ''.join(getCharacter())

    if (sum(c in string.punctuation for c in password) >= specialCharacterAmount and sum(c in string.digits for c in password) >= numericDigitsAmount):
        break

pyperclip.copy(password)
print("\n************* Finished Generating ****************")
print("**************** Specifications ******************")
print("Password Lenght: " + str(password_length))
print("Special Character Minimum Amount: " + str(specialCharacterAmount))
print("Numeric Character Minimum Amount: " + str(numericDigitsAmount))
print("\nPassword: " + password)
print("Text copied to clipboard.")
print("\n***************************************************")
input("\nPress enter to terminate the process...\n")