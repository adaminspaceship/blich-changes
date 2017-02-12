# -*- coding: utf-8 -*-
import requests
import os
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import smtplib
import ifttt_maker

ifttt = ifttt_maker.Ifttt("blich", "pYTi1N5f7ucT6tqt0PZjDVfgTjg_0rz6wRlI5EorafI")
gmail_user = 'adam.eliezerov@gmail.com'  
gmail_password = 'adamadam123'
fromaddr = 'adam.eliezerov@gmail.com'
toaddrs  = 'adam.eliezerov@gmail.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(gmail_user,gmail_password)


url = "http://blich.iscool.co.il/DesktopModules/IS.TimeTable/MainScreen.aspx?pid=17&mid=6264&page=1&msgof=0&static=1"

r = requests.get(url)

html_content = r.text

soup = BeautifulSoup(html_content,"html.parser")
soup.original_encoding
'WINDOWS-1255'

table = soup("td", {'class' : 'DisplayFreeChange' })


#testing if test found in table0
try:
    table0 = table[0]
    
except:
    print "No free lesson found"
else:
    print "Free lesson found!"
    table0str = str(table0)
    table0strdone = re.sub('<[^>]*>', '', table0str)
    subject = "ביטול במערכת שעות"
    message = 'Subject: {}\n\n{}'.format(subject, table0strdone)
    #server.sendmail(fromaddr, toaddrs, message)
    print (table0strdone)
    ifttt.trigger(value1=table0strdone)
	





	
	
#end all proccess running
server.quit()
	
