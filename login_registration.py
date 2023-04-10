from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

# #1
# driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)
# #2
# acc = driver.find_element(By.CSS_SELECTOR, "#menu-item-50 a")
# acc.click()
# #3
# reg_mail = driver.find_element(By.ID, "reg_email")
# reg_mail.send_keys("avfk@mail.ru")
# #4
# reg_pass = driver.find_element(By.ID, "reg_password")
# reg_pass.send_keys("ASTON8j/hr5a-")
# #5
# regist_btn = driver.find_element(By.CSS_SELECTOR, ".register input:nth-child(3)")
# regist_btn.click()
# driver.quit()
#-------------------------Второй тест____________________________
#1
driver.get("https://practice.automationtesting.in/")
#2
acc = driver.find_element(By.CSS_SELECTOR, "#menu-item-50 a")
acc.click()
#3
login_mail = driver.find_element(By.ID, "username")
login_mail.send_keys("avfk@mail.ru")
#4
login_pass = driver.find_element(By.ID, "password")
login_pass.send_keys("ASTON8j/hr5a-")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
logout = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
driver.quit()