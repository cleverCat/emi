#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmpp
import logging
from sqlAdapter import getData
from sqlAdapter import getConfig
from sqlAdapter import performQuery

def testMysql():
	try:
		if getData(u"SHOW TABLES LIKE 'usersAccessLevel'")==():
			logging.debug(u"пора выполнить запрос на создание таблицы ")
			performQuery(u"CREATE TABLE `usersAccessLevel` (`id` INT(11) NOT NULL AUTO_INCREMENT, `name` CHAR(30) NOT NULL, `accessLevel` SMALLINT(6) NOT NULL, PRIMARY KEY(`id`))")
			performQuery("ALTER TABLE usersAccessLevel CONVERT TO CHARACTER SET utf8 COLLATE     utf8_general_ci;")#конвертнет таблицу в нужную кодировку 
		return True
	except Exception, e:
		logging.warning(e)
	return False


def getAccess(command,bot,user,message):
	"""возвращает можно ли выполнить комманду для этого пользователя"""
	try:
		if testMysql()==False:
			return False
		logging.debug(user.getNode())
		logging.debug(u"формируем запрос")
		query=u"SELECT `accessLevel` FROM `usersAccessLevel` WHERE `name` ='"+unicode(user.getNode().decode('utf-8'))+u"@"+unicode(user.getDomain().decode('utf-8'))+u"';"
		logging.debug(query)
		userLevel=999
		if getData(query)!=():
			userLevel=getData(query)[0][0]
		logging.debug(u"сравниваем уровни доступа")
		logging.debug(int(userLevel))
		logging.debug(int(bot.plugins[command].accessLevel()))
		if int(userLevel)<=int(bot.plugins[command].accessLevel()):
			logging.debug(u"выходим из getAccess")
			return True
		else:
			return False
	except Exception, e:
		logging.warning(e)
		return False