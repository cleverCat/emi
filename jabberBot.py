#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	import xmpp,sys
	import socket
	import threading
	import logging
	import time
	from xmpp import *
	try:
		import thread
	except ImportError:
		import _thread as thread
	import time
except ImportError:
	pass
from pluginsManager import loadBotPlugins
from pluginsManager import runPlugin

class TJabberBot: 
	""" класс бота"""
	def __init__(self, user,server,port, password):
		self._jid = xmpp.protocol.JID(user)
		self.user=user
		self.server=server
		self.port=port
		self.password =password
		self.connect()
		self.auth()

	def connect(self): 
		"""функция подключения к серверу"""
		logging.debug(u"connect to server"+self.server)
		self.conn = xmpp.Client(self._jid.getDomain(), debug = [])#proxy=':3128'
		conn_result = self.conn.connect(server=(self.server,self.port))
		if not conn_result:
			logging.critical( u"Can't connect to server!\n" )
			sys.exit(1)
		logging.debug(u"connect try server "+self.server+"на порту "+str(self.port))

	def auth(self):
		"""аутентификация"""
		logging.debug(u"authorize")
		authResult=self.conn.auth(self._jid.getNode(), str(self.password),'bot')
		if not authResult:
			logging.critical( u"Can't to authorize!\n")
			sys.exit(1)

	def registerHandler(self, name, handler): 
		"""привязка функций к событиям"""
		self.conn.RegisterHandler(name, handler)


	def sendMessage(self,user,message):
		"""отправляем сообщение """
		message=xmpp.Message(user, message)
		message.setAttr('type','chat')
		self.conn.send(message)

	def runCommand(self,user,command,message):
		"""проверяем есть ли у нас такая комманда, возможно в будущем стоит добавить проверку можем ли мы выполнить эту комманду"""
		if command in self.plugins:
			logging.debug(u"!!!! trying to run the command"+command)
			runPlugin(command,self,user,message)
			logging.debug(u"!!!! command will fulfilled")
		else:
			#self.sendMessage(user,"не удалось найти комманду")
			runPlugin("emi",self,user,message)

	def getMessage(self,user,message):#получаем сообщение и запускаем плагин если он есть )
		try:
			if message.find(" ")==-1:
				self.runCommand(user,message,"")
			else:
				command=message[:message.find(" ")]
				message=message[message.find(" ")+1:]
				self.runCommand(user,command,message)
		except:
			self.sendMessage(user,"command will fall during the execution of")
		


	def stepOn(self):
		try:
			self.conn.Process(1)
			time.sleep(1)
		except KeyboardInterrupt:
			return False
		return True

	def start(self):
		"""запускаем бота"""
		self.conn.sendInitPresence(requestRoster=1)
		self.plugins = loadBotPlugins(self)
		logging.debug(u"Bot started!")
		while self.stepOn():
			pass
		logging.debug(u"Bot down")
