import logging
import time
import pyautogui as key
from SapGuiLibrary import SapGuiLibrary

import Utilities.Logfile as cl
import subprocess

from Base.BaseClass import BaseClass
from Configuration.config import ConfigData
from Utilities.SAPActionClass import SAPActionClass

sapGui = SapGuiLibrary()


class SAP_Page(SAPActionClass):

    def launchGUI(self):
        subprocess.Popen(ConfigData.sapLogonPath)
        time.sleep(10)
        sapGui.connect_to_session()
        sapGui.open_connection(ConfigData.SAP_ConnectionName)
        time.sleep(3)

    def enterUserName(self, UserName, data):
        try:
            self.inputText("wnd[0]/usr/txtRSYST-BNAME", UserName)
            self.log.info("Enter User Name: " + data)
        except:
            print("")

    def SAPFuntions(self, UserName, Password):
        log = cl.customLogger(logging.DEBUG)
        log.info("Enter GUI user name: " + UserName)
        # sapGui.input_text("wnd[0]/usr/txtRSYST-BNAME", UserName)

        log.info("Enter GUI user name: " + Password)
        sapGui.input_text("wnd[0]/usr/pwdRSYST-BCODE", Password)
        sapGui.send_vkey(0, window=0)
        time.sleep(10)
        sapGui.run_transaction("vl33n")
        key.press('f4')
        time.sleep(5)
        sapGui.input_text(
            "wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/ctxtG_SELFLD_TAB-LOW[1,24]",
            "23.04.2020")
        sapGui.input_text(
            "wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/ctxtG_SELFLD_TAB-LOW[2,24]",
            "2FR00131")
        sapGui.click_element("wnd[1]/tbar[0]/btn[0]")
        time.sleep(3)

        # copy_asn
        asn_value = sapGui.get_value("wnd[1]/usr/lbl[1,4]")
        print(asn_value)
        time.sleep(3)

        # click_enter
        sapGui.click_element("wnd[1]/tbar[0]/btn[0]")
        time.sleep(3)

        # sap_logout
        sapGui.click_element("wnd[0]/mbar/menu[6]")
        time.sleep(3)
        sapGui.click_element("wnd[0]/mbar/menu[6]/menu[12]")
        time.sleep(2)
        sapGui.click_element("wnd[1]/usr/btnSPOP-OPTION1")
