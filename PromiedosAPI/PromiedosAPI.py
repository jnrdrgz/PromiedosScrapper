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

	def _get_HTML_league(self, league, lround=0):
		extLeagues = {"espana": 10, 
		"italia": 11, "inglaterra": 12,
		"alemania": 25, "brasil":26, 
		"francia": 27}

		localLeagues = {"primera": "", 
		"bnacional": "b", "bmetro": "bm",
		"federala": "fa", "primerac": "c",
		"primerad": "d"}

		#10 españa
		#11 italia
		#12 premier
		#25 alemania
		#26 brasil
		#27 francia

		if(lround != 0):
			if(league in extLeagues.keys()):
				r = urllib.request.urlopen(self.URL + "fechaex.php?fecha=" + str(lround) + "_&liga=" + str(extLeagues[league]))
			elif(league in localLeagues.keys()):
				r = urllib.request.urlopen(self.URL + "fecha" + localLeagues[league] +".php?fecha=" + str(lround))
			else:
				print("League not found")
				return []
		else:
			r = urllib.request.urlopen(self.URL + league)
			
			

		s = BeautifulSoup(r, 'html.parser')

		return s

	def get_matches(self, league, lround):
		#print(league)

		s = self._get_HTML_league(league, lround)

		equipos = []
		fechas = []
		horarios = []

		for e in s.find_all(class_='datoequipo'):
			equipos.append(e.get_text())

		for e in s.find_all(class_="horariopartido"):
			fechas.append((e.get_text()).strip())

		for e in s.find_all(class_="falta"):
			horarios.append((e.get_text()).strip())



		return equipos + fechas + horarios
		
	def get_scores(self, league, lround):
		#print(league)

		s = self._get_HTML_league(league, lround)

		prueba = []

		for e in s.find_all(class_='datoequipo'):
			prueba.append(e.get_text())
		for e in s.find_all("span", {"id": re.compile("r\d_\d_\d\d\d")}):
			prueba.append(e.get_text())

		return prueba

	def get_standings(self, league, team=False, json=False):
		s = self._get_HTML_league(league)

		s = s.find(class_='tablesorter3')
		#str(s)

		s = re.findall(re.compile(r'<strong>[A-Za-z()_.\- ]+<\/strong><\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>[-+]?\d+'), str(s))

		if json == True:
			#{team1: }
			s = [((x.replace("</td><td>", "---")).replace("<strong>", "")).replace("</strong>", "") for x in s]
			json = {}
			pos = 1
			for te in s:
				t = te.split("---")
				json[t[0]] = {
					"points": int(t[1]),
					"played": int(t[2]),
					"wins": int(t[3]),
					"draws":int(t[4]),
					"losses":int(t[5]),
					"GF": int(t[6]),
					"GA": int(t[7]),
					"GD": int(t[8]),
					"pos": pos
				}
				pos += 1

			if team != False:
				return json[team]

			return json

		s = [((x.replace("</td><td>", " ")).replace("<strong>", "")).replace("</strong>", "") for x in s]

		return s

		#regex pos
		#<strong>[A-Za-z()_.\- ]+<\/strong><\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>[-+]?\d+