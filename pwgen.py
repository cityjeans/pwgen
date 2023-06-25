import string
import secrets

requirements = [False, False, False, False]
input_prompts = ["Use uppercase letters? (Y/n): ","Use numbers? (Y/n): ","Use punctuation? (Y/n): ","Length of password? (integer above 6, default: 16): "]
pw_length = 16

def get_password_requirements():
    def get_boolean_input(prompt):
        inp = ""
        while True:
            inp = input(prompt).lower()
            if(inp == "n" or inp == "no"):
                return False
            elif(inp == "y" or inp == "yes" or inp == ""):
                return True

    def get_int_input():
        global pw_length
        while True:
            inp = input(input_prompts[3])
            if(inp.isdecimal() and int(inp) > 5 ):
                pw_length = int(inp)
                break
            elif(inp == ""):
                pw_length = 16
                break

    for i in range(3):
        if(get_boolean_input(input_prompts[i])):
            requirements[i] = True
    get_int_input()

def generate():
    while True:
        lowercase   = ''.join(secrets.choice(string.ascii_lowercase)    for i in range(64))
        uppercase   = ''.join(secrets.choice(string.ascii_uppercase)    for i in range(64))
        digits      = ''.join(secrets.choice(string.digits)             for i in range(64))
        symbols     = ''.join(secrets.choice(string.punctuation)        for i in range(64))

        intermediate = [uppercase, digits, symbols]

        s = lowercase 

        for i in range(3):
            if(requirements[i]):
                s += intermediate[i]

        password =  ''.join(secrets.choice(s) for i in range(pw_length))
        return password


get_password_requirements()
print(generate())
