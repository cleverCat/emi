#!/usr/bin/env python
# -*- coding: utf-8 -*-
class echo(object):
	"""отсылает то что прислали ему параметром"""
	def __init__(self, bot):
		pass
		
	def accessLevel(self):
		return 0
	def run(self,bot,user,message):
		bot.sendMessage(user,message)
		
	def help(self):
		return "отсылает то что ему прислали параметром"