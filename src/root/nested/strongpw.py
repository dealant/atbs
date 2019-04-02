#! python3
import sys, re
if len(sys.argv) < 2:
    print('Usage: python strongpw.py - To check if pw is strong')
    sys.exit()
 
password = sys.argv[1] #first command line arg is the password to test

# TODO: make a Regex at least 8 characters.
pwlength = re.compile(r'.{8,}')
test0 = pwlength.search(password)

if test0 == None:
    exit('Password is too short')

# TODO: make a Regex contains both uppercase and lowercase letters
pwlcase = re.compile(r'[(a-z)]+')
pwucase = re.compile(r'[(A-Z)+]')
test11 = pwlcase.search(password)
test12 = pwucase.search(password)
test1 = test11 and test12
# TODO: make a regex that has at least one digit
pwnum = re.compile(r'\d+')
test2 = pwnum.search(password)
#===============================================================================
# Jenny's coffee
# 3 pumps of syrup
# 3 table spoons of creamer
#===============================================================================
# check password from user against all three regex

alltest = [test0, test1, test2]
strength = 0

for i in alltest:
    if i is not None:
        strength = strength+1

result = {'0': 'Your password is weak',
          '1': 'Your password is mediocore',
          '2': 'Your password is okay',
          '3': 'Your password is strong'}

print(result[str(strength)])
