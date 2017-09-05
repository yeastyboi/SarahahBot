import os, time, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#### HOW TO USE ################################################################################################
'''
If you aren't using 64 bit linux delete the chromedriver from assets and download the correct drive for your os:
https://chromedriver.storage.googleapis.com/index.html?path=2.30/
Add the driver to the assets folder

Make sure that:
You have PIP installed
You have google chrome installed

For all OSes:
Use pip to install selenium
pip install -U selenium

Modify the settings
'''
################################################################################################################

#is linux or mac
unix = True;

#Who's profile to spam (ie https://victim.sarahah.com/)
victim = "victim"

#A random message will get picked each iteration
messages = [
"Message 1",
"Message 2",
"Message 3"
]

#author tag (leave blank for none)
author = ""

#use https ("s" = https, "" = http)
https = "s"

if unix:
	os.system("clear")

print("Yeasty Sarahah Bot v1")
print("Launching chrome automation...")
chromedriver = "assets/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

count = 0
mes = len(messages)
while 1:
	count += 1
	try:
		message = messages[random.randint(0, mes-1)]
		print("Spamming " + victim + " with " + message)
		driver.get("http" + https + "://" + victim + ".sarahah.com/")
		q = driver.find_element_by_id("Text")
		q.send_keys(message + author)
		driver.find_element_by_id("Send").click()
		time.sleep(3)
	except:
		driver.quit()
		os.system("python auto.py")
