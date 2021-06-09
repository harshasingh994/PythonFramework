from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Base.BaseClass import BaseClass


class WebActionClass(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    '''
        @method name:verifyLinkPresence
        @author:
        @description:This method is used to verify the presence of link on the page
    '''

    def verifyLinkPresence(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))

    '''
        @method name:elementClick
        @author:
        @description:This method is used to click on web element on the page
    '''

    def elementClick(self, by_locator):
        try:
            WebDriverWait(self.driver, 120).until(EC.visibility_of_element_located(by_locator)).click()
        except:
            print("Test failed while loading page")

    '''
         @method name:do_sendKeys
         @author:
         @:param: text
         @description: This method is used to enter text to the web element on the page
    '''

    def do_sendKeys(self, by_locator, text):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    '''
        @method name:selectOptionByText
        @author:
        @:param: text
        @description:This method is used to select data from the drop down using 'text' attribute
    '''

    def selectOptionByText(self, by_locator, text):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        select = Select(element)
        select.select_by_visible_text(text)

    '''
        @method name:selectOptionByValue
        @author:
        @:param: value
        @description:This method is used to select data from the drop down using 'value' attribute
          '''

    def selectOptionByValue(self, by_locator, value):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        select = Select(element)
        select.select_by_value(value)

    '''
        @method name:selectOptionByIndex
        @author:
        @:param: index
        @description:This method is used to select data from the drop down using 'index' attribute
         '''

    def selectOptionByIndex(self, by_locator, index):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        select = Select(element)
        select.select_by_index(index)

    '''
        @method name:verifyText
        @author:
        @:param: text
        @description:This method is used to verify UI text on the web page
             '''

    def verifyText(self, by_locator, text):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).text
        assert (text in element)

    '''
        @method name:selectFromList
        @author:
        @:param: value
        @description:This method is used to select value from the list element
            '''

    def selectFromList(self, by_locator):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))

    '''
        @method name:pageRefresh
        @author:
        @description:This method is used to refresh the web page
            '''

    def pageRefresh(self):
        self.driver.refresh()

    '''
        @method name:elementDoubleClick
        @author:
        @description:This method is used to double click on the web element using action class
         '''

    def elementDoubleClick(self, by_locator):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(driver)
        action.double_click(element).perform()

    '''
        @method name:mouseHover
        @author:
        @description:This method is used to do mouse hover or mose movement on the web element using action class
         '''

    def mouseHover(self, by_locator):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(driver)
        action.move_to_element(element)

    '''
        @method name:drag_and_drop
        @author:
        @description:This method is used to perform drag and drop of the web element using action class
            '''

    def drag_and_drop(self, by_locator_source, by_locator_target):
        sourceElement = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator_source))
        targetElement = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator_target))
        action = ActionChains(driver)
        action.drag_and_drop(sourceElement, targetElement).perform()

    '''
        @method name:action_click
        @author:
        @description:This method is used to do click on the web element using action class
            '''

    def action_click(self, by_locator):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(driver)
        action.click(element)

    def verify_element_is_checkbox(self, by_locator):

        my_element_type = by_locator.get_attribute('type')

        if my_element_type != 'checkbox':
            raise AssertionError('The passed is not a checkbox')

        return

    """
        Function to check if a checkbox is checked or not.
        It will return 'True' if checked or 'False' if not checked.
        :param element:
        :return: boolean
        """

    def is_checkbox_selected(self, by_locator):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        self.verify_element_is_checkbox(element)
        if element.is_selected():
            return True
        else:
            return False

    """
       Function to assert if a check box is select.
       Will raise an assertion exception if the passed in element is not a check box or it is not checked.
       :param element:
       :return:
       """

    def assert_checkbox_is_selected(self, by_locator):

        self.verify_element_is_checkbox(by_locator)

        if not self.is_checkbox_selected(by_locator):
            raise AssertionError('The element is not selected.')
            return

    """
        Function to verify if the passed in element is enabled. Enabled element is clickable/selectable.
        Raises an assertion exception if the element is not checkbox or is not enabled.
        :param element:
        :return:
        """

    def assert_checkbox_is_enabled(self, by_locator):
        self.verify_element_is_checkbox(by_locator)
        if not by_locator.is_enabled():
            raise AssertionError('The checkbox is not enabled.')

# add description to the methods
# action class
# add to take screen shot
# switch to different window
# switch to alert
# open new window
# check box
# radio button
# javascript executor
# switch to frame
