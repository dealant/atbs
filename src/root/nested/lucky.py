#! python3
'''
Created on May 26, 2019

@author: alansuface
This program:
Gets search keywords from the command line arguments.
Retrieves the search results page.
Opens a browser tab for each result

Fucntionally this means your code will need to do the following:
Read the command line arguments from sys.argv.
Fetch the search result page with the requests module.
Find the links to each search result.
Call the webbrowser.open() function to open the web browser.
'''

import sys, requests, webbrowser, bs4

#TODO: Gets search keywords from the command line arguments.

print('GETTING IT FROM GOOGLE') #the text displayed while loading results
SEARCHVAR = sys.argv[1:]
res = requests.get('http://google.com/search?q=' + ' '.join(SEARCHVAR))
res.raise_for_status()
print('Searching ' + ' '.join(SEARCHVAR[:]) + ' on Google')
#TODO: Retrieves the search results page.
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print('Parsing')
RequestText = open('sourcetext.txt', 'w')
RequestText.write(res.text)
RequestText.close
# Open a browser tab for each result.
linkElems = soup.select('.jfp3ef a')
print('Finding results in parsed data')
#TODO: Opens a browser tab for each result
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
print('done')