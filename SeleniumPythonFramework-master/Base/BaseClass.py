import logging
import time

import Utilities.Logfile as cl
import pytest
import subprocess
from Configuration.config import ConfigData
from SapGuiLibrary import SapGuiLibrary

driver = None


@pytest.mark.usefixtures('setup')
class BaseClass:
    def launchWebURL(self):
        self.driver.get(ConfigData.Base_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
