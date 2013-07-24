#!/usr/bin/env python
# -*- coding: utf-8 -*-


class help(object):
	"""показывает справку по коммандам"""
	def __init__(self, bot):
		pass

def init(bot):
	return 0

def run(bot,user,message):
	if message==u"комманды" or message==u"commands":
		bot.sendMessage(user,",".join(bot.plugins['commands']) )
		return
	if bot.plugins['message']!=null:
		plugin = bot.plugins['message']
		try:
			helpText=plugin.help()
			bot.sendMessage(user,helpText)
		except Exception:
			bot.sendMessage(user,u"к сожалению коммандa ( "+str(message)+u" не содержит справку")
	else:
		bot.sendMessage(user,u"к сожалению у меня нет справки по комманде ( "+str(message))


def help(self):
	return "показывает справку по коммандам"