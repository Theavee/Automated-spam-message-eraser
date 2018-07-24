import time
from selenium import webdriver
from getpass import getpass

user_name = input('enter user name: ')
password = getpass('enter password: ')

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

user_name_box = browser.find_element_by_xpath('//*[@id="identifierId"]')
user_name_box.send_keys(user_name)

next_button = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/content/span')
next_button.click()
time.sleep(2)

password_box = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/div[1]/div/div[1]/div/div[1]/input')
password_box.send_keys(password)


login_button = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/content/span')
login_button.click()
time.sleep(3)


browser.get('https://mail.google.com/mail/u/0/#inbox')

more_section = browser.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/span/span[1]')
more_section.click()
time.sleep(2)

spam_section = browser.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/div/div[4]/div/div/div[2]/span/a')
spam_section.click()
time.sleep(2)

browser.get('https://mail.google.com/mail/u/0/#spam')
open_spam_message = browser.find_element_by_xpath('//*[@id=":iu"]').click()
delete_spam_message = browser.find_element_by_xpath('/html/body/div[13]/div[3]/button[1]').click()

