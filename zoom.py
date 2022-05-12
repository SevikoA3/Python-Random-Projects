from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
import time

jam = input('jam berapa zoom dimulai? (HH:MM)\n')
lama = float(input('berapa lama zoom dilaksanakan dalam menit?\n'))
loading = ['|', '/', '-', '\\']
element = 0
while (True) :
    if (datetime.now().strftime('%H:%M') == jam) :
        break
    else :
        pass
    time.sleep(0.25)
    os.system('cls')
    if (element > 3) : element = 0
    print('menunggu sampai', jam, loading[element])
    element += 1

os.system('cls')
option = Options()
option.add_argument("--use-fake-ui-for-media-stream")
option.add_argument("--use-fake-device-for-media-stream")
driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe', options=option)
driver.maximize_window()
driver.implicitly_wait(15)

driver.get('masukin link zoom (bukan link zoom yang ada pilihan zoom web atau zoom app)')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="mic-btn"]').click()
driver.find_element_by_xpath('//*[@id="video-btn"]').click()
driver.find_element_by_xpath('//*[@id="inputname"]').send_keys('masukin nama')
driver.find_element_by_xpath('//*[@id="joinBtn"]').click()
driver.find_element_by_xpath('//*[@id="inputpasscode"]').send_keys('masukin password')
driver.find_element_by_xpath('//*[@id="joinBtn"]').click()

time.sleep(lama*60)
driver.quit()