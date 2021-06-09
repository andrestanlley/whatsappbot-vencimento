from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from time import sleep

options = Options()
options.headless = False
perfil = FirefoxProfile('C:\\Users\\André\\AppData\\Roaming\\Mozilla\\Firefox\Profiles\\nhxkat9x.default-release')
browser = webdriver.Firefox(firefox_profile=perfil, options=options)
browser.get('https://web.whatsapp.com')
sleep(5)
browser.save_screenshot('login.png')
