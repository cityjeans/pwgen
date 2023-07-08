#!/usr/bin/env python3
import string
import secrets
import argparse

# third party dependencies
#import requests
from urllib.request import urlopen

def fetch_local_words(word_list=[]):
    with open("eff_words.txt", "r") as file:
        for line in file:
            word_list.append(line)
    return word_list

def fetch_url_words(word_list=[]):
    url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
    with urlopen(url) as file:
        for line in file:
            line_parse = line.split()
            word_list.append(line_parse[1].decode('utf-8'))
    return word_list

def generate(word_list):
    lowercase   = ''.join(secrets.choice(string.ascii_lowercase)    for i in range(64))
    uppercase   = ''.join(secrets.choice(string.ascii_uppercase)    for i in range(64))
    digits      = ''.join(secrets.choice(string.digits)             for i in range(64))
    symbols     = ''.join(secrets.choice('/=!@#$%&*()')        for i in range(64))
    combined_sequence = ""
    words = [""]
    if args.words:
        words = [secrets.choice(word_list) for x in range(words_amount)]

    if(args.uppercase):
        combined_sequence += uppercase
        words = [i.capitalize() for i in words]
    if(args.digits):
        combined_sequence += digits
        words.insert(0, digits[0:2])
    if args.symbols:
        combined_sequence += symbols
        words.append(symbols[0:2])
    if args.words:
        password = '-'.join(words)
    else:
        combined_sequence += lowercase
        password = ''.join(secrets.choice(combined_sequence) for i in range(pw_length))
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog='pwgen',
                        description='Generates a secure password')
    parser.add_argument('-u', '--uppercase', action='store_true')   # Uppercase
    parser.add_argument('-d', '--digits', action='store_true')      # Digits
    parser.add_argument('-s', '--symbols', action='store_true')     # symbols 
    parser.add_argument('-l', '--length')                           # length
    parser.add_argument('-w', '--words', action='store_true')       # dictionary words
    args = parser.parse_args()

    pw_length = 16
    words_amount = 4

    if(args.length != None):
        pw_length = int(args.length)
        if args.words:
            words_amount = int(args.length)


print(generate(fetch_local_words()))

