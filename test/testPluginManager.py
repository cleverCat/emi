#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pluginsManager import loadBotPlugins
from pluginsManager import runPlugin
from jabberBot import *
import logging

def startTest():
	try:
		bot = TJabberBot('sotona@jabberes.org','jabberes.org',5222,'aqre13mstrfajk')
		loadBotPlugins(bot)
		runPlugin('emi',bot,'sotona@jabberes.org','hello')
	except Exception, e:
		print("testPluginManager")
		logging.warning(e)
		return False
	return True