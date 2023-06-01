from selenium import webdriver
from  bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
drive = webdriver.Chrome()

drive.get("https://moscowzoo.ru/animals/khishchnye/undefined?PAGEN_1=2")

print(drive.title)
html = drive.page_source
print(html)