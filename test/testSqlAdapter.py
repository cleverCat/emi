#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
from sqlAdapter import getData
from sqlAdapter import getConfig
from sqlAdapter import performQuery


def testSqlAdapter():
	print getConfig()
	print "testSqlAdapter"

def startTest():
	#ko=u"INSERT INTO usersAccessLevel (name,accessLevel) values ('игорь_борщевский@rubserv','0');"
	#performQuery(ko)
	try:
		testSqlAdapter()
		getData(u"SHOW TABLES LIKE 'usersAccessLevel'")==()
	except:
		return False
	return True