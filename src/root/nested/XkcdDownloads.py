#! python3

'''
Created on May 27, 2019

@author: alansuface

Loads the XKCD home page.
Saves the comic image on that page.
Follows the Previous Comic link.
Repeats until it reaches the first comic.


'''
import requests, bs4, webbrowser, os

url = 'http://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd

#TODO: Download page with requests moduled (function)

while not url.endswith('#'):
    # Download the page.
    print('Downloading page {0}'.format(url)) #gives the URL that is being downloaded to the user
    res = requests.get(url) #getting the page
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    #TODO: Find the URL of img
    img = soup.select('#comic img')
    
    ComicElem = soup.select('#comic img')
    if ComicElem == []: 
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + ComicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    
    #TODO: Download and save the img with iter_content()
    
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    
    #TODO: Find the url of the previous page and repeat
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')