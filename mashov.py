#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from http.cookies import SimpleCookie
cookie = SimpleCookie()
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-uname", help="username", dest='uname',required=True)
parser.add_argument("-passwd", help="password", dest='passwd',required=True)

results = parser.parse_args()

mainheaders = {'Content-Type': 'application/json;charset=UTF-8','Accept-Encoding':'compress;q=0.5, gzip;q=1.0'}
url = "https://svc.mashov.info/api/login"
username = results.uname
password = results.passwd
data1 = '{"school":{"semel":540211,"name":"תיכון בליך - רמת גן","years":[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],"top":true},"username":"'+username+'","year":2017,"password":"'+password+'","semel":540211,"appName":"com.mashov.main","appVersion":3.20170503}'


r = requests.post(url, data=data1, headers=mainheaders)


def authOK():
    cookie.load(r.headers['Set-Cookie'])
    MashovSessionID = cookie['MashovSessionID'].value
    CsrfToken = cookie['Csrf-Token'].value
    uniqueId = cookie['uniquId'].value
    XCsrfToken = r.headers['X-Csrf-Token']
    loginheads = {'Content-Type': 'application/json;charset=UTF-8', 'Accept-Encoding': 'compress;q=0.5, gzip;q=1.0'}
    loginheads['X-Csrf-Token'] = XCsrfToken
    loginheads['Cookie'] = "MashovSessionID="+MashovSessionID+"; Csrf-Token="+CsrfToken+"; uniquId="+uniqueId
    studentId = json.loads(r.text)
    studentId =  studentId['credential']['userId']
    post = requests.get("https://svc.mashov.info/api/students/"+studentId+"/grades", headers=loginheads)
    grades = json.loads(post.text)
    gradeArray = []
    for x in range(0,len(grades)):
        gradeArray.append(grades[x]['grade'])
        if "None" in gradeArray: gradeArray.remove("None")
    for a in gradeArray:
        print a


if r.status_code == 200:
    authOK()
else:
    print "auth wrong. Try again."










# curl -i -H "Accept-Encoding:compress;q=0.5, gzip;q=1.0" -H "Content-Type:application/json;charset=UTF-8" -H "Cookie:MashovSessionID=MY_MASHOV_SESSION_ID; Csrf-Token=MY_CSRF_TOKEN; uniquId=MY_UNIQUE_ID" -H "X-Csrf-Token:AGAIN_MY_CSRF_TOKEN" "https://svc.mashov.info/api/students/MY_ACCOUNT_ID/grades"



# {"school":{"semel":540211,"name":"תיכון בליך - רמת גן","years":[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],"top":true},"username":"adameliezerov","year":2017,"password":"otherworld2","semel":540211,"appName":"com.mashov.main","appVersion":3.20170503}

