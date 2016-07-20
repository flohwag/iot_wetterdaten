#!/usr/bin/env python
# coding: utf8

import sys, os, time
#import MySQLdb
import httplib


sensors = {"feuchtigkeit", "licht"}

#def printText(txt):
#    lines = txt.split('\n')
#    for line in lines:
#        print line.strip()

def getValues():
    return "feuchtigkeit,27;licht,50"
#    httpServ = httplib.HTTPConnection("10.1.10.109", 80)
#    httpServ.connect()
#
#    httpServ.request('GET', "/")
#
#    response = httpServ.getresponse()
#    if response.status == httplib.OK:
#        print "Output from HTML request", printText (response.read())
#        return printText(response.read)

def uploadToServer(sensor, value):
    pass

def getValuesFromText(sensor):
    text = getValues()
    for sensor in sensors:
        x = text.index(sensor)
        comma = text.index(",", x)
        print y
        print sensor + str(x)


#connection = MySQLdb.connect (host = "localhost",
#                              user = "data",
#                              passwd = "ljhbosaubcLAK",
#                              db = "data",)

#cursor = connection.cursor()


getValuesFromText("feuchtigkeit")

#print getValuesFromText("feuchtigkeit")
