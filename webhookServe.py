#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
from langdetect import detect


weekday_before = int(datetime.datetime.today().strftime('%w'))
weekday = weekday_before+1
#driver = webdriver.Chrome("C:/Users/adame/Downloads/chromedriver_win32/chromedriver.exe")

#driver.get("http://blich.iscool.co.il/tabid/2117/language/he-IL/Default.aspx")
#time.sleep(3)
#elem = driver.find_element_by_xpath("""//*[@id="dnn_ctr7919_TimeTableView_TdClassesList"]""")
#ddd = driver.find_element_by_xpath('''//*[@id="dnn_ctr7919_TimeTableView_ClassesList"]/option[@value='2']''').click()
#driver.find_element_by_xpath('''//*[@id="dnn_ctr7919_TimeTableView_btnChangesTable"]''').click()

#    xpath for first lesson      //*[@id="dnn_ctr7919_TimeTableView_PlaceHolder"]/div/table/tbody/tr[4]/td[4]/table/tbody/tr[2]/td
# xpath for tuesday 1st lesson  /html/body[@id='Body']/form[@id='Form']/table[1]/tbody/tr/td[@id='dnn_TopPane']/table/tbody/tr[2]/td[@id='dnn_ctr7919_ContentPane']/div[@id='dnn_ctr7919_ModuleContent']/div/div[@id='dnn_ctr7919_TimeTableView_PlaceHolder']/div/table[@class='TTTable']/tbody/tr[3]/td[@class='TTCell'][3]/table/tbody/tr/td[@class='TableFillChange']

# xpath try original  driver.find_element_by_xpath(''' /html/body[@id='Body']/form[@id='Form']/table[1]/tbody/tr/td[@id='dnn_TopPane']/table/tbody/tr[2]/td[@id='dnn_ctr7919_ContentPane']/div[@id='dnn_ctr7919_ModuleContent']/div/div[@id='dnn_ctr7919_TimeTableView_PlaceHolder']/div/table[@class='TTTable']/tbody/tr[3]/td[@class='TTCell'][''',day,''']/table/tbody/tr/td[@class='TableFillChange']''')

driver = webdriver.Chrome("C:/Users/adame/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("http://blich.iscool.co.il/tabid/2117/language/he-IL/Default.aspx")
time.sleep(3)
elem = driver.find_element_by_xpath("""//*[@id="dnn_ctr7919_TimeTableView_TdClassesList"]""")
ddd = driver.find_element_by_xpath('''//*[@id="dnn_ctr7919_TimeTableView_ClassesList"]/option[@value='19']''').click()
driver.find_element_by_xpath('''//*[@id="dnn_ctr7919_TimeTableView_btnChangesTable"]''').click()

T00 =  ''' //*[@class='TTTable']/tbody/tr[2]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''

T01 =  ''' //*[@class='TTTable']/tbody/tr[3]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''

T02 =  ''' //*[@class='TTTable']/tbody/tr[4]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''

T03 =  ''' //*[@class='TTTable']/tbody/tr[5]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''

T04 =  ''' //*[@class='TTTable']/tbody/tr[6]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''

T05 =  ''' //*[@class='TTTable']/tbody/tr[7]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''

T06 =  ''' //*[@class='TTTable']/tbody/tr[8]/td[@class='TTCell'][1]//*[@class='TableFreeChange']'''

#

res = ""

#//*[@id="dnn_ctr7919_TimeTableView_PlaceHolder"]/div/table/tbody/tr[5]/td[4]/table/tbody/tr/td

yesMade = "false"

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
       # self.wfile.write("This is POST-ONLY server...")

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print(post_data)
        object1 = json.loads(post_data)
        object2 = object1["result"]["parameters"]["Day"]
        objecttest = object1["result"]["resolvedQuery"]
        lang = detect(objecttest)
        if object2 == "today":
            answerArray = []
            yesMade = "false"
            print(weekday)
            a = weekday
            finalDay = a
            for i in range(3,11):
                c = ''' //*[@id="dnn_ctr7919_TimeTableView_PlaceHolder"]/div/table/tbody/tr['''+str(i)+''']/td[@class='TTCell']['''+str(finalDay)+''']/table/tbody/tr/td[@class='TableFreeChange']'''
                #c = ''' //*[@class='TTTable']/tbody/tr['''+str(i)+''']/td[@class='TTCell']['''+str(finalDay)+''']//*[@class='TableFreeChange']'''
                print(c)
                
                try:
                    driver.find_element_by_xpath(c)
                except:
                    print ("no")
                    res = "no"
                    answerArray.append("no")
                else:
                    if yesMade == "false":
                        yesMade = "true"
                        print ("yes")
                        res = "yes"
                        answerArray.append("yes")
                        
            print(answerArray)
            if "yes" in answerArray:
                self._set_response()
                #self.wfile.write("POST request".encode('utf-8'))
                if lang == "he":
                    lastjson = json.dumps({'speech':"כן",'displayText':"כן",'data':{},'contextOut':[],'source':'adam'})
                    print("Response: "+lastjson)
                    self.wfile.write(lastjson.encode('utf-8'))
            else:
                self._set_response()
                #self.wfile.write("POST request".encode('utf-8'))
                if lang == "he":
                    lastjson = json.dumps({'speech':"לא",'displayText':"לא",'data':{},'contextOut':[],'source':'adam'})
                    print("Response: "+lastjson)
                    self.wfile.write(lastjson.encode('utf-8'))
                
        if object2 == "tomorrow":
            answerArrayT = []
            yesMade = "false"
            print(weekday)
            a = weekday
            finalDay = a+1
            for i in range(3,11):
                c = ''' //*[@id="dnn_ctr7919_TimeTableView_PlaceHolder"]/div/table/tbody/tr['''+str(i)+''']/td[@class='TTCell']['''+str(finalDay)+''']/table/tbody/tr/td[@class='TableFreeChange']'''
                #c = ''' //*[@class='TTTable']/tbody/tr['''+str(i)+''']/td[@class='TTCell']['''+str(finalDay)+''']//*[@class='TableFreeChange']'''
                print(c)
                
                try:
                    driver.find_element_by_xpath(c)
                except:
                    print ("no")
                    res = "no"
                    answerArrayT.append("no")
                else:
                    if yesMade == "false":
                        yesMade = "true"
                        print ("yes")
                        res = "yes"
                        answerArrayT.append("yes")
                        
            print(answerArrayT)
            if "yes" in answerArrayT:
                self._set_response()
                #self.wfile.write("POST request".encode('utf-8'))
                if lang == "he":
                    lastjson = json.dumps({'speech':"כן",'displayText':"כן",'data':{},'contextOut':[],'source':'adam'})
                    print("Response: "+lastjson)
                    self.wfile.write(lastjson.encode('utf-8'))
                else:
                    lastjson = json.dumps({'speech':"Yes",'displayText':"Yes",'data':{},'contextOut':[],'source':'adam'})
                    print("Response: "+lastjson)
                    self.wfile.write(lastjson.encode('utf-8'))
            else:
                self._set_response()
                #self.wfile.write("POST request".encode('utf-8'))
                if lang == "he":
                    lastjson = json.dumps({'speech':"לא",'displayText':"לא",'data':{},'contextOut':[],'source':'adam'})
                    print("Response: "+lastjson)
                    self.wfile.write(lastjson.encode('utf-8'))
                else:
                    lastjson = json.dumps({'speech':"No",'displayText':"No",'data':{},'contextOut':[],'source':'adam'})
                    print("Response: "+lastjson)
                    self.wfile.write(lastjson.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
