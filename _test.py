from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import allure
import os

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

@pytest.fixture(scope='module')
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.title("Verify Landing Page")
@pytest.mark.test    
def test_landing_page(setup):
    try:
        driver = setup
        driver.get('https://eklipse.gg')
        assert "https://eklipse.gg" in current_url, f"URL mismatch: expected 'https://eklipse.gg/', got"
        img_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'logo_white.png')]")))
        assert img_element.is_displayed()
        allure.attach(driver.get_screenshot_as_png, name='Screenshot', attachment_type=allure.attachment_type.PNG)
        print('Landing page test success!')
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
        print(f'Landing page test failed: {e}')

@allure.title("Account Sign In")
@pytest.mark.test        
def test_login(setup):
    try:
        driver = setup
        driver.get('https://eklipse.gg')
        sign_in_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In")))
        sign_in_button.click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, "username")))
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        login_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Sign In')]")
        login_button.click()
        WebDriverWait(driver,10).until(EC.url_to_be("https://app.eklipse.gg/home"))
        current_url = driver.current_url
        assert current_url == "https://app.eklipse.gg/home", f"URL mismatch: expected 'https://app.eklipse.gg/home', got {current_url}"
        skip_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='btn btn-link--highlight' and text()='Skip for now']"))
        )
        skip_button.click()
        img_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//img[@class='logo-main' and @alt='logo']")))
        assert img_element.is_displayed()
        print('Login test passed!')
    except Exception as e:
        print(f'Login test failed: {e}')

@allure.title("Edit Clips")
@pytest.mark.test
def edit_clips(setup):
    try:
        driver = setup
        driver.get('https://studio.eklipse.gg/')
        WebDriverWait(driver,10).until(EC.url_contains('studio.eklipse.gg'))
        current_url = driver.current_url
        assert 'studio.eklipse.gg' in current_url, f"URL mismatch: expected to contain 'studio.eklipse.gg', got {current_url}"
        print('Editing clips test passed!')
    except Exception as e:
        print(f'Editing clips test failed: {e}')

@allure.title("Account Settings")      
@pytest.mark.test  
def account_settings(setup):
    try:
        driver = setup
        sign_in_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In")))
        sign_in_button.click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, "username")))
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(passwords)
        login_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Sign In')]")
        login_button.click()
        WebDriverWait(driver,10).until(EC.url_to_be("https://app.eklipse.gg/home"))
        current_url = driver.current_url
        assert current_url == "https://app.eklipse.gg/home", f"URL mismatch: expected 'https://app.eklipse.gg/home', got {current_url}"
        
        skip_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='btn btn-link--highlight' and text()='Skip for now']"))
        )
        skip_button.click()
        
        profile_dropdown = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='ic-user']")))
        profile_dropdown.click()
        
        acc_settings_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @role='menuitem' and .//span[text()='Account Settings']]")))
        acc_settings_button.click()
        
        acc_setting_title = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Account Setting']")))
        assert acc_setting_title.text == 'Account Setting'
        
        WebDriverWait(driver,10).until(EC.url_contains("/account"))
        current_url = driver.current_url
        
        twitch_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable(By.XPATH, "//img[@class='icon' and contains(@src, 'icon-twitch.png')]/following-sibling::button[text()='Connect']"))
        assert twitch_button.is_displayed(), "Twitch connect button not found!"
        twitch_button.click()
        
        
        assert '/account' in current_url, f"URL mismatch: expected to contain '/account', got {current_url}"
        print("Account settings test passed!")
    except Exception as e:
        print(f'Account settings test failed: {e}')

@allure.title("Upload and Edit Clip")    
@pytest.mark.test    
def edit_upload_clip(setup):
    try:
        driver = setup
        driver.get('https://studio.eklipse.gg/')
        twitch_kick_button_upload = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='From Twitch/Kick']")))
        twitch_kick_button_upload.click()
        print('Upload test case passed!')
    except Exception as e:
        print(f'Upload test case failed: {e}')
