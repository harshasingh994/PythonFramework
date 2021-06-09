import logging

from selenium.webdriver.common.by import By
from Utilities.WebActionClass import WebActionClass
import Utilities.Logfile as cl


class HomePage(WebActionClass):
    log = cl.customLogger(logging.DEBUG)
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    nameTextField = (By.XPATH, "//*[contains(@class, 'form-control')][@name='name']")
    emailTextField = (By.NAME, "email")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    checkbox = (By.ID, "exampleCheck1")

    def enterName(self, data):
        try:
            self.do_sendKeys(self.nameTextField, data)
            self.log.info("Enter first Name: " + data)
        except:
            print("")

    def enterEmail(self, data):
        self.do_sendKeys(self.emailTextField, data)
        self.log.info("Enter Email ID: " + data)

    def enterGender(self, data):
        self.selectOptionByText(self.gender, data)
        self.log.info("Select Gender as: " + data)

    def clickOnSubmit(self):
        self.elementClick(self.submit)
        self.log.info("Click on submit button")

    def verifySuccessMessage(self):
        text = "Success"
        self.verifyText(self.successMessage, text)
        self.log.info("Success message verified")
        self.pageRefresh()

    def clickOnCheckbox(self):
        # self.is_checkbox_selected(self.checkbox)
        self.elementClick(self.checkbox)
        self.is_checkbox_selected(self.checkbox)
        self.log.info("Check box is selected")
