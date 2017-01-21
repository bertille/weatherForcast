#!/usr/bin/python

import httplib

# Variables
MYKEY="2914e9db205477351929329d6eae4772"
URI="/data/2.5/weather?q="
HOSTNAME="api.openweathermap.org"
mycities = ['Paris','Barcelone','Prague']


class Forecaster:
	def __init__(self, comment):
		self.comment=comment

	def searchCity(self, city):
		connection=httplib.HTTPConnection(HOSTNAME)
		CITY=city
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

	def setComment(self):
		self.comment=comment

	def getComment(self):
		return self.comment


	# Search for a array of city
	def searchCities(self,cities):
		if len(cities) > 0:	
			for city in cities:
				self.searchCity(city)
		else:
			print "No cities to process"
			return


forecastGVA=Forecaster("Prévision pour Paris")
forecastGVA.searchCity("Paris")

forecastGLOBAL=Forecaster("Prevision pour trois villes d'Europe")
forecastGLOBAL.searchCities('mycities')
