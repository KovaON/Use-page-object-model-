from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(link)
    botton = browser.find_element(By.CSS_SELECTOR,'.btn.btn-lg.btn-primary.btn-add-to-basket').text
    assert botton == 'Добавить в корзину', 'Ошибка'


