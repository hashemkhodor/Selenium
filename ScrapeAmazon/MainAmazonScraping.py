# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:29:54 2022

@author: Hashem
"""

from AmazonBot import AmazonBot

Bot1= AmazonBot('C:\SeleniumWebdrivers\chromedriver_win32 (6)\chromedriver.exe')
Bot1.scrapeproduct("sunglasses")
Bot1.exportxlsx()

