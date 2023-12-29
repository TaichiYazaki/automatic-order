import os
from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        options = webdriver.ChromeOptions()
    )
driver.get("https://www.google.co.jp/")

