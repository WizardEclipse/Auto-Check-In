from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

def initialize():
    #tweaks selenium options to store cached cookies in the data folder
    global options
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=./chromedriver_win32/data")

    #makes webdriver
    global chrome
    chrome = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe", options=options)

    #calls webdriver to open whatsaap
    chrome.get('https://web.whatsapp.com/')

    #sleeps to allow loading time
    time.sleep(60)
    return

def SendMessage(name, mess):
    user = chrome.find_element_by_xpath(f"//tagname[@title='{name}']")
    user.click()

    time.sleep(15)

    message_box = chrome.find_element_by_xpath('//div[@class="_3uMse"]')
    message_box.send_keys(mess)

    time.sleep(10)
    
    button = chrome.find_element_by_xpath('//button[@class="_1U1xa"]')
    button.click()
    
    print(f'"{mess}" sent to {name} at {time.ctime()}')

    return
        

def exit():
    time.sleep(10)
    chrome.quit()
    return

    
    
