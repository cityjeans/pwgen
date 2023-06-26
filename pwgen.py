import string
import secrets
import argparse

parser = argparse.ArgumentParser(
                    prog='pwgen',
                    description='Generates a secure password')
parser.add_argument('-u', '--uppercase', action='store_true') # Uppercase
parser.add_argument('-d', '--digits', action='store_true') # Digits
parser.add_argument('-s', '--symbols', action='store_true') # symbols 
parser.add_argument('-l', '--length') # length

args = parser.parse_args()

pw_length = 16
if(args.length != None):
    pw_length = int(args.length)

def generate():
    lowercase   = ''.join(secrets.choice(string.ascii_lowercase)    for i in range(64))
    uppercase   = ''.join(secrets.choice(string.ascii_uppercase)    for i in range(64))
    digits      = ''.join(secrets.choice(string.digits)             for i in range(64))
    symbols     = ''.join(secrets.choice(string.punctuation)        for i in range(64))

    combined_sequence = lowercase 
    
    if(args.uppercase):
        combined_sequence += uppercase
    if(args.digits):
        combined_sequence += digits
    if(args.symbols):
        combined_sequence += symbols 

    password =  ''.join(secrets.choice(combined_sequence) for i in range(pw_length))
    return password

print(generate())
