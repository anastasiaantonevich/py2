import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
username = "antonevich+1@uchi.ru"
password = 1234

@pytest.fixture()
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):
    driver.get("https://uchi.ru/")
    driver.find_element_by_id('login').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_class_name('login-form__submit').click()
    button_to_child = driver.find_element_by_link_text('Перейти в аккаунт ученика')
    WebDriverWait(driver,10).until(EC.visibility_of(button_to_child))