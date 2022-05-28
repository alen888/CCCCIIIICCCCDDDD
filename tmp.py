from selenium import webdriver

url = "https://www.google.com"
#driver = webdriver.Chrome()
#driver = webdriver.Chrome("/usr/lib/python3/dist-packages/chromedriver")
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get(url)
print(driver.page_source)
driver.close()
