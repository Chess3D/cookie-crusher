# Imports the functions in clicker
from clicker import *

# Imports selenium requirements
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Creates an Options object so the browser can run headlessly
options = Options()

# Sets the headless option to true
options.headless = False

# Cookie Clicker website
website = 'https://orteil.dashnet.org/cookieclicker/'

# Starts the browser headlessly
driver = webdriver.Chrome(options=options)
driver.get(website)

# Wait for page to load
load(driver)

# Infinate loop because the game never ends
while True:

    # Clicks the cookie 10 times
    click_cookie(driver, 10)

    # Attempts to buy crate upgrades
    buy_upgrades(driver, 'crate')

    # Attempts to buy product upgrades
    buy_upgrades(driver, 'product')

    # Attempts to click golden cookie
    golden_cookie(driver)