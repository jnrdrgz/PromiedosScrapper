#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re
import urllib.request
		
#class Match:
#	def __init__(self, inited=False, hour, id):

class PromiedosAPI:
	URL = "http://www.promiedos.com.ar/"

	def __init__(self):
		print("API Inited")

	def _get_HTML_league(self, league, lround):
		extLeagues = {"espana": 10, 
		"italia": 11, "inglaterra": 12,
		"alemania": 25, "brasil":26, 
		"francia": 27}

		localLeagues = {"superliga": "", 
		"bnacional": "b", "bmetro": "bm",
		"federala": "fa", "primerac": "c",
		"primerad": "d"}

		#10 españa
		#11 italia
		#12 premier
		#25 alemania
		#26 brasil
		#27 francia

		if(league in extLeagues.keys()):
			r = urllib.request.urlopen(self.URL + "fechaex.php?fecha=" + str(lround) + "_&liga=" + str(extLeagues[league]))
		elif(league in localLeagues.keys()):
			r = urllib.request.urlopen(self.URL + "fecha" + localLeagues[league] +".php?fecha=" + str(lround))
		else:
			print("League not found")
			return []

		s = BeautifulSoup(r, 'html.parser')

		return s

	def get_matches(self, league, lround):
		#print(league)

		s = self._get_HTML_league(league, lround)

		prueba = []

		for e in s.find_all(class_='datoequipo'):
			prueba.append(e.get_text())

		return prueba

	def get_scores(self, league, lround):
		#print(league)

		s = self._get_HTML_league(league, lround)

		prueba = []

		for e in s.find_all(class_='datoequipo'):
			prueba.append(e.get_text())
		for e in s.find_all("span", {"id": re.compile("r\d_\d_\d\d\d")}):
			prueba.append(e.get_text())

		return prueba

	def prueba(self):
		pass