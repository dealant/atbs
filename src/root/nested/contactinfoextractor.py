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
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

#create email regex
emailreg = re.compile(r'''(
    [a-zA-Z0-9._%+-]+             #user name
    @                           #the @ sign 
    [a-zA-Z0-9.-]+             #domainname
    (\.(com|org|net|gov|edu))    #domain type
    )''', re.VERBOSE)

# TODO: Find matches in clipboard text.

text = str(pyperclip.paste())
matches = []
for groups in phonenum.findall(text):
    phonefind = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phonefind += ' x' + groups[8]
    matches.append(phonefind)
for groups in emailreg.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
