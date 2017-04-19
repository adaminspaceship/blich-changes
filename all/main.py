#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime
import sys
import calendar


classnum = "3"

#######################################################################################################################################



date = str(datetime.datetime.today().strftime('%w'))

nownownow = datetime.datetime.now()

dateweek =  time.strftime("%A")

pathday = '/Users/adam/Desktop/logs/'+date+'.log'

timecurrent = time.strftime("%X")

daytoday = open(pathday, 'w')

hournow = ("%s" %nownownow.hour)
hournowint = int(hournow)

chromedriver = "/Users/adam/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://blich.iscool.co.il/tabid/2117/language/he-IL/Default.aspx")
elem = driver.find_element_by_xpath("""//*[@id="dnn_ctr7919_TimeTableView_TdClassesList"]""")
# value 3 at the end = ט - 3
ddd = driver.find_element_by_xpath('''//*[@id="dnn_ctr7919_TimeTableView_ClassesList"]/option[@value='2']''').click()
driver.find_element_by_xpath('''//*[@id="dnn_ctr7919_TimeTableView_btnChangesTable"]''').click()


#######################################################################################################################################
print "Today is " + dateweek

def FreeLesson():
	T00 =  ''' //*[@class='TTTable']/tbody/tr[4]/td[@class='TTCell'][3]//*[@class='TableExamChange']'''
	
	try:
		driver.find_element_by_xpath(T00)
	except:
		return False
		print "false"
		
	else:
		return True
		print "true"
		

FreeLesson()
#######################################################################################################################################

#alarm function
def alarm():
	hour1 = input("what hour do you want to set the alarm to?   ")
	minute1 = input("what minute do you want to set the alarm to?   ")
	print('Alarm running...')
	not_executed = 1

	while(not_executed == 1):
		dt = list(time.localtime())
		hour = dt[3]
		minute = dt[4]
		time.sleep(5)
		if (hour == hour1) and (minute == minute1) and (FreeLesson() == True):
			hour2 = hour1 + 1
			minute2 = minute1 + 1
			hour2str = str(hour2)
			print "Free Lesson Found... Waking up at " + hour2str + ":00"
			not_executed = 3
			while(not_executed == 3):
				dt = list(time.localtime())
				hour = dt[3]
				minute = dt[4]
				time.sleep(5)
				if (hour == hour1) and (minute == minute2):
					print "Wake Up!      press ⌘ C  "
					os.system("afplay /Users/adam/Desktop/a.mp3")
					not_executed = 0
			
		elif (hour == hour1) and (minute == minute1) and (FreeLesson() == False):
			print "Wake up, first hour!"
			os.system("afplay /Users/adam/Desktop/a.mp3")
		
	
			

# end alarm function


alarm()



#quiting all

daytoday.close()

driver.quit()