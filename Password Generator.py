
import string
import random
import time

def choice():
    global n
    print('''
    How many digits do you want in your password? (7-50)
    ''')
    n = int(input(": "))
    if n >50 :
        print("Too big. (7-50)")
        choice()
    elif n < 7:
        print("Too Small. (7-50)")
        choice()
    else:
        config()

def config():
    global ran_str
    ran_str = ''.join(random.choices(string.ascii_uppercase +string.ascii_lowercase+ string.digits, k = n))
    final()

def final():
    print("Random String : " + str(ran_str))
    time.sleep(0.5)
    save = input("Would you like to save the password? (y/n)")
    if save == "y" or save == "Y":
        opt = input("What program are you going to use the password? ")
        with open("password.txt", mode = "a") as f:
            f.write("\n")
            f.write(f"{opt} - Your password: {ran_str}")
        print(f"Ok saved")
        input("")
    elif save == "n" or save == "N":
        print("Ok")
    else:
        print("Unknown command.")
        final()
    
choice()
