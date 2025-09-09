import random
import string

def Password_Generator(password_size, check_ch, check_special):
    password_list = []
    passwordPhrase = ""
        
    for i in range(0, password_size):
        if check_ch == 1:
            letterOrNumber = random.choice(["letter", "number"])
            if letterOrNumber == "letter":
                passwordPhrase = f"{passwordPhrase}{random.choice(string.ascii_letters)}"
            elif letterOrNumber == "number":
                passwordPhrase = f"{passwordPhrase}{random.randint(0, 9)}"
        else:
            password = random.randint(0,9)
            password_list.append(password)
            passwordPhrase = f"{passwordPhrase}{random.randint(0, 9)}"

        if check_special == 1:
            passwordPhrase = f"{passwordPhrase}{random.choice(string.punctuation)}"

    return passwordPhrase

