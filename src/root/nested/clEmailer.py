#! python3
'''
Created on May 27, 2019

@author: alansuface

Command Line Emailer
Write a program that takes an email address and string of text on the command line and then, 
using Selenium, logs into your email account and sends an email of the string to the provided address. 
(You might want to set up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs. 

You could also write a similar program to send messages from a Facebook or Twitter account.

'''
import sys, re
from selenium import webdriver

emailreg = re.compile(r'''(
    [a-zA-Z0-9._%+-]+             #user name
    @                           #the @ sign 
    [a-zA-Z0-9.-]+             #domainname
    (\.(com|org|net|gov|edu))    #domain type
    )''', re.VERBOSE)

#TODO: Read arguments and split them up as needed
if len(sys.argv) > 3 and sys.argv[1].search(emailreg) is True:
    EMAILADDR = sys.argv[1] 
    MSG = sys.argv[2:]
#TODO: open up gmail
browser = webdriver.Firefox()
browser.get('https://mail.google.com')

#TODO: paste in the email address and body

#TODO: hit send
