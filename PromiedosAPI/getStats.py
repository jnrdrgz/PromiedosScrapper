#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re
import urllib.request

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

