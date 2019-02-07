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
'Talleres (C)', 'Rosario Central', 'Newells', 'Independiente', 'Def y Justicia', 'Atl Tucuman', 'Banfield', 'Gimnasia LP', 'Argentinos', 'Godoy Cruz', 'River Plate', 'Belgrano', 'San Martin (SJ)', 'Patronato', 'Colon', 'Tigre', 'Aldosivi', 'Huracan', 'San Lorenzo', 'Lanus', 'Racing Club', 'Velez', 'Estudiantes LP', 'Boca Juniors', 'San Martin (T)', 'Union', '0', '1', '2', '2', '1', '1', '1', '0', '0', '0', '0', '0', '1', '0', '2', '2', '2', '1', '2', '2', '2', '0', '2', '0', '1', '1']

'''
