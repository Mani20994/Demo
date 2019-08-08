from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("C:\\Users\\lts\\PycharmProjects\\Test_Automation\\Drivers\\chromedriver.exe")

driver.maximize_window()


driver.get("http://real-estate.itechscripts.com/login.php")

time.sleep(5)
driver.close()
