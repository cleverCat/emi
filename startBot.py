#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
	import xmpp,sys
	import logging
	from standartFunction.TSettingsRecord import *
except ImportError:
	pass
from jabberBot import TJabberBot


reload(sys)
sys.setdefaultencoding('utf8') 
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)

def messageHandler(conn, mess): #вызывается при входящем сообщении
	global bot
	if (mess.getBody() == None ):
		return
	if (mess.getBody()==u"засыпай эми"):
		sys.exit(1)

	text = unicode(mess.getBody()) #получаем текст сообщения
	user = mess.getFrom() #и  отправителя
	logging.debug(user.getNode()+u"@"+user.getDomain()+text)
	bot.getMessage(user,text)


#while(True):
#	try:
config=TSettingsRecord("bot","bot").getSettings()
bot = TJabberBot(str(config['user']),str(config['server']),int(config['port']),str(config['password']))
bot.registerHandler('message', messageHandler)
bot.start()
#	except:
#		pass

