#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

config={
		'friends':( 'myjabber',)
		}



class emi(object):
	"""docstring for emi"""
	def __init__(self, bot):
		for friend in config['friends']:
			bot.sendMessage(friend,u"привет я проснулась ) поболтай со мной")

	def accessLevel():
		return 1000

	def run(bot,user,message):
		logging.debug(u"выполняем run emi")
		bot.sendMessage(user,"ты так интересно рассказываешь ))")

	def help():
		return "при старте бота сигнализирует о том что он поднялся )"