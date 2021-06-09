import pytest

import logging

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import Utilities.Logfile as cl
from Configuration.config import ConfigData

'''def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )
'''
driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    log = cl.customLogger(logging.DEBUG)
    browser_name = ConfigData.BrowserName


    if browser_name == "Chrome":
        driver = webdriver.Chrome(executable_path=ConfigData.Chrome_Path)
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        log.info(browser_name + " browser has been launched")
    elif browser_name == "firefox":
        # driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
        driver = webdriver.Firefox(GeckoDriverManager().install())
        log.info(browser_name + " browser has been launched")
    elif browser_name == "IE":
        print("IE driver")

    request.cls.driver = driver
    yield
    # driver.close()
    # log.info(browser_name + " browser has been Closed")

'''
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
 '''