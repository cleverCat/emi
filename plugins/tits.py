#!/usr/bin/env python
# -*- coding: utf-8 -*-

class tits(object):
	"""показывает (o Y o)"""
	def __init__(self, arg):
		pass

	def accessLevel(self):
		return 0

	def run(self,bot,user,message):
		bot.sendMessage(user,"(o Y o)")

	def help(self):
		return "показывает (o Y o) "