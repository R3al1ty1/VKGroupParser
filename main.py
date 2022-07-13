from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

geckodriverLocation = r"/Users/user/Documents/geckodriver" # Location of geckodriver
firefoxProfile = r"/Users/Nasa/Library/Application Support/Firefox/Profiles/459ixwje.default" # Selected Firefox profile

service = Service(geckodriverLocation) # Setting up location

options = Options()
options.headless = True
options.set_preference('profile', firefoxProfile) # Setting up profile
browser = webdriver.Firefox(service=service, options=options)  # Creating webdriver

browser.get('https://vk.com/club143060440')
url = 'https://vk.com/club143060440'

def ratingGrabber(url):
    accountData = browser.find_element(by=By.CLASS_NAME, value='rate-minus').text
    downVotes = browser.find_element(by=By.CLASS_NAME, value='rate-minus').text
    percentage = browser.find_element(by = By.CLASS_NAME, value = 'rate-perc').text
    return upVotes, downVotes, percentage
start = time.time()
print(ratingGrabber(url))
end = time.time()
print(end - start)