#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re
import urllib.request


		
#class Match:
#	def __init__(self, inited=False, hour, id):

class promiedosAPI:
	URL = "http://www.promiedos.com.ar/"

	def __init__(self):
		print("API Inited")

	def getMatches(self, league, round):
		#print(league)
		r = urllib.request.urlopen(self.URL + "fechaex.php?fecha=" + str(round) + "_&liga=10")
		s = BeautifulSoup(r, 'html.parser')

		prueba = []

		for e in s.find_all(class_='datoequipo'):
			prueba.append(e.get_text())
			
		return prueba

		