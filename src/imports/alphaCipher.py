import string
import random

def codeGenerator(size=10, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))
    
def jimActivity():
    code=codeGenerator()
    answer=alphaCipher(code)
    print("You look at the computer and see that a password is required. There is a button that says 'Generate Random Encrypted Password'.")
    print("You press the button and the code\n\n%s\n\nappears on the screen. A dialog box says 'Please enter the decrypted password.'" %(code))
    print("Jim seems to have forgotten about the cipher key, which is taped to his monitor. The note reads:\n")
    print("abcdefghijklmnopqrstuvwxyz")
    print("zyxwvutsrqponmlkjihgfedcba\n")
    while True:
        com=input('Please enter decrypted password: ').lower().strip()
        words=com.split()
        numWords=len(words)
        if numWords != 1 or 'help' in com:
            print("The computer seems to be waiting for the password...")
        else:
            if com==answer:
                print()
                print("............")
                print("............")
                print("............")
                print("Password Correct!\n")
                print("The only file on Jim's desktop is entitled: CSIT Guinea Pig Feeding Schedule.")
                print("You click the file and this is what you see:\n")
                print("GUINEA PIG FEEDING SCHEDULE")
                print(" --------------------------")
                print("|Date     | Time   | Name  |")
                print("|--------------------------|")
                print("|5/6/2012 | 5:00pm | Jim   |")
                print("|5/7/2012 | 5:00pm | Kevin |")
                print("|5/8/2012 | 5:00pm | Ron   |")
                print(" -------------------------- ")
                break
            else:
                print("............")
                print("............")
                print("............")
                print("Invalid Password!")

def alphaCipher(code):
    alpha='abcdefghijklmnopqrstuvwxyz'
    newCode=''
    for char in code:
        index=alpha.find(char)
        newChar=alpha[::-1][index]
        newCode=newCode+newChar
    return newCode

