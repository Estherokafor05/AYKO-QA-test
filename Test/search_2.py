from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('env/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get('https://www.ribblecycles.co.uk')
driver.implicitly_wait(10)

driver.find_element(By.PARTIAL_LINK_TEXT, "Register or Log").click()  # login
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, "#email").send_keys('estherokafor05@gmail.com')  # email

driver.find_element(By.CSS_SELECTOR, '#pass').send_keys('Revelation12')  # password

driver.find_element(By.CSS_SELECTOR, "#send2").click()

searchBox = driver.find_element(By.CSS_SELECTOR, "#search")  # search
searchBox.send_keys("Look Keo Classic Plu")
searchBox.submit()

driver.find_element(By.PARTIAL_LINK_TEXT, "Look Keo Classic Plu").click()  # click product
content = driver.find_element(By.XPATH, "//div[@class = 'availability in-stock']").text  # assert error
if content.find("In stock"):
    print(content)
else:
    print('out of stock')
    driver.quit()
