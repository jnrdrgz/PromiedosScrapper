#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re
import urllib.request
import itertools

# class Partido -> to do: make a class partido

#classes
class Match:
	def __init__(self, _id="", time=0, date="", stadium="", referee="", home="", away=""):
			self._id = _id
			self.time = time
			self.date = date
			self.stadium = stadium
			self.referee = referee
			self.home = home 
			self.away = away
			
class LiveTeam:
	def __init__(self, name="", goals=0, scorers=[], stats="", players="", coach="", changes="", yellow_cards="", red_cards=""):
		self.name = name
		self.goals = goals
		self.scorers = scorers
		self.stats = stats
		self.players = players
		self.coach = coach
		self.changes = changes
		self.yellow_cards = yellow_cards 
		self.red_cards = red_cards
			

class Stat:
	def __init__(self, possession="", shots_attempts="", shots_ongoal="", fouls="", corners=""):
		self.possession = possession
		self.shots_attempts = shots_attempts
		self.shots_ongoal = shots_ongoal
		self.fouls = fouls
		self.corners = corners


class PromiedosAPI:
	URL = "http://www.promiedos.com.ar/"

	def __init__(self):
		print("API Inited")

	def _get_HTML_league(self, league, lround=0):
		extLeagues = {"espana": 10, 
		"italia": 11, "inglaterra": 12,
		"alemania": 25, "brasil":26, 
		"francia": 27, "mexico": 87, "mls": 88}

		localLeagues = {"primera": "", 
		"bnacional": "b", "bmetro": "bm",
		"federala": "fa", "primerac": "c",
		"primerad": "d"} #argentina divisions

		#10 españa
		#11 italia
		#12 premier
		#25 alemania
		#26 brasil
		#27 francia

		if(lround != 0):
			if(league in extLeagues.keys()):
				r = urllib.request.urlopen(self.URL + "fechaex.php?fecha=" + str(lround) + "_&liga=" + str(extLeagues[league]) + ".php")
			elif(league in localLeagues.keys()):
				r = urllib.request.urlopen(self.URL + "fecha" + localLeagues[league] +".php?fecha=" + str(lround))
			else:
				print("League not found")
				return []
		else:
			r = urllib.request.urlopen(self.URL + league)
			
		s = BeautifulSoup(r, 'html.parser')

		return s

	def _get_html(self, extra, strin=False): #this function has to replace _get_html_league
		p = self.URL + extra
		r = urllib.request.urlopen(p)
		s = BeautifulSoup(r, 'html.parser')
		
		if strin:
			return str(s)

		return s

	def get_matches(self, league, lround, json=False):
		#print(league)

		s = self._get_HTML_league(league, lround)

		'''equipos = []
		fechas = []
		horarios = []

		for e in s.find_all(class_='datoequipo'):
			equipos.append(e.get_text())

		for e in s.find_all(class_="horariopartido"):
			fechas.append((e.get_text()).strip())

		for e in s.find_all(class_="finaliza"):
			horarios.append((e.get_text()).strip())

		for e in s.find_all(class_="falta"):
			horarios.append((e.get_text()).strip())'''

		todo = []

		for x in s.findAll(True, {'class':['datoequipo', 'falta', 'finaliza', 'horariopartido']}):
			todo.append(x.get_text())

		# played si/no, id if played, ordenar fecha/hora

		if json:
			_json = {}
			
			return _json

		return todo
		#return equipos + fechas + horarios
		#return s
	def get_scores(self, league, lround=0):
		#print(league)

		s = self._get_HTML_league(league, lround)

		#print(s)

		quips = [] #teams list
		scores = [] #scores list
		ids = []

		if s != []:
			for e in s.find_all(class_='datoequipo'):
				quips.append(e.get_text())
			for e in s.find_all("span", {"id": re.compile("r\d\d?\d?_\d\d?\d?_\d\d?\d?")}):
				ids.append(e.get_text())
				#need to be fixed because not all ids follow this regex it has to be
				#dd?d?_dd?d?_dd?d? sintax needs to be fixed

			for e in s.find_all(class_='resu'):
				scores.append(e.get_text())

			if scores[0] != '':
				return list(itertools.chain.from_iterable(zip(quips, scores)))
			return quips

	def get_standings(self, league, team=False, json=False):
		s = self._get_HTML_league(league)

		s = s.find(class_='tablesorter3')
		#str(s)

		s = re.findall(re.compile(r'<strong>[A-Za-z()_.\- ]+<\/strong><\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>[-+]?\d+'), str(s))

		if json == True:
			#{team1: }
			s = [((x.replace("</td><td>", "---")).replace("<strong>", "")).replace("</strong>", "") for x in s]
			_json_ = {}
			pos = 1
			for te in s:
				t = te.split("---")
				_json[t[0]] = {
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
				return _json[team]

			return _json

		s = [((x.replace("</td><td>", " ")).replace("<strong>", "")).replace("</strong>", "") for x in s]

		return s

		#regex pos
		#<strong>[A-Za-z()_.\- ]+<\/strong><\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>\d+<\/td><td>[-+]?\d+

	'''def get_stats(self, id_):
		promiLink = self.URL + "ficha.php?id=" + id_
		try:
			r = urllib.request.urlopen(promiLink)
			s = BeautifulSoup(r, 'html.parser')

			s = str(s)
			
			s = s.replace(" (total de intentos)", "")

			newArr = re.findall(r'>\d\d?%?<|>Posesion:<|>Tiros efectivos al arco:<|Fouls Cometidos:|Tiros al arco:|Corners:', s)
			
			tiempo = re.findall(r'se">\d\d?|se">Entretiempo|iz">Finalizado', s)
			
			ind = newArr.index(">Posesion:<")
			newArr = newArr[ind:]
			
			newArr = [(x.replace("<", "")).replace(">", "") for x in newArr]

			for i in range(len(newArr)):
				if("%" in newArr[i]):
					newArr[i] = newArr[i].replace("%", "")

			dic = {}
			a = 0
			dats = ["PL", "PV", "TAL", "TAV", "TL" , "TV", "FL", "FV", "CL", "CV"]
			for i in range(1, len(newArr), 3):
				dic[dats[a]] = newArr[i]
				dic[dats[a+1]] = newArr[i+1]
				a += 2

			return dic
		except Exception as e:
			dic = {}
			print(e)
			print("Probably you put an invalid id")
			return dic'''

	def get_match(self, id_):
		ext = "ficha.php?id=" + id_

		s = self._get_html(ext)

		statsHT = [] #home	
		statsAT = [] #away
		flag = 0
		tmp = []

		match = Match()
		hTeam = LiveTeam()
		hStats = Stat()
		aTeam = LiveTeam()
		aStats = Stat()

		match._id = id_

		for x in s.findAll(True, {'id':['ficha-horario']}):
			st = x.get_text()
			if ":" in x:
				lmt = s.index(":")+3
				match.date = st[:lmt]
				match.referee = match.stadium = st[lmt+1:]
			else:
				match.referee = match.stadium = st

		for x in s.findAll(True, {'id':['ficha-tiempo']}):
			match.time = x.get_text()

		f = 0		
		dathtmp = []
		datatmp = []
		for x in s.findAll(True, {'class':['nomequipo', 'incidencias1', 'incidencias2', 'amarillas', 'rojas', 'cambios']}):
			if f < 2:
				if x.get("class") == ['nomequipo']:
					if f == 0:
						hTeam.name = x.get_text()
					else:
						aTeam.name = x.get_text()
					f += 1
				else:
					dathtmp.append(x.get_text())
				
			else:
				if x.get("class") == ['nomequipo']:
					aTeam.name = x.get_text()
				else:
					datatmp.append(x.get_text())

		dicH = {}
		dicA = {}
		
		for i in range(0, len(dathtmp), 2):
			dicH[dathtmp[i].strip()] = dathtmp[i+1]

		for i in range(0, len(datatmp), 2):
			dicA[datatmp[i].strip()] = datatmp[i+1]


		if "GOLES" in dicH.keys():
			hTeam.scorers = dicH["GOLES"].split(";")[:len(dicH["GOLES"].split(";"))-1]
			hTeam.goals = len(hTeam.scorers)
		if "AMARILLAS" in dicH.keys():
			hTeam.yellow_cards = dicH["AMARILLAS"]
		if "ROJAS" in dicH.keys():
			hTeam.red_cards = dicH["ROJAS"]
		if "CAMBIOS" in dicH.keys():
			hTeam.changes = dicH["CAMBIOS"]

		if "GOLES" in dicA.keys():
			aTeam.scorers = dicA["GOLES"].split(";")[:len(dicA["GOLES"].split(";"))-1]
			aTeam.goals = len(aTeam.scorers)
		if "AMARILLAS" in dicA.keys():
			aTeam.yellow_cards = dicA["AMARILLAS"]
		if "ROJAS" in dicA.keys():
			aTeam.red_cards = dicA["ROJAS"]
		if "CAMBIOS" in dicA.keys():
			aTeam.changes = dicA["CAMBIOS"]
		
		stl = []
		sta = []
		for x in s.findAll(True, {'id':['porcentaje1']}):
			stl.append(x.get_text())
		
		for x in s.findAll(True, {'id':['porcentaje2']}):
			sta.append(x.get_text())
	
		hStats.possession = stl[0]
		hStats.shots_ongoal = stl[1]
		hStats.shots_attempts = stl[2]
		hStats.fouls = stl[3]
		hStats.corners = stl[4]

		aStats.possession = sta[0]
		aStats.shots_ongoal = sta[1]
		aStats.shots_attempts = sta[2]
		aStats.fouls = sta[3]
		aStats.corners = sta[4]
		
		hTeam.stats = hStats
		aTeam.stats = aStats

		match.home = hTeam
		match.away = aTeam
		
		return match

	def _get_secret_id(self, id_):
		s = self._get_html("ficha.php?id=" + id_, True)
		secretid = ((re.search(r's1=\"[A-Za-z]+\"', s).group()).replace('s1=\"', "")).replace('"', "")
		
		return secretid

	def get_live_score(self, secretid, json=False):
		
		link = self.URL + "fichas/" + secretid + ".htm"
		r = urllib.request.Request(link, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0", "X-Requested-With": "XMLHttpRequest"})
		p = urllib.request.urlopen(r)
		s = BeautifulSoup(p, 'html.parser')

		time = s.find(class_='jugandose').get_text()
		teams = [x.get_text() for x in s.find_all(class_='nomequipo')]
		home = s.find("div", {"id": "ficha-resultado1"}).get_text()
		away = s.find("div", {"id": "ficha-resultado2"}).get_text()

		if json:
			return {"time": time, "homeTeam": teams[0], 
			"homeGoals": home, "awayTeam": teams[1], "awayGoals": away}

		return [time, teams[0], home, teams[1], away]

	#today == 1 -> today matches // today == 0 -> next matches(tomorrow and after) 
	def today(self, today=1):
		r = urllib.request.urlopen(self.URL)
		s = BeautifulSoup(r, 'html.parser')
		
		#print(s)
		
		#for e in s.find_all(True, {'class':['datoequipo', 'verdegrande']}:
		#	print(e.get_text())

		tod = []
		nex = []
		flag = 0

		# here create a list of list so the matches from one league separate from others
		# ex [[league1, p1, p2], [league2, p1, p2]]
		for x in s.findAll(True, {'class':['datoequipo', 'falta', 'verdegrande', 'resu', 'tituloin']}):
			if x.get_text() == 'PROXIMOS PARTIDOS':
				flag = 1
			
			if not flag:
				tod.append(x.get_text())
			else:
				nex.append(x.get_text())

		if today == 1:
			return tod[1:]
		else:
			return nex
	

#http://www.promiedos.com.ar/scores.jsonid
#a
