from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import loginInfo
import os

options = Options()
chromedriver_path = "/chromedriver.exe" # driver path

r = open("follow_req.txt","w")

browser = webdriver.Chrome(executable_path=chromedriver_path, options=options) #Start Browser
browser.get("https://www.instagram.com/")
time.sleep(3) #Waiting 3 seconds after we open the page.

#login to your instagram account 
browser.find_element_by_name ("username").send_keys (loginInfo.username)
browser.find_element_by_name ("password").send_keys(loginInfo.password)
login_button = browser.find_element_by_xpath ("//button[@type='submit']")
login_button.click()
time.sleep(5)

# go to follow requests page 
browser.get("https://www.instagram.com/accounts/access_tool/current_follow_requests")

#open full list of ongoing follow requests 
while True:
    try:
        vm_button = browser.find_element_by_xpath ("//button[@type='button']")
        vm_button.click()
        time.sleep(2)
    except NoSuchElementException:
        break

#list with all users with not accepted follow requests 
usernamesList = browser.find_elements_by_xpath("//div[@class='-utLf']") 

# create a txt file with the usernames of the ongoing requests 
for i in usernamesList:
    r.write(i.text+"\n")
r.close()

print('all on going follow requests are save in this file :  "follow_req.txt"')
browser.quit()

#start cancelling the requests 
os.system('python cancel_req.py')