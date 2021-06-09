import logging
import time
import pyautogui as key
from SapGuiLibrary import SapGuiLibrary

import Utilities.Logfile as cl
import subprocess

from Base.BaseClass import BaseClass
from Configuration.config import ConfigData

sapGui = SapGuiLibrary()


class SAPActionClass(BaseClass):
    '''
            @method name: inputText
            @author: SESA548418
            @description: This method is used to enter text to the text field
    '''

    def inputText(self, by_locator, text):
        sapGui.input_text(by_locator, text)
