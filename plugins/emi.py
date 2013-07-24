#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from standartFunction.TSettingsRecord import *

config=TSettingsRecord("emi","emi").getSettings()


class emi(object):
	"""docstring for emi"""
	def __init__(self, bot):
		for friend in config['friends']:
			bot.sendMessage(friend,u"привет я проснулась ) поболтай со мной")

	def accessLevel(self):
		return 1000

	def run(self,bot,user,message):
		logging.debug(u"выполняем run emi")
		bot.sendMessage(user,"ты так интересно рассказываешь ))")

	def help(self):
		return "при старте бота сигнализирует о том что он поднялся )"