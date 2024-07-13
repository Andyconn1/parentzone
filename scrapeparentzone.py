from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run in headless mode (optional)
driver = webdriver.Chrome(options=options)

# Function to log in to the website
def login_to_website(driver, url, username, password):
    driver.get(url)
   
    # Find the login elements and perform login
    username_input = driver.find_element(By.ID, 'email')  # Change 'username_field_id' to the actual ID
    password_input = driver.find_element(By.ID, 'password')  # Change 'password_field_id' to the actual ID
    login_button = driver.find_element(By.CSS_SELECTOR, "[data-test-id='login_btn']")      # Change 'login_button_id' to the actual ID

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
   
    # Wait for the login to complete (you may need to adjust the wait time or use explicit waits)
    time.sleep(2)

# Function to scroll to the bottom of the page
def scroll_to_bottom(driver):
   
    # Find the scrollable div container
    scroll_container = driver.find_element(By.CSS_SELECTOR, "[data-test-id='timeline_scroll_container']")
    last_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_container)
    # while True:
    for _ in range(10):
        # Scroll the scrollable div container
        time.sleep(1)
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll_container)
        
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_container)
        if new_height == last_height:
            break
        last_height = new_height

def get_password():
    with open('password.txt', 'r') as file:
        return file.read()

# Login credentials
url = 'https://www.parentzone.me/login'
username = 'andyconn1988@googlemail.com'
password = get_password()

# Log in to the website
login_to_website(driver, url, username, password)

# Navigate to the target page after login if necessary
driver.get('https://www.parentzone.me/timeline')

# Scroll to the bottom to load all data
scroll_to_bottom(driver)

# Get page source and parse it with BeautifulSoup
time.sleep(1)
page_source = driver.page_source
with open('soup_object.html', 'w', encoding='utf-8') as file:
    file.write(str(page_source))

# Close the driver
driver.quit()

