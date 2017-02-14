#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime


b = int(datetime.datetime.today().strftime('%w'))

chromedriver = "/Users/adam/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://blich.iscool.co.il/tabid/2117/language/he-IL/Default.aspx")
time.sleep(3)
elem = driver.find_element_by_xpath("""//*[@id="dnn_ctr7919_TimeTableView_TdClassesList"]""")
ddd = driver.find_element_by_xpath('''//*[@id="dnn_ctr7919_TimeTableView_ClassesList"]/option[@value='2']''').click()
driver.find_element_by_xpath('''//*[@id="dnn_ctr7919_TimeTableView_btnChangesTable"]''').click()

#    xpath for first lesson      //*[@id="dnn_ctr7919_TimeTableView_PlaceHolder"]/div/table/tbody/tr[4]/td[4]/table/tbody/tr[2]/td
# xpath for tuesday 1st lesson  /html/body[@id='Body']/form[@id='Form']/table[1]/tbody/tr/td[@id='dnn_TopPane']/table/tbody/tr[2]/td[@id='dnn_ctr7919_ContentPane']/div[@id='dnn_ctr7919_ModuleContent']/div/div[@id='dnn_ctr7919_TimeTableView_PlaceHolder']/div/table[@class='TTTable']/tbody/tr[3]/td[@class='TTCell'][3]/table/tbody/tr/td[@class='TableFillChange']

# xpath try original  driver.find_element_by_xpath(''' /html/body[@id='Body']/form[@id='Form']/table[1]/tbody/tr/td[@id='dnn_TopPane']/table/tbody/tr[2]/td[@id='dnn_ctr7919_ContentPane']/div[@id='dnn_ctr7919_ModuleContent']/div/div[@id='dnn_ctr7919_TimeTableView_PlaceHolder']/div/table[@class='TTTable']/tbody/tr[3]/td[@class='TTCell'][''',day,''']/table/tbody/tr/td[@class='TableFillChange']''')


# DAY = SUNDAY

print "DAY = SUNDAY"

#lesson = 0        day = sunday
T00 =  ''' //*[@class='TTTable']/tbody/tr[2]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T00)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 1        day = sunday
T01 =  ''' //*[@class='TTTable']/tbody/tr[3]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T01)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 2        day = sunday
T02 =  ''' //*[@class='TTTable']/tbody/tr[4]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T02)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 3        day = sunday
T03 =  ''' //*[@class='TTTable']/tbody/tr[5]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T03)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 4        day = sunday
T04 =  ''' //*[@class='TTTable']/tbody/tr[6]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T04)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 5        day = sunday
T05 =  ''' //*[@class='TTTable']/tbody/tr[7]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T05)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 6        day = sunday
T06 =  ''' //*[@class='TTTable']/tbody/tr[8]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T06)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)





# DAY = MONDAY

print "DAY = MONDAY"
time.sleep(1)


#lesson = 0 
T10 =  ''' //*[@class='TTTable']/tbody/tr[2]/td[@class='TTCell'][2]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T10)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 1
T11 =  ''' //*[@class='TTTable']/tbody/tr[3]/td[@class='TTCell'][2]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T11)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 2        day = sunday
T12 =  ''' //*[@class='TTTable']/tbody/tr[4]/td[@class='TTCell'][2]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T12)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 3        day = sunday
T13 =  ''' //*[@class='TTTable']/tbody/tr[5]/td[@class='TTCell'][2]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T13)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 4        day = sunday
T14 =  ''' //*[@class='TTTable']/tbody/tr[6]/td[@class='TTCell'][2]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T14)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 5        day = sunday
T15 =  ''' //*[@class='TTTable']/tbody/tr[7]/td[@class='TTCell'][2]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T15)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 6        day = sunday
T16 =  ''' //*[@class='TTTable']/tbody/tr[8]/td[@class='TTCell'][2]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T16)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)


# DAY = TUESDAY

print "DAY = TUESDAY"
time.sleep(1)


#lesson = 0 
T20 =  ''' //*[@class='TTTable']/tbody/tr[2]/td[@class='TTCell'][3]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T20)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 1
T21 =  ''' //*[@class='TTTable']/tbody/tr[3]/td[@class='TTCell'][3]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T21)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 2        day = sunday
T22 =  ''' //*[@class='TTTable']/tbody/tr[4]/td[@class='TTCell'][3]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T22)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 3        day = sunday
T23 =  ''' //*[@class='TTTable']/tbody/tr[5]/td[@class='TTCell'][3]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T23)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 4        day = sunday
T24 =  ''' //*[@class='TTTable']/tbody/tr[6]/td[@class='TTCell'][3]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T24)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 5        day = sunday
T25 =  ''' //*[@class='TTTable']/tbody/tr[7]/td[@class='TTCell'][3]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T25)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)
#lesson = 6        day = sunday
T26 =  ''' //*[@class='TTTable']/tbody/tr[8]/td[@class='TTCell'][3]//*[@class='TableFreeChange']'''
try:
	 driver.find_element_by_xpath(T26)
except:
	print "no"
else:
	print "yes"
time.sleep(0.5)









#lesson1 test for free lesson






#driver.quit()