# Registration_login: регистрация аккаунта
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
email = driver.find_element_by_id('reg_email')
email.send_keys('greg@yandex.ru')
password = driver.find_element_by_id('reg_password')
password.send_keys('QwErTy!23$%6&qw')
register = driver.find_element_by_css_selector('[name="register"]')
register.click()
driver.quit()


# Registration_login: логин в систему
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
logout = driver.find_element_by_link_text('Logout')
logout_text = logout.text
assert logout_text == 'Logout'
driver.quit()


