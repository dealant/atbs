'''
using regular expressions extract all emails and phone numbers from body of text

outline
get the text from clipboard
make regex for both email and phone number 
find all emails and phone number
paste results to clipboard
'''
#! python3
import pyperclip, re

phonenum = re.compile(r'''(
    (/d{3}|/(/d{3}/))? #area code
    )