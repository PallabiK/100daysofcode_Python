from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # count.click()
#
# # anyone_can_edit = driver.find_element(By.LINK_TEXT, "anyone can edit")
# # anyone_can_edit.click()
#
# search = driver.find_element(By.NAME, 'search')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
#
#
# driver.close()

driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Haha")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Lala")
email = driver.find_element(By.NAME, "email")
email.send_keys("hahalala@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()


