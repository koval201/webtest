from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def perser():
    driver = webdriver.Firefox()
    driver.get("https://drive.google.com/drive/folders/1Bz75IcdiIB-bdmc68ux-v42hlyolup2G?usp=sharing")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="file.txt"]'))
        )
        print("Success!!!")
    finally:
        driver.quit()