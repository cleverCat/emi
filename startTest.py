#!/usr/bin/env python
# -*- coding: utf-8 -*-

import test.testSqlAdapter
import sys


reload(sys)
sys.setdefaultencoding('utf8') 

def runTests():
	"""загружаем тесты бота из папочки с тестами"""
	import os
	outpytString=""
	try:
		tests=[]
		for fileName in os.listdir('test/'):
			if fileName.endswith('.py'):#выбираем только файлы с расширением py
				testName = fileName[:-3]#убираем расширение файла
				if testName != '__init__':# игнорируем файл __init__.py
					tests=__import__('test.'+testName)
					test = getattr(tests,testName)
					if test.startTest():
						outpytString=outpytString+testName+u" пройден\n"
					else:
						outpytString=outpytString+u"!!"+testName+u" завален\n"
	except Exception, e:
		outpytString=outpytString+u"\n!!!ужасно тесты упали (("
		raise e
	return outpytString
			
print runTests()

