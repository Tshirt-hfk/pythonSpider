from selenium import webdriver
driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  #调用chrome浏览器
driver.get('https://www.baidu.com')
print(driver.title)