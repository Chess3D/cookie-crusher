from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Creates an Options object so the browser can run headlessly
options = Options()

# Sets the headless option to true
options.headless = False

# Cookie Clicker website
website = 'https://clickspeedtest.com/5-seconds.html'

# Starts the browser headlessly
driver = webdriver.Chrome(options=options)

driver.get(website)

print('Start clicking')
id = driver.find_element_by_id('clicker')
while True: # click for ever
  try:
    id.click() 
  except Exception as ex: # until it breaks
    print('Time is over')
    break

time.sleep(1) # results are slow
result = driver.find_element_by_css_selector('.times')
print(f'Result: {result.text}\n') 
driver.close()