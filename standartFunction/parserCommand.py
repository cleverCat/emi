#!/usr/bin/env python
# -*- coding: utf-8 -*-

#делит строку попалам до разделителя и после не включая разделитель 
def _getSibstringsOnQuote(string,separator):
	if separator in string:
		return {'left':string[:string.find(separator)],'rigth':string[string.find(separator)+len(separator):]}
	return {'left':string,'rigth':""}

#получаем список слов разделенных разделителем
def _getWords(string,separator):
	words=[]
	for word in string.split(separator):
		if word!="":
			words.append(word)
	return words

#возвращаем список подстрок и остаток от строки
def _getSubstringsAndReast(string,isQuote):
	separator=u"\'"
	if isQuote==True:
		return {"'"+'substrinds':[_getSibstringsOnQuote(string,separator)['left']+"'",],
				'restString':string[string.find(separator)+len(separator):]}
	else:
		return {'substrinds':_getWords(_getSibstringsOnQuote(string,separator)['left']," "),'restString':string[string.find(separator)+len(separator):]}

#получаем список подстрок остаток строки и признак рассматриваем ли мы слово в кавычках
def getSubstrings(separator,string,isQuote):
	substrings=[]
	if separator not in string:
		substrings=_getWords(string," ")
		string=""
	else:
		substrings=_getSubstringsAndReast(string,isQuote)['substrinds']
		string=_getSubstringsAndReast(string,isQuote)['restString']
		isQuote=not isQuote
	return {'substrings':substrings,'string':string,'isQuote':isQuote}

# подстроки разделяемые 
#пробелами и кавычками если внутри подстроки обрамленной кавычками есть пробелы
#они не являются разделителями и такую строку нужно вернуть в кавычках , такие дела
def getListParameters(string):
	try:

		separator=u"\'"
		if (string.count(separator)%2!=0):
			raise NameError, "lol odd number of quotes oo"
		kokoString=string
		substrings=[]
		ko=False
		i=0
		while kokoString!="":
			s=getSubstrings(separator,kokoString,ko)
			substrings,kokoString,ko=substrings+s['substrings'],s['string'],s['isQuote']
			i=i+1
			if i==10:
				break
		return substrings
	except Exception, e:
		raise e
	
