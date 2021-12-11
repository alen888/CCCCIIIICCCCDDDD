from selenium import webdriver

url = "https://www.google.com"
#driver = webdriver.Chrome()
driver = webdriver.Chrome("/var/lib/jenkins/workspace/Freestyle_0001/chromedriver")
driver.get(url)
print(driver.page_source)
driver.close()
