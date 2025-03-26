from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Tarayıcıyı başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://www.obilet.com/seferler/424-356/2025-03-28'

while True:
    driver.get(url)
    
    time.sleep(5)
    
    seferler = driver.find_elements(By.CLASS_NAME, 'journey')
    
    for sefer in seferler:
        saat = sefer.find_element(By.CLASS_NAME, 'departure').text
        koltuk_durumu = sefer.find_element(By.CLASS_NAME, 'text').text

        if saat >= '15:30':
            if 'Sefer Dolu' not in koltuk_durumu:
                print(f'{saat} saatindeki seferde boş yer mevcut!')
    
    time.sleep(120)

driver.quit()
