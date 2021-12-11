from selenium import webdriver

url = "https://www.google.com"
#driver = webdriver.Chrome()
driver = webdriver.Chrome("/home/success/python3/chromedriver")
driver.get(url)
print(driver.page_source)
driver.close()
