from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class InstaBot:
    def __init__(self, username, pw):
        mobile_emulation = { "deviceName": "Nexus 5" }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument ("lang = en_us")
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.driver = webdriver.Chrome(executable_path=r"D:\Dev apps\chromedriver_win32\chromedriver.exe",chrome_options = chrome_options)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Log In')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        finally:
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]").click()
            sleep(2)
            self.driver.find_element_by_xpath('//*[name()="svg" and @aria-label="Direct"]').click()
            sleep(3)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(2)
            self.driver.find_element_by_xpath('//*[name()="svg" and @aria-label="Back"]').click()

    def openDM(self,name):
        self.driver.find_element_by_xpath("//span[@aria-label=\"Search & Explore\"]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]").send_keys(name)
        sleep(4)
        self.driver.find_element_by_xpath("//li").click()
        sleep(10)
        self.driver.find_element_by_xpath("//button[contains(text(), \"Message\")]").click()
        sleep(2)        
    
    def closeDM(self):
        self.driver.find_element_by_xpath('//*[name()="svg" and @aria-label="Back"]').click()
    
    def sendDM(self, message):
        self.driver.find_element_by_xpath("//textarea[@placeholder=\"Message...\"]").send_keys(message)
        self.driver.find_element_by_xpath("//button[contains(text(), \"Send\")]").click()
        sleep(1)

my_bot = InstaBot('user-name', 'password')
my_bot.openDM('recievers-name')
my_bot.sendDM('message')
my_bot.closeDM()
