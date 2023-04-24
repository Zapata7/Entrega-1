
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.saucedemo.com/")

driver.set_window_size(1024, 600)
driver.maximize_window()

Usuario = driver.find_element(By.ID,"user-name")
Usuario.send_keys("standard_user")
time.sleep(3)

Clave = driver.find_element(By.ID,"password")
Clave.send_keys("secret_sauce")
Usuario.send_keys(Keys.ENTER)


time.sleep(5)
