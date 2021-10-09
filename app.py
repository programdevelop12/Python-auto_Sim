import pyautogui
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'C:\Users\Lukas Lima\Documents\Repositorio\Python\Automação Pesquisa S vs D\geckodriver.exe')

driver.get('https://duckduckgo.com/')
driver.find_element_by_name("q").send_keys("Spotify vs Deezer" + Keys.RETURN)