#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import logging

configMYsql={
			'host':"localhost",
	 		'user':"emi",
	 		'password':"password",
	 		'db':"emi",
	 		'charset':'utf8'
		}

def getConfig():
	"""получаем конфиги для подключения к бд ))"""
	return configMYsql

def getData(query):
	"""получаем данные из базы"""
	logging.debug(u"подключаемся к базе")
	db = MySQLdb.connect(host=configMYsql['host'], user=configMYsql['user'], passwd=configMYsql['password']
						, db=configMYsql['db'], charset=configMYsql['charset'])
	#logging.debug(u"подключились к базе")
	db.set_character_set('utf8')
	cursor = db.cursor()# формируем курсор
	#logging.debug(u"сформировали курсор")
	cursor.execute("set character_set_client='utf8';")
	cursor.execute("set character_set_results='utf8';")
	cursor.execute("set collation_connection='utf8_general_ci';")
	#cursor.execute("ALTER TABLE usersAccessLevel CONVERT TO CHARACTER SET utf8 COLLATE     utf8_general_ci;")#конвертнет таблицу в нужную кодировку 
	cursor.execute(str(query))# выполняем запрос
	logging.debug(u"выполнили запрос" +query)
	data =  cursor.fetchall()# получаем результат выполнения запроса
	
	db.close()# закрываем соединение с БД
	#logging.debug(u"закрыли соеденение с базой")
	logging.debug(data)
	return data


def performQuery(query):
	"""выполняем запрос """
	db = MySQLdb.connect(host=configMYsql['host'], user=configMYsql['user'], passwd=configMYsql['password']
						, db=configMYsql['db'], charset=configMYsql['charset'])
	db.set_character_set('utf8')
	cursor = db.cursor()# формируем курсор
	cursor.execute("set character_set_client='utf8';")
	cursor.execute("set character_set_results='utf8';")
	cursor.execute("set collation_connection='utf8_general_ci';")
	cursor.execute(query)# исполняем SQL-запрос
	db.commit()# применяем изменения к базе данных
	db.close()# закрываем соединение с базой данных

def perfomQurySupressError(query):
	"""выполняем запрос и давим сообщения об ошибках"""
	try:
		performQuery(query)
		return True
	except:
		return False
