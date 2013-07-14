#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import urllib
import time
from threading import Thread
from sqlAdapter import getData
from sqlAdapter import getConfig
from sqlAdapter import performQuery
from standartFunction.parserCommand import getListParameters


config={
		'urlToRchan':"http://b.rchan.ws"
		}

class rchanPlugin(object):
	"""docstring for rchanPlugin"""
	def __init__(self, arg):
		testMysql()
		startBody(bot)

	def testMysql():
		"""проверяем есть ли таблица с пользователями и постами и если нет создаём"""
		try:
			if getData(u"SHOW TABLES LIKE 'usersReadPost'")==():
				logging.debug(u"пора выполнить запрос на создание таблицы ")
				performQuery(u"CREATE TABLE `usersReadPost` (`id` INT(11) NOT NULL AUTO_INCREMENT, `user` CHAR(30) NOT NULL, `posts` INT(11) NOT NULL, PRIMARY KEY(`id`))")
				performQuery("ALTER TABLE usersReadPost CONVERT TO CHARACTER SET utf8 COLLATE     utf8_general_ci;")#конвертнет таблицу в нужную кодировку 
			return True
		except Exception, e:
			logging.warning(e)
			return False

	def updateRecord(user,posts):
		"""обновляем количество постов для пользователя"""
		performQuery("UPDATE  `emi`.`usersReadPost` SET  `posts` =  \'"+str(posts)+"\' WHERE  `usersReadPost`.`user` =\'"+user+"\';")

	def addUser(user):
		"""добавляем нового пользователя"""
		if getData(u"select * from `emi`.`usersReadPost` where `usersReadPost`.`user`=\'"+user+u"\' ;")!=():
			return
		posts=getPosts()
		performQuery("INSERT INTO `usersReadPost` (`user`, `posts`) VALUES (\'"+user+"\', \'"+str(posts)+"\');")

	def getPosts():
		"""получаем количество постов на бороде способ не очень но апи то нет (( и в базу нас не пускают (("""
		define=urllib.urlopen(config['urlToRchan'])
		stringOfPost=define.read()
		#print(stringOfPost)
		stringOfPost1=stringOfPost[stringOfPost.find("Всего постов: ")+len("Всего постов: "):]
		#print(stringOfPost1)
		posts=stringOfPost1[:stringOfPost1.find("</li>")]
		#print(posts)
		postINint=posts.replace(",","")
		logging.debug(u"получили количество постов ")
		logging.debug(postINint)
		return int(postINint)

	def body(bot):
		"""тело потока проверяющего количество постов и сигнализирующего об этом """
		while True:
			posts=getPosts()
			usersAndPosts=getData("select user , posts from usersReadPost")
			for userAndPost in usersAndPosts:
				if posts!=userAndPost[1]:
					updateRecord(userAndPost[0], posts)
					bot.sendMessage(userAndPost[0],u"на бороде опять ктото разбушевался")
			time.sleep(60*10)
		pass

	def removeUser(user):
		"""удаление пользователя"""
		performQuery("DELETE FROM `usersReadPost` WHERE `user`=\'"+user+"\' ;")

	def startBody(bot):
		"""запуск потока проверки постов"""
		thread = Thread(target=body,args=(bot,))
		thread.start()
		pass

	def accessLevel():
		return 1000

	def run(bot,user,message):
		params=getListParameters(message)
		if params[0]==u"add":
			addUser(unicode(user.getNode().decode('utf-8'))+u"@"+unicode(user.getDomain().decode('utf-8')))
			bot.sendMessage(user,u"добавление прошло успешно ))")
		elif params[0]==u"get":
			bot.sendMessage(user,str(getPosts()) )
		elif params[0]==u"remove":
			removeUser(unicode(user.getNode().decode('utf-8'))+u"@"+unicode(user.getDomain().decode('utf-8')))
			bot.sendMessage(user,u"больше не буду слать обновления с рчана бака")
		else:
			bot.sendMessage(user,u"что ты от меня хочешь?")

 