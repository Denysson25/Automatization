import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

#1
driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# #2
# acc = driver.find_element(By.CSS_SELECTOR, "#menu-item-50 a")
# acc.click()
# login_mail = driver.find_element(By.ID, "username")
# login_mail.send_keys("avfk@mail.ru")
# login_pass = driver.find_element(By.ID, "password")
# login_pass.send_keys("ASTON8j/hr5a-")
# #3
# shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a")
# shop_btn.click()
# #4
# book_forms = driver.find_element(By.CSS_SELECTOR, ".products.masonry-done>li:nth-child(3) img")
# book_forms.click()
# #5
# book_header = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".summary.entry-summary>h1"), "HTML5 Forms"))

#--------------------- Тест 2 -------------------------------
# driver.get("https://practice.automationtesting.in/")
# #2
# acc = driver.find_element(By.CSS_SELECTOR, "#menu-item-50 a")
# acc.click()
# login_mail = driver.find_element(By.ID, "username")
# login_mail.send_keys("avfk@mail.ru")
# login_pass = driver.find_element(By.ID, "password")
# login_pass.send_keys("ASTON8j/hr5a-")
# #3
# shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a")
# shop_btn.click()
# #4
# html_cat = driver.find_element(By.CSS_SELECTOR, ".product-categories>li:nth-child(2) a")
# html_cat.click()
# #5
# product_count = driver.find_elements(By.CLASS_NAME, "woocommerce-LoopProduct-link")
# if len(product_count) == 3:
#     print("На странице 3 товара")
# else:
#     print("Ошибка, на странице " + str(len(product_count)) + " товаров")
#------------------------------------Тест 3-----------------------------------
# driver.get("https://practice.automationtesting.in/")
# #2
# acc = driver.find_element(By.CSS_SELECTOR, "#menu-item-50 a")
# acc.click()
# login_mail = driver.find_element(By.ID, "username")
# login_mail.send_keys("avfk@mail.ru")
# login_pass = driver.find_element(By.ID, "password")
# login_pass.send_keys("ASTON8j/hr5a-")
# #3
# shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a")
# shop_btn.click()
# #4
# sort = driver.find_element(By.NAME, "orderby")
# sort_value = sort.get_attribute("value")
# if sort_value == "menu_order":
#     print("Выбрана сортировка по умолчанию")
# else:
#     print("Выбран другой вариант")
# #5
# select = Select(sort)
# select.select_by_index(5)
# #6
# sort = driver.find_element(By.NAME, "orderby")
# sort_value = sort.get_attribute("value")
# if sort_value == "price-desc":
#     print("Выбрана сортировка по убыванию")
# else:
#     print("Выбран другой вариант")
#----------------------------------Тест 4-------------------------------------
#1
# driver.get("https://practice.automationtesting.in/")
# #2
# acc = driver.find_element(By.CSS_SELECTOR, "#menu-item-50 a")
# acc.click()
# login_mail = driver.find_element(By.ID, "username")
# login_mail.send_keys("avfk@mail.ru")
# login_pass = driver.find_element(By.ID, "password")
# login_pass.send_keys("ASTON8j/hr5a-")
# #3
# shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a")
# shop_btn.click()
# #4
# book_android = driver.find_element(By.CSS_SELECTOR, ".post-169 .woocommerce-LoopProduct-link")
# book_android.click()
# #5
# old_cost = driver.find_element(By.CSS_SELECTOR, ".product_cat-android del>span")
# old_cost_text = old_cost.text
# assert old_cost_text == "₹600.00"
# #6
# new_cost = driver.find_element(By.CSS_SELECTOR, ".product_cat-android ins")
# new_cost_text = new_cost.text
# assert new_cost_text == "₹450.00"
# #7
# driver.implicitly_wait(10)
# view_img = driver.find_element(By.CSS_SELECTOR, "#content .images>a")
# view_img.click()
# #8
# driver.implicitly_wait(10)
# close_btn = driver.find_element(By.CLASS_NAME, "pp_close")
# close_btn.click()
#--------------------------------------------Тест5--------------------------------
# #1
# driver.get("https://practice.automationtesting.in/")
# #2
# shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a")
# shop_btn.click()
# #3
# add_basket = driver.find_element(By.CSS_SELECTOR, ".products.masonry-done li:nth-child(6)>a:nth-child(2)")
# add_basket.click()
# time.sleep(5)
# #4
# basket_cont = driver.find_element(By.CLASS_NAME, "cartcontents")
# basket_cont_text = basket_cont.text
# assert basket_cont_text == "1 Item"
# basket_cost = driver.find_element(By.CSS_SELECTOR, "#wpmenucartli .amount")
# basket_cost_text = basket_cost.text
# assert basket_cost_text == "₹350.00"
# #5
# cart_btn = driver.find_element(By.CSS_SELECTOR, "#wpmenucartli>a")
# cart_btn.click()
# #6
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .amount"), "₹350.00"))
# #7
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .amount"), "₹357.00"))

#1
driver.get("https://practice.automationtesting.in/")
#2
shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a")
shop_btn.click()
#3
add_basket = driver.find_element(By.CSS_SELECTOR, ".products.masonry-done li:nth-child(6)>a:nth-child(2)")
add_basket.click()
time.sleep(5)
cart_btn = driver.find_element(By.CSS_SELECTOR, "#wpmenucartli>a")
cart_btn.click()
proceed = driver.find_element(By.CSS_SELECTOR, ".wc-proceed-to-checkout>a")
driver.implicitly_wait(10)
proceed.click()
first_name = driver.find_element(By.ID, "billing_first_name")
first_name.send_keys("Denis")
last_name = driver.find_element(By.ID, "billing_last_name")
last_name.send_keys("Lopez")
email_order = driver.find_element(By.ID, "billing_email")
email_order.send_keys("avfk@mail.ru")
phone_order = driver.find_element(By.ID, "billing_phone")
phone_order.send_keys("89277777777")
country_select = driver.find_element(By.ID, "s2id_billing_country")
country_select.click()
country = driver.find_element(By.ID, "s2id_autogen1_search")
country.click()
country.send_keys("Russia")
rus_check = driver.find_element(By.CLASS_NAME, "select2-match")
rus_check.click()
adress_order = driver.find_element(By.ID, "billing_address_1")
adress_order.send_keys("Kuznetsova")
city_order = driver.find_element(By.ID, "billing_city")
city_order.send_keys("Samara")
state_order = driver.find_element(By.ID, "billing_state")
state_order.send_keys("Russia")
postcode_order = driver.find_element(By.ID, "billing_postcode")
postcode_order.send_keys("443112")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
payments = driver.find_element(By.CSS_SELECTOR, "#payment>ul>li:nth-child(2) input")
payments.click()
place_order = driver.find_element(By.ID, "place_order")
place_order.click()
order_recieved = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 div.woocommerce p:nth-child(1)"), "Thank you. Your order has been received."))
order_pay = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3) td"), "Check Payments"))