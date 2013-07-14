#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from security import getAccess
from threading import Thread 
import logging


def getInstanseClass(typeObject,bot):
	return typeObject(bot)


def loadBotPlugins(bot):
	"""загружаем плагины бота из папочки с плагинами"""
	import os
	plugins=dict()
	for fileName in os.listdir('plugins/'):
		if fileName.endswith('.py'):#выбираем только файлы с расширением py
			pluginName = fileName[:-3]#убираем расширение файла
			if pluginName != '__init__':# игнорируем файл __init__.py
				pluginModules=__import__('plugins.'+pluginName)
				plugin = getattr(pluginModules,pluginName)
				pluginType=getattr(plugin,pluginName)
				objectPlugin=getInstanseClass(pluginType,bot)
				plugins.update([(pluginName,objectPlugin),])
	return plugins# возвращаем загруженные плагины 
	

def runPlugin(command,bot,user,message):
	"""запускаем комманду из плагинов"""
	if getAccess(command,bot,user,message)==True:
		logging.debug(u"ищем плагин"+command)
		plugin = bot.plugins[command]
		logging.debug(u"получили плагин")
		thread = Thread(target=plugin.run,args=(bot,user,message))
		thread.start()
		logging.debug(u"выполнили плагин")
	else:
		bot.sendMessage(user,"ололо не для тебя эта комманда писалась")