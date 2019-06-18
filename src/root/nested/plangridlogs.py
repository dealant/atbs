from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def findxpathclick(xpathname):
    button = browser.find_element_by_xpath(xpathname)
    button.click()
    time.sleep(5)

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderlist', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.manager.showAlertOnComplete', False)
profile.set_preference('browser.download.dir','C:\\Users\\alan3\\Downloads')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',\
        'application/octet-stream'
        +',text/csv')
#start up browser
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('https://app.plangrid.com/en/login')
uname = browser.find_element_by_id('test-email')
uname.send_keys('alan.tsui@bayley.net')
findxpathclick('//*[@id="test-submitLogin"]') #to password page
pword = browser.find_element_by_id('test-password')
pword.send_keys('TsuiA001')
findxpathclick('//*[@id="test-submitLogin"]') #login
#glacier project
findxpathclick('/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/a/span[1]/span/span')
#select RFI's and download
findxpathclick('/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div/ul[1]/li[4]') #go to RFI section
findxpathclick('/html/body/div[1]/div/div[2]/div/div/div[3]/div/form/div[4]/div[2]/ul/li[2]') #press open status
findxpathclick('/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/div/button[1]') #press reports
findxpathclick('//*[@id="csvRadio"]')#change to csv radio
findxpathclick('/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/span[2]/span[2]') #download csv file
findxpathclick('/html/body/div[1]/div/div[2]/div/div/div[3]/div/div/table/tbody/tr[1]/td[7]/a/span[1]')
#select submittals and download
findxpathclick('/html/body/div[1]/div/div[1]/div/div/ul[1]/li[8]/a') #click on submittals section
time.sleep(5)
findxpathclick('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/a[2]') #go to packages
findxpathclick('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/button[2]') #turn on filters
ballincourt = browser.find_element_by_xpath(\
        '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/fieldset[1]/div/div[1]/input')
ballincourt.send_keys('jknight@integrusarch.com')
ballincourt.send_keys(Keys.ARROW_DOWN)
ballincourt.send_keys(Keys.ENTER)
substatus = browser.find_element_by_xpath(\
            '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/fieldset[3]/div/div[1]/input')
substatus.send_keys('In Review')
substatus.send_keys(Keys.ARROW_DOWN)
substatus.send_keys(Keys.ENTER)
findxpathclick('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/button[1]') #press on export


