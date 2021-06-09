import logging
import time

import pyautogui as key
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

import Utilities.Logfile as cl
from Base.BaseClass import driver
from Configuration.config import ConfigData

from Utilities.WebActionClass import CommonUtility


class Web_Page(CommonUtility):
    log = cl.customLogger(logging.DEBUG)
    userName = (By.ID, 'j_username')
    passWord = (By.ID, 'j_password')
    signIn = (By.NAME, 'btnEnter')
    MenuIcon = (By.XPATH, '//*[@id = "phMenu"]')
    ASNLink = (By.XPATH, '//*[@id="MIDP19"]/a')
    ASNSearchBox = (By.XPATH, '//*[@alt = "Find ASN"]')

    def launchWebURL(self):
        self.driver.get(ConfigData.Base_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

    def enterUserName(self, data):
        try:
            self.do_sendKeys(self.userName, data)
            self.log.info("Enter User ID: " + data)
        except:
            print("Timeout exception")

    def enterPassWord(self, data):
        try:
            self.do_sendKeys(self.passWord, data)
            self.log.info("Enter PassWord: " + data)
            self.elementClick(self.signIn)
            time.sleep(6)
        except:
            print("Timeout exception")

    def webFunctions(self, userName, Password):
        asn_value = 1234567890
        self.enterUserName(userName)
        self.enterPassWord(Password)
        self.elementClick(self.MenuIcon)
        self.elementClick(self.MenuIcon)
        # click_on_ASNs
        time.sleep(6)
        self.elementClick(self.ASNLink)
        time.sleep(4)
        # search_ASN():
        self.do_sendKeys(self.ASNSearchBox, asn_value)
        time.sleep(3)
        key.press('enter')
