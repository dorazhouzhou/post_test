import  random
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
result = random.randint(1,10)
print(result)
driver = ""
ele = driver.find_elements()
ele[{}].format(result).click