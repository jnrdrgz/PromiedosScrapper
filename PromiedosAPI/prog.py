from apiProm import promiedos, getStats
import time

partidos = promiedos()

a = 1
idsJugando = []

for i in range(len(partidos)):
	#print("partido"+ str(a) + ":" + partidos["Partido"+str(a)]["EL"] +  "-" + partidos["Partido"+str(a)]["EV"])
	if "ID" in partidos["Partido"+str(a)].keys():
		try:
			print("partido"+ str(a) + ":" + partidos["Partido"+str(a)]["EL"] + " " 
				+ partidos["Partido"+str(a)]["GL"] +  "-" + " " + partidos["Partido"+str(a)]["GV"] + partidos["Partido"+str(a)]["EV"] 
				+ " tim: " + partidos["Partido"+str(a)]["Tiem"])
		except Exception as e:
			print(str(e))
		
		idsJugando.append(partidos["Partido"+str(a)]["ID"])
	a += 1

for i in range(len(idsJugando)):
	idsJugando[i] = idsJugando[i].replace("id=" ,"")

while(True):
	for i in range(len(idsJugando)):
		a = getStats(idsJugando[i])
		print(a)

	time.sleep(120)