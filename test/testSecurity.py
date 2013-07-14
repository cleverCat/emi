#!/usr/bin/env python
# -*- coding: utf-8 -*-

from security import testMysql
from security import getAccess
from jabberBot import *


def startTest():
	try:
		bot = TJabberBot('sotona@jabberes.org','jabberes.org',5222,'aqre13mstrfajk')
		getAccess('emi',bot,'sotona@jabberes.org','hello')
		return True
	except:
		return False
	return True