import string
import secrets
import argparse
import re

#third party, must be installed with pip, apt, etc
import requests

parser = argparse.ArgumentParser(
                    prog='pwgen',
                    description='Generates a secure password')
parser.add_argument('-u', '--uppercase', action='store_true') # Uppercase
parser.add_argument('-d', '--digits', action='store_true') # Digits
parser.add_argument('-s', '--symbols', action='store_true') # symbols 
parser.add_argument('-l', '--length') # length
parser.add_argument('-w', '--words', action='store_true') # dictionary words

args = parser.parse_args()

pw_length = 16
if(args.length != None):
    pw_length = int(args.length)

word_list = None 

def fetch_words():
    global word_list
    meaningpedia_response = requests.get("https://meaningpedia.com/5-letter-words?show=all")
    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
    word_list = pattern.findall(meaningpedia_response.text)

def generate():
    lowercase   = ''.join(secrets.choice(string.ascii_lowercase)    for i in range(64))
    uppercase   = ''.join(secrets.choice(string.ascii_uppercase)    for i in range(64))
    digits      = ''.join(secrets.choice(string.digits)             for i in range(64))
    symbols     = ''.join(secrets.choice(string.punctuation)        for i in range(64))
    combined_sequence = lowercase 
    
    if(args.words):
        fetch_words()
        password = '-'.join(secrets.choice(word_list) for i in range(4))
    else:
        if(args.uppercase):
            combined_sequence += uppercase
        if(args.digits):
            combined_sequence += digits
        if(args.symbols):
            combined_sequence += symbols 
        password =  ''.join(secrets.choice(combined_sequence) for i in range(pw_length))
    return password

print(generate())
