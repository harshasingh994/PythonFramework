import pytest
from Base.BaseClass import BaseClass
from Pages.SAP_Page import SAP_Page
from Pages.HomePage import HomePage
from Pages.Web_Page import Web_Page
from Utilities.ExcelUtility import ExcelUtility


class TestOne:

    def test_workFlow(self, getData):
        SAPpage = SAP_Page()
        SAPpage.launchGUI()
        SAPpage.SAPFuntions(getData["UserName"], getData["Password"])

    '''
       web_page = Web_Page(self.driver)
       web_page.launchWebURL()
       web_page.webFunctions(getData["Web_User"], getData["Web_Pass"])
    '''

    # homepage = HomePage(self.driver)

    # homepage.enterName(getData["Firstname"])

    #  homepage.enterEmail(getData["Email"])
    #  homepage.enterGender(getData["Gender"])
    #  homepage.clickOnSubmit()
    #  homepage.verifySuccessMessage()
    # homepage.clickOnCheckbox()

    @pytest.fixture(params=ExcelUtility.getTestData("TestOne"))
    def getData(self, request):
        return request.param
