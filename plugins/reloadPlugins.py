#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from pluginsManager import loadBotPlugins
from pluginsManager import runPlugin

class reloadPlugins(object):
	"""перезагружает плагины"""
	def __init__(self, bot):
		super(reloadPlugins, self).__init__()

	def accessLevel():
		return 0

	def run(bot,user,message):
		logging.debug(u"перезагружаем плагины")
		bot.plugins = loadBotPlugins(bot)
		bot.sendMessage(user,"перезагрузили плагины")

	def help():
		return "перезагружает плагины"
