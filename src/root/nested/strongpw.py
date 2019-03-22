#! python3
import pyperclip, re

# TODO: make a Regex at least 8 characters.

pwlength = re.compile(r'[a-zA-Z0-9._%+-]{8,}')

# TODO: make a Regex contains both uppercase and lowercase letters
pwcaseandnum = re.compile(r'[a-z]+[A-Z]+[0-9]+')
# TODO: make a regex that has at least one digit

# TODO: check password from user against all three regex
