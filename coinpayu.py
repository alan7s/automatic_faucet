from selenium import webdriver
import time

driver = webdriver.Chrome()
email='your_email'
senha='your_password'

driver.get("https://coinpayu.com/login")
print("loading page...")
time.sleep(10) #change value if block by cloudflare
driver.find_element_by_css_selector(".btn-info.jzy-btn").click()
print("30s for you solve the captchar!")
time.sleep(30) #30s for you solve QbkRecaptcha
driver.find_element_by_css_selector("input.form-control[type=email]").send_keys(email)
driver.find_element_by_css_selector("input.form-control[type=password]").send_keys(senha)
driver.find_element_by_css_selector('.btn-info.jzy-btn').click()
time.sleep(5)
driver.get("https://coinpayu.com/dashboard/ads_surf")
time.sleep(10)
print("10s to load page")
elements=[]
try:
    elements = driver.find_elements_by_css_selector('.col-12.text-overflow.ags-description.pull-left')
    i = len(elements) - 1
    while i >= 0:
        elements[i].click()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(45)
        try:
            teste = driver.find_element_by_css_selector('.recaptcha-style')
            print("20s for you solve the captchar")
            time.sleep(20)
        except:
            print("captchar not found, next ad")
        #    if driver.find_element_by_css_selector('.recaptcha-style'):
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        i -= 1
except:
    print("Something is wrong...")