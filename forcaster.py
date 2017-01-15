#!/usr/bin/python

import os
import httplib

MYKEY="2914e9db205477351929329d6eae4772"
URI="/data/2.5/weather?q=Geneve"
URL=URI+'&APPID='+MYKEY+'&mode=xml'


connection = httplib.HTTPConnection('api.openweathermap.org')
connection.request("GET", URL)
response = connection.getresponse()
data = response.read()

print response.status
print data

connection.close()
