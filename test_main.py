import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    chrome_browser = webdriver.Remote(command_executor='http://browser:4444', options=options)
    # chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(5)
    chrome_browser.maximize_window()
    return chrome_browser


def test_message(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    message = driver.find_element(By.XPATH, '//*[text()="Default welcome msg!"]')
    assert message.is_displayed()


def test_add_to_cart(driver):
    driver.get('https://magento.softwaretestingboard.com/proteus-fitness-jackshirt.html')
    driver.find_element(By.ID, 'option-label-size-143-item-166').click()
    driver.find_element(By.ID, 'option-label-color-93-item-49').click()
    driver.find_element(By.ID, 'product-addtocart-button').click()
    counter = driver.find_element(By.XPATH, '//*[@class="action showcart"]//span[contains(@class,"counter ")]')
    wait = WebDriverWait(driver, 5)
    wait.until_not(
        EC.text_to_be_present_in_element_attribute(
            (By.XPATH, '//*[@class="action showcart"]//span[contains(@class,"counter ")]'),
            'class',
            '_block-content-loading'
        )
    )
    assert counter.text.startswith('1')

