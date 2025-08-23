from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def initialize_driver():
    driver = webdriver.Edge()
    return driver

def main():
    driver = initialize_driver()
    driver.get("https://www.saucedemo.com/")
    input_username = driver.find_element(By.ID, "user-name")
    print(input_username)

if __name__ == '__main__':
    main()