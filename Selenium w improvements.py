# Added the following improvements: Add error handling for the case where the Chrome webdriver is not found or not executable. 
# You can use a try-except block to catch the error and print a helpful error message to the user.
# Use a with block to handle the creation and closing of the webdriver, which is a context manager. This ensures that the webdriver is properly closed even if an error occurs.
# Move the URL and expected h1 text to variables at the beginning of the script to make them easier to modify.
# Consider using the find_element_by_xpath method instead of presence_of_element_located to wait for the h1 element to load. This allows you to wait for a specific element with a given XPath, which can be more reliable than waiting for # any element of a certain type.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://example.com"
expected_h1_text = "Welcome to Example.com"

# Set up the Selenium webdriver
try:
    with webdriver.Chrome(options=options) as driver:
        # Navigate to the URL
        driver.get(url)

        # Wait for an element to load on the page
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='" + expected_h1_text + "']"))
        )

        # Find all links on the page and print their text and href attributes
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            print(link.text.strip(), link.get_attribute("href"))
except Exception as e:
    print("Error: " + str(e))

