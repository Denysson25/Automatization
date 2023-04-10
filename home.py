from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

#1
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)
#2
driver.execute_script("window.scrollBy(0, 600);")
#3
book1 = driver.find_element(By.CSS_SELECTOR, ".col3-1.first h3")
book1.click()
#4
reviews1 = driver.find_element(By.CSS_SELECTOR, ".reviews_tab a")
reviews1.click()
#5
stars1 = driver.find_element(By.CSS_SELECTOR, ".stars a:nth-child(5)")
stars1.click()
#6
comment1 = driver.find_element(By.ID, "comment")
comment1.send_keys("Nice book!")
#7
name1 = driver.find_element(By.ID, "author")
name1.send_keys("Denis")
#8
email1 = driver.find_element(By.ID, "email")
email1.send_keys("avfk@mail.ru")
#9
submit = driver.find_element(By.NAME, "submit")
submit.click()
driver.quit()