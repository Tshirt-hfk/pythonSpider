from selenium import webdriver
driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  #调用chrome浏览器
driver.get('http://localhost:8888/signin')
elem_user = driver.find_element_by_id("email")
elem_user.send_keys('sao@outlook.com') #用户名
elem_pwd = driver.find_element_by_id('password')
elem_pwd.send_keys('123456')  #密码
elem_rem = driver.find_element_by_id("submit")
elem_rem.click()
driver.get('http://www.baidu.com/')
driver.get('http://localhost:8888')