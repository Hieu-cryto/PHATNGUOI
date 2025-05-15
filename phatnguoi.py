from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image
import pytesseract
from io import BytesIO
import schedule

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"   

def PHATNGUOI():
    driver = webdriver.Chrome()
    try
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
    click_bien_kiem_soat = '#formBSX > div.bot > div:nth-child(1) > input'    
    element_bien_kiem_soat= driver.find_element(By.CSS_SELECTOR, click_bien_kiem_soat)
    element_bien_kiem_soat.send_keys("74F168459")

    click_phuong_tien = '#formBSX > div.bot > div:nth-child(2) > select > option:nth-child(1)'    
    element_phuong_tien = driver.find_element(By.CSS_SELECTOR, click_phuong_tien)
    element_phuong_tien.click()

    capcha_element = driver.find_element(By.CSS_SELECTOR, '#imgCaptcha')
    capcha_png = capcha_element.screenshot_as_png

    image = Image.open(BytesIO(capcha_png))

    capcha_text = pytesseract.image_to_string(image, config='--psm 8').strip()
    new_text1 = capcha_text[1:]
    new_text2 = new_text1.replace(" ", "")
      
    time.sleep(2)
    click_bien_kiem_soat = '#formBSX > div.bot > div:nth-child(3) > div > input'    
    element_bien_kiem_soat= driver.find_element(By.CSS_SELECTOR, click_bien_kiem_soat)
    element_bien_kiem_soat.send_keys(new_text2)
    time.sleep(2)
    click_xe = '#formBSX > div.bot > input.btnTraCuu'    
    element_xe = driver.find_element(By.CSS_SELECTOR, click_xe)
    element_xe.click()
    finally:
    driver.quit()

schedule.every().day.at("06:00").do(PHATNGUOI)
schedule.every().day.at("12:00").do(PHATNGUOI)

print('Đang thực hiện ...')

while True:
    schedule.run_pending()
    time.sleep(1)  
#mạng chậm dễ bị lỗi á thầy

