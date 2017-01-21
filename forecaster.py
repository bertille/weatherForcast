#!/usr/bin/python

import httplib

# Variables
MYKEY="2914e9db205477351929329d6eae4772"
URI="/data/2.5/weather?q="
HOSTNAME="api.openweathermap.org"


class Forecaster:
	def __init__(self, city):
		self.city = city

	def search(self):
		connection=httplib.HTTPConnection(HOSTNAME)
		CITY=self.city
		URL=URI+CITY+'&APPID='+MYKEY+'&mode=xml'

		connection.request("GET", URL)
		response=connection.getresponse()
		data=response.read()
	
		if response.status == 200:
			print(data)
			return data
			connection.close()
		else:
			print(response)
			connection.close()

	def getCity(self):
		return self.city

forecastGVA=Forecaster("Paris")
forecastGVA.search()
