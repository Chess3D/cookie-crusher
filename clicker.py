# Import selenium requirements
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


# Wait for page to load
def load(driver):

    # Define wait
    wait = WebDriverWait(driver, 10)

    # Element ID of the loading message
    load_ID = 'loading'

    # Element ID of the cookie
    cookie_ID = 'bigCookie'

    # Wait until loading starts
    wait.until( ec.visibility_of_element_located((By.ID, load_ID)) )

    # Wait until loading starts
    wait.until( ec.invisibility_of_element_located((By.ID, load_ID)) )

    # Wait until cookie is clickable
    wait.until( ec.element_to_be_clickable((By.ID, cookie_ID)) )


# Click the cookie the desired number of times
def click_cookie(driver, count=1):

    # Element ID of the clickable cookie
    cookie_ID = 'bigCookie'

    # Finds the cookie element
    cookie_element = driver.find_element_by_id(cookie_ID)

    # Click the cookie the desired amount of times
    for i in range(count):
        cookie_element.click()


# Buys all possible upgrades of the given type
def buy_upgrades(driver, upgrade):

    # Selects correct class for crate upgrades
    if upgrade == 'crate':
        upgrade_class = 'crate.upgrade.enabled'

    # Selects correct class for product upgrades
    elif upgrade == 'product':
        upgrade_class = 'product.unlocked.enabled'

    # Tries to find and the purchase an upgrade
    try:

        # Looks for purchasable upgrade
        upgrade_element = driver.find_element_by_class_name(upgrade_class)
        
        # Purchases upgrade
        if upgrade_element.is_displayed():
            upgrade_element.click()

    # Exit the recursive loop when no upgrades can be bought
    except:
        return
    
    # Recursively loop to buy all available upgrades
    buy_upgrades(driver, upgrade)


# Attempts to click the golden cookie
def golden_cookie(driver):
    
    # Element ID of the golden cookie
    cookie_ID = 'goldenCookie'

    # Tries to click the golden cookie
    try:

        # Finds the golden cookie elemtnt
        cookie_element = driver.find_element_by_id(cookie_ID)

        # Clicks the golden cookie
        if cookie_element.is_displayed():
            cookie_element.click()
    
    # Exits the definition
    except:
        return