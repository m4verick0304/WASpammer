from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome setup
options = Options()
options.binary_location = "/usr/bin/google-chrome-stable"

service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

# FIXED URL
driver.get("https://web.whatsapp.com")

input("Scan QR and press Enter...")
A = input("Select chat and press Enter...")

WAIT = WebDriverWait(driver, 30)

# Try all possible search selectors
SEARCH_SELECTORS = [
    (By.XPATH, "//div[@aria-label='Search']"),
    (By.XPATH, "//div[@data-tab='3']"),
    (By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='3']"),
    (By.XPATH, "//p[contains(@class,'selectable-text')]"),
    (By.XPATH, "//div[contains(@class,'selectable-text') and @contenteditable='true']")
]

search = None
for selector in SEARCH_SELECTORS:
    try:
        search = WAIT.until(EC.presence_of_element_located(selector))
        print("Found search bar using:", selector)
        break
    except:
        pass

if search is None:
    raise Exception("Could NOT find WhatsApp search bar. UI changed.")

search.click()
search.send_keys("A")
time.sleep(0.5)
search.send_keys(Keys.ENTER)

message = input("Enter your message: ")
count = int(input("Enter number of messages to send: "))

for _ in range(count):
    box = driver.find_elements(By.CSS_SELECTOR, "div[contenteditable='true']")[-1]
    box.send_keys(message + Keys.ENTER)
    time.sleep(0.3)
print("Messages sent successfully.")
