from bs4 import BeautifulSoup
import re
import urllib.request

def promiedos():
	prom = "http://www.promiedos.com.ar" 
	page = urllib.request.urlopen(prom)
	soup = BeautifulSoup(page, 'html.parser')

	soup = str(soup)

	juntos = re.findall(r'ficha\.php\?id=\w*|po\">[\s|\w|\.|(|)]*|ti_\d*_\d*\">[\s|\w|\.\:]*|">\d<', soup)

	for i in range(len(juntos)):
		if "ficha.php?id=" in juntos[i]:
			juntos[i] = juntos[i].replace("ficha.php?", "")
		elif "</td><td style=\"width: 34%;" in juntos[i]:
			juntos[i] = juntos[i].replace("</td><td style=\"width: 34%;", "")
		elif "po\">" in juntos[i]:
			juntos[i] = juntos[i].replace('po">', "")
		elif "ti_" in juntos[i]:
			a = juntos[i].index(">")
			juntos[i] = juntos[i][a:len(juntos[i])]
		elif (juntos[i][0] == "\"" and juntos[i][3] == "<"):
			juntos[i] = juntos[i] = juntos[i].replace("<", "")
			juntos[i] = juntos[i].replace("\">", "")

	cc = 0		
	while(True):
		if cc == len(juntos):
			break
		if juntos[cc][0] == ">":
			juntos.insert(cc, "--")
			cc+=1
		cc += 1


	final = []
	arrAux = []
	arrAux2 = []
	cc = 0

	while(True):
		if juntos[cc] == "--":
			arrAux2.append(arrAux)
			arrAux = []
			cc += 1

		else:
			arrAux.append(juntos[cc])
			cc +=1

		if cc == len(juntos):
			break

	juntos = arrAux2[1:]

	for i in range(len(juntos)):
		juntos[i][0] = juntos[i][0].replace(">", "")
		juntos[i][0] = juntos[i][0].replace("  ", "")

	print(juntos)
	partido = 1
	dic = {}
	for i in range(len(juntos)):
		dic['Partido' + str(partido)] = {}
		partido += 1

	partido = 1

	for i in range(len(juntos)):
		for j in range(len(juntos[i])):
			if len(juntos[i]) == 3:
				dic['Partido' + str(partido)]["Hora"] = juntos[i][0]
				dic['Partido' + str(partido)]["EL"]   = juntos[i][1]	
				dic['Partido' + str(partido)]["EV"]   = juntos[i][2]
			if len(juntos[i]) == 4:
				dic['Partido' + str(partido)]["Hora"] = juntos[i][0]
				dic['Partido' + str(partido)]["EL"]   = juntos[i][1]	
				dic['Partido' + str(partido)]["EV"]   = juntos[i][2]
				dic['Partido' + str(partido)]["ID"]   = juntos[i][3]
			if len(juntos[i]) == 6:
				dic['Partido' + str(partido)]["Tiem"] = juntos[i][0]
				dic['Partido' + str(partido)]["EL"]   = juntos[i][1]
				dic['Partido' + str(partido)]["GL"]   = juntos[i][2]
				dic['Partido' + str(partido)]["GV"]   = juntos[i][3]	
				dic['Partido' + str(partido)]["EV"]   = juntos[i][4]
				dic['Partido' + str(partido)]["ID"]   = juntos[i][5]	

		partido += 1

	return dic

def getStats(id):
	promiLink = "http://www.promiedos.com.ar/ficha.php?id=" + id
	try:
		page = urllib.request.urlopen(promiLink)
		soup = BeautifulSoup(page, 'html.parser')
		#print(soup)

		soup = str(soup)
		with open("htmPr.html", "w") as f:
			f.write(soup)
		#newArr = re.findall(r'\d[\s]?[\s]?-[\s]?[\s]?\d', soup)
		soup = soup.replace(" (total de intentos)", "")


		newArr = re.findall(r'>\d\d?%?<|>Posesion:<|>Tiros efectivos al arco:<|Fouls Cometidos:|Tiros al arco:|Corners:', soup)
		tiempo = re.findall(r'se">\d\d?|se">Entretiempo|iz">Finalizado', soup)
		
		ind = newArr.index(">Posesion:<")
		newArr = newArr[ind:]

		for i in range(len(newArr)):
			newArr[i] = newArr[i].replace("<", "")
			newArr[i] = newArr[i].replace(">", "")
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
		return dic

