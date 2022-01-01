import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('env/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get('https://www.ribblecycles.co.uk')
driver.implicitly_wait(10)

ribbleSearchBox = driver.find_element(By.CSS_SELECTOR, "#search")  # search product
ribbleSearchBox.send_keys("Look Keo Classic Plu")
ribbleSearchBox.submit()

driver.find_element(By.PARTIAL_LINK_TEXT, "Look Keo Classic Plu").click()  # add product
driver.find_element(By.XPATH, ".//button[@title= 'Add to Basket']").click()
driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/header[1]/div[1]/div[10]/a[1]/span[1]/i[1]").click()
a = driver.find_element(By.PARTIAL_LINK_TEXT, "Look Keo Classic Plu")  # assert item exist
basket = a.text
print(basket)

driver.find_element(By.XPATH, ".//button[@title= 'Continue to Checkout']").click()

driver.find_element(By.CSS_SELECTOR, "#login-email").send_keys('estherokafor05@gmail.com')  # email

driver.find_element(By.CSS_SELECTOR, '#login-password').send_keys('Revelation12')  # password

driver.find_element(By.CSS_SELECTOR, "#login-submit").click()
driver.find_element(By.XPATH, "//*[@id='shipping-buttons-container']/button").click()
driver.implicitly_wait(10)
driver.quit()

driver.find_element(By.XPATH, "//*[@id='shipping-method-buttons-container']/button").click()
driver.find_element(By.XPATH, "//*[@id='checkout-payment-method-load']/dt[2]/label").click()
driver.find_element(By.XPATH, "//*[@id='stripe-payments-card-number']").send_keys('5531 8866 5214 2950')
driver.find_element(By.XPATH, "//*[@id='root']/form/span[2]/span/input").send_keys('09 / 32')
driver.find_element(By.XPATH, "//*[@id='root']/form/span[2]/span/input").send_keys('441')
driver.find_element(By.XPATH, "//*[@id='payment-buttons-container']/button").click()

driver.quit()
