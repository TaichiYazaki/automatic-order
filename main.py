import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver

BASE_URL = "https://jp.supreme.com/products/2i_0eglt08q5z-te"

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        options = webdriver.ChromeOptions()
)
driver.get(BASE_URL)
select_size = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/div/div[4]/div[2]/div[2]/div[1]/div[2]/div/select")
size = Select(select_size)
size.select_by_value("42725425381580")
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div/div/div/div[2]/div[2]/form/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[1]/input").click()
time.sleep(1)
choose_payment_page = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div/div/div/div[1]/div/div/div/a[2]")
driver.execute_script('return arguments[0].click()', choose_payment_page)

load_dotenv()
EMAIL = os.getenv('EMAIL')
LAST_NAME = os.getenv('LAST_NAME')
FIRST_NAME = os.getenv('FIRST_NAME')
POST_CODE = os.getenv('POST_CODE')
CITY = os.getenv('CITY')
ADDRESS = os.getenv('ADDRESS')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/main/div/form/div[1]/div/div/section/div/div/div/div/div[3]/div/div/div/input").send_keys(EMAIL)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/main/div/form/div[1]/div/div/div[2]/div/section/div/div[2]/section/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/input").send_keys(LAST_NAME)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/main/div/form/div[1]/div/div/div[2]/div/section/div/div[2]/section/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/input").send_keys(FIRST_NAME)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/main/div/form/div[1]/div/div/div[2]/div/section/div/div[2]/section/div/div/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div/div/div/input").send_keys(POST_CODE)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/main/div/form/div[1]/div/div/div[2]/div/section/div/div[2]/section/div/div/div[1]/div/div/div/div[1]/div[4]/div/div/div/input").send_keys(CITY)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/main/div[1]/form/div[1]/div/div/div[2]/div/section/div/div[2]/section/div/div/div[1]/div/div/div/div[1]/div[5]/div/div/div/div/div/input").send_keys(ADDRESS)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/main/div[1]/form/div[1]/div/div/div[2]/div/section/div/div[2]/section/div/div/div[1]/div/div/div/div[1]/div[7]/div/div/div/input").send_keys(PHONE_NUMBER)

select_prefecture = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/main/div[1]/form/div[1]/div/div/div[2]/div/section/div/div[2]/section/div/div/div[1]/div/div/div/div[1]/div[3]/div[2]/div/div/select")
prefecture = Select(select_prefecture)
prefecture.select_by_value("JP-11")

select_payment_method = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/main/div[1]/form/div[1]/div/div/div[3]/div/section/div/div[2]/div/div/div/div/fieldset/div/div[2]/label/div/div[1]/input")
driver.execute_script('return arguments[0].click()', select_payment_method)
time.sleep(1)
# # 買わない時は押さないこと
# #driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/main/div/form/div[1]/div/div/div[4]/div/section/div/div/div/div/div/div/div/button").click()
time.sleep(5)
driver.quit()