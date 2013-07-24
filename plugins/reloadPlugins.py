#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from pluginsManager import loadBotPlugins
from pluginsManager import runPlugin

class reloadPlugins(object):
	"""перезагружает плагины"""
	def __init__(self, bot):
		pass

	def accessLevel(self):
		return 0

	def run(self,bot,user,message):
		logging.debug(u"reload plugins")
		bot.plugins = loadBotPlugins(bot)
		bot.sendMessage(user,"restarted plugins")

	def help(self):
		return "перезагружает плагины"
