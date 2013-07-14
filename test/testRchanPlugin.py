#!/usr/bin/env python
# -*- coding: utf-8 -*-
from plugins.rchanPlugin import *


def startTest():
	try:
		r=rchanPlugin()
		print r.getPosts()
	except Exception, e:
		print("test rchanPlugin") 
		print e
		return False
	return True
