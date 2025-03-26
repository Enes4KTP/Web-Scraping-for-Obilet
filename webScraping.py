from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Tarayıcıyı başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Webscraping yapmak istediğiniz url'i giriniz.
url = 'https://www.obilet.com/seferler/'

while True:
    driver.get(url)
    
    time.sleep(5)
    
    #Seferlerin olduğu bölüm
    seferler = driver.find_elements(By.CLASS_NAME, 'journey')
    
    for sefer in seferler:
        saat = sefer.find_element(By.CLASS_NAME, 'departure').text # Seferin saati
        koltuk_durumu = sefer.find_element(By.CLASS_NAME, 'text').text # Seferin koltuk durumu

        if saat >= '15:30': # Örnek olarak 15:30'dan sonraki seferleri kontrol eder.
            if 'Sefer Dolu' not in koltuk_durumu:
                print(f'{saat} saatindeki seferde boş yer mevcut!') #
    
    time.sleep(120) # 60 x 2 -> 2 dakika bekleme süresi

driver.quit()
