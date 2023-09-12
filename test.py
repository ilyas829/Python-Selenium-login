# Importing the necessary modules
from selenium import webdriver # To control the browser
from selenium.webdriver.common.keys import Keys # To send keyboard input
import time # To add some delay between actions

# Creating a webdriver object and launching the browser
driver = webdriver.Chrome() # You can use other browsers such as Firefox, Edge, etc.

# Navigating to the Gmail login page
driver.get("https://mail.google.com/mail/u/0/#inbox")

# Finding the element for entering the email or phone number
email = driver.find_element_by_id("identifierId")

# Sending the email or phone number to the element
email.send_keys("your_email@gmail.com") # Replace with your email or phone number

# Finding and clicking the next button
next_button = driver.find_element_by_id("identifierNext")
next_button.click()

# Adding some delay to wait for the password page to load
time.sleep(3)

# Finding the element for entering the password
password = driver.find_element_by_name("password")

# Sending the password to the element
password.send_keys("your_password") # Replace with your password

# Finding and clicking the next button
next_button = driver.find_element_by_id("passwordNext")
next_button.click()

# Adding some delay to wait for the inbox page to load
time.sleep(5)

# Printing a success message
print("Logged in successfully")

# Closing the browser
driver.close()
