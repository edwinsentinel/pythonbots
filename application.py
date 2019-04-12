from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

#enter the link to the website you want to automate login.
website_link="https://fms.logistics.co.ke/"
#enter your login username
username="Pius"
#enter your login password
password="*2016*"

#enter the element for username input field
element_for_username="Login1$UserName"
#enter the element for password input field
element_for_password="Login1$Password"
#enter the element for submit button
element_for_submit="Login1$LoginButton"

browser= webdriver.Chrome()#for macOS users[for others use chrome vis chromedriver]
browser.get((website_link))	

try:
	username = browser.find_element_by_name(element_for_username)
	username.send_keys(username)		
	password  = browser.find_element_by_name(element_for_password)
	password.send_keys(password)
	signInButton = browser.find_element_by_name(element_for_submit)
	signInButton.click()
	
	#### to quit the browser uncomment the following lines ####
	# time.sleep(3)
	# browser.quit()
	# time.sleep(1)
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)
except Exception:
	#### This exception occurs if the element are not found in the webpage.
	print ("Some error occured :(") 

	#### to quit the browser uncomment the following lines ####
	# browser.quit()
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)