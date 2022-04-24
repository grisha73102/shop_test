# Shop: отображение страницы товара
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('greg@yandex.ru')
log_password = driver.find_element_by_id('password')
log_password.send_keys('QwErTy!23$%6&qw')
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()
html5 = driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]')
html5.click()
title = driver.find_element_by_class_name('product_title')
title_text = title.text
assert title_text == 'HTML5 Forms'
driver.quit()


# Shop: количество товаров в категории
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('greg@yandex.ru')
log_password = driver.find_element_by_id('password')
log_password.send_keys('QwErTy!23$%6&qw')
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()
html_category = driver.find_element_by_css_selector('.cat-item.cat-item-19>a')
html_category.click()
books_count = driver.find_elements_by_class_name('product')
if len(books_count) == 3:
    print("В списке 3 книги")
else:
    print("Ошибка. Количество товаров в списке: " + str(len(books_count)))
driver.quit()


# Shop: сортировка товаров
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('greg@yandex.ru')
log_password = driver.find_element_by_id('password')
log_password.send_keys('QwErTy!23$%6&qw')
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()
filter = driver.find_element_by_class_name('orderby')
filter_default = filter.get_attribute('value')
assert filter_default == 'menu_order'
select = Select(filter)
select.select_by_value('price-desc')
filter_two = driver.find_element_by_class_name('orderby')
filter_two_default = filter_two.get_attribute('value')
assert filter_two_default == 'price-desc'

driver.quit()


# Shop: отображение, скидка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('greg@yandex.ru')
log_password = driver.find_element_by_id('password')
log_password.send_keys('QwErTy!23$%6&qw')
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()
android = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
android.click()
old_price = driver.find_element_by_css_selector('del>.woocommerce-Price-amount.amount')
old_price_text = old_price.text
assert old_price_text == '₹600.00'
new_price = driver.find_element_by_css_selector('ins>.woocommerce-Price-amount.amount')
new_price_text = new_price.text
assert new_price_text == '₹450.00'
wait = WebDriverWait(driver, 10)
foto_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div>a>img.attachment-shop_single')))
foto_btn.click()
close_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
close_btn.click()

driver.quit()


# Shop: проверка цены в корзине
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_id('menu-item-40')
shop.click()
book_add = driver.find_element_by_css_selector('.post-182>.button')
book_add.click()
time.sleep(2)
item = driver.find_element_by_class_name('cartcontents')
item_text = item.text
assert item_text == '1 Item'
price = driver.find_element_by_class_name('amount')
price_text = price.text
assert price_text == '₹180.00'
cart = driver.find_element_by_class_name('wpmenucart-contents')
cart.click()
wait = WebDriverWait(driver, 10)
subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal .woocommerce-Price-amount'), '₹180.00'))
total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total .woocommerce-Price-amount'), '₹189.00'))

driver.quit()


# Shop: работа в корзине
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
book_html_add = driver.find_element_by_css_selector('.post-182>.button')
book_html_add.click()
time.sleep(2)
book_js_add = driver.find_element_by_css_selector('.post-180>.button')
book_js_add.click()
cart = driver.find_element_by_class_name('wpmenucart-contents')
cart.click()
time.sleep(2)
remove_btn = driver.find_element_by_css_selector('.shop_table .cart_item:nth-child(1) .remove')
remove_btn.click()
undo_btn = driver.find_element_by_css_selector('.woocommerce-message>a')
undo_btn.click()
quantity_js = driver.find_element_by_css_selector('.shop_table .cart_item:nth-child(1) input')
quantity_js.clear()
quantity_js.send_keys('3')
update_cart = driver.find_element_by_css_selector('[name="update_cart"]')
quantity_js_value = quantity_js.get_attribute('value')
assert quantity_js_value == '3'
time.sleep(2)
apply_coupon = driver.find_element_by_css_selector('[name="apply_coupon"]')
apply_coupon.click()
error = driver.find_element_by_css_selector('.woocommerce-error>li')
error_text = error.text
assert error_text == 'Please enter a coupon code.'

driver.quit()


# Shop: покупка товара
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
book_html_add = driver.find_element_by_css_selector('.post-182>.button')
book_html_add.click()
time.sleep(2)
cart = driver.find_element_by_class_name('wpmenucart-contents')
cart.click()
wait = WebDriverWait(driver, 10)
checkout_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button')))
checkout_btn.click()
first_name = wait.until(EC.element_to_be_clickable((By.ID, 'billing_first_name')))
first_name.send_keys('greg')
last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('grog')
email = driver.find_element_by_id('billing_email')
email.send_keys('greg@yandex.ru')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('9999999999')
country_select = driver.find_element_by_id('s2id_billing_country')
country_select.click()
country_input = driver.find_element_by_id('s2id_autogen1_search')
country_input.send_keys('Russia')
country_select_two = driver.find_element_by_id('select2-results-1')
country_select_two.click()
address = driver.find_element_by_id('billing_address_1')
address.send_keys('ul')
city = driver.find_element_by_id('billing_city')
city.send_keys('Moscow')
state = driver.find_element_by_id('billing_state')
state.send_keys('Moscow obl')
postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('123456')
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
check_payments = driver.find_element_by_id('payment_method_cheque')
check_payments.click()
place_order = driver.find_element_by_id('place_order')
place_order.click()
order = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
payment_method = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.method>strong'), 'Check Payments'))

driver.quit()