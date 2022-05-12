from selenium import webdriver
import time

while(True) :
    search = input('search nama terlebih dahulu?(y/n) : ')
    if (search == 'y' or search == 'n') : break
    else : print('jawaban tidak valid')

nama = input('masukkan nama yang ingin di spam : ')
message = input('pesan apa yang ingin di kirim : ')
howMuch = int(input('spam berapa banyak : '))

driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
driver.implicitly_wait(15)
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
if (search == 'y') : driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(nama)
driver.find_element_by_css_selector("span[title='" + nama + "']").click()
for _ in range(howMuch) :
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(message)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()

time.sleep(60)
driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span').click()
driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]/div[1]').click()
time.sleep(3)
driver.quit()
