#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
try:
	import xml.etree.ElementTree as etree
except Exception, e:
	logging.debug(u"load xml.etree failed")


class TSettingsRecord(object):
	"""класс записи настройки"""
	def __init__(self,name,fileConfig):
		try:
			self.name = name
			tree = etree.parse('settings/'+fileConfig+'.xml')
			root = tree.getroot()
			setting=root.find(name)
			self.properties=setting.attrib
			for child in setting:
				listValuePropirtie=list() 
				for field in child:
					listValuePropirtie.append(field.text)
				self.properties.update({child.tag:listValuePropirtie})
		except Exception, e:
			logging.debug(u"problem from load settings")
			logging.debug(e)
		finally:
			pass
		

	def getSettings(self):
		"""получить настройки"""
		return self.properties
