from PromiedosAPI import *

promiedos = PromiedosAPI()

'''
in league paramater: 
leagues:

espana
italia
inglaterra
alemania
brasil
francia


argentina: (in paramater only put the name of the division)
	superliga
	bnacional
	bmetro
	federala
	primerac
	primerad

'''
#promiedos.get_matches(league, round)
promiedos.get_matches("superliga", 2)
'''
should return:

["team", "team", "team", "team"]

example:
['Talleres (C)', 'Rosario Central', 'Newells', 'Independiente', 'Def y Justicia', 'Atl Tucuman', 'Banfield', 'Gimnasia LP', 'Argentinos', 'Godoy Cruz', 'River Plate', 'Belgrano', 'San Martin (SJ)', 'Patronato', 'Colon', 'Tigre', 'Aldosivi', 'Huracan', 'San Lorenzo', 'Lanus', 'Racing Club', 'Velez', 'Estudiantes LP', 'Boca Juniors', 'San Martin (T)', 'Union']
'''

#----

promiedos.get_scores("superliga", 2)
'''
should return:

["team", "team", "team", "team" ... "score home team", "score away team"]

example:
'Talleres (C)', 'Rosario Central', 'Newells', 'Independiente', 'Def y Justicia', 'Atl Tucuman', 'Banfield', 'Gimnasia LP', 'Argentinos', 'Godoy Cruz', 'River Plate', 'Belgrano', 'San Martin (SJ)', 'Patronato', 'Colon', 'Tigre', 'Aldosivi', 'Huracan', 'San Lorenzo', 'Lanus', 'Racing Club', 'Velez', 'Estudiantes LP', 'Boca Juniors', 'San Martin (T)', 'Union', 
'0', '1', '2', '2', '1', '1', '1', '0', '0', '0', '0', '0', '1', '0', '2', '2', '2', '1', '2', '2', '2', '0', '2', '0', '1', '1']

'''

promiedos.get_standings("primera")

'''

['Racing Club 42 17 13 3 1 32 10 +22', 'Def y Justicia 39 17 11 6 0 24 10 +14', 'Boca Juniors 31 16 9 4 3 24 11 +13', 'Atl Tucuman 31 16 9 4 3 31 19 +12', 'Huracan 30 17 8 6 3 22 16 +6', 'Velez 28 17 8 4 5 22 19 +3', 'River Plate 25 16 7 4 5 24 13 +11', 'Independiente 25 17 6 7 4 25 17 +8', 'Union 24 17 6 6 5 15 15 0', 'Aldosivi 24 17 7 3 7 16 19 -3', 'Godoy Cruz 23 17 7 2 8 16 19 -3', 'Talleres (C) 22 17 6 4 7 18 16 +2', 'Banfield 22 17 5 7 5 15 16 -1', 'Lanus 21 17 5 6 6 16 20 -4', 'Newells 20 17 5 5 7 15 13 +2', 'Colon 19 17 4 7 6 16 21 -5', 'Rosario Central 19 16 5 4 7 12 18 -6', 'Estudiantes (LP) 18 17 4 6 7 16 20 -4', 'San Martin (SJ) 18 17 5 3 9 18 24 -6', 'Tigre 18 17 4 6 7 20 30 -10', 'Gimnasia (LP) 18 17 5 3 9 15 25 -10', 'San Martin (T) 17 17 3 8 6 16 25 -9', 'Patronato 16 17 4 4 9 22 28 -6', 'San Lorenzo 15 17 2 9 6 15 21 -6', 'Belgrano 14 17 2 8 7 10 18 -8', 'Argentinos 11 17 2 5 10 5 17 -12']

'''