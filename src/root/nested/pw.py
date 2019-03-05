#! python 3
# a password organizer

password = {'1' : ' 0001',
            'desktoppin' : '0202',
            'worklaptop' : 'thing'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in password:
    pyperclip.copy(password[account])
    print('password for ' + account + 'copied to clipboard.')
else:
    print('You do not have a passord for' + account)
    

    