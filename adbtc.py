from selenium import webdriver
import time

driver = webdriver.Chrome()
email='your_email'
senha='your_password'

driver.get("https://adbtc.top/index/enter/")
time.sleep(30) #30s for you solve hCaptcha
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('password').send_keys(senha)
driver.find_element_by_css_selector('.btn.light-blue.darken-4').click()
time.sleep(10)
driver.get("https://adbtc.top/surf/rotator")
time.sleep(45) #45s for you solve hCaptcha
while True:
    try:
        driver.find_element_by_css_selector('.pulse.animated.valign-wrapper.btn').click()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        str1=str(driver.title)
        print(str1)
        tempo=str1.split()
        tempo=int(tempo[0])+10
        #print(tempo)
        time.sleep(tempo)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except:
        print("Please solve the captchar! Or something is wrong...")
        time.sleep(10)
