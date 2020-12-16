import requests
from math import log2
from problem.models import Problem

def rating_to_difficulty(rating):
	if rating <= 1100 : 
		return 'B'
	elif rating <= 1500:
		return 'E'
	elif rating <= 1800:
		return 'M'
	elif rating <= 2100:
		return 'H'
	elif rating <= 2600:
		return 'S'
	else :
		return 'C'

def update_uva_problems():

	url = "https://uhunt.onlinejudge.org/api/p"
	res= requests.get(url)
	data = res.json()

	for p in data:

		if len(Problem.objects.filter(prob_id = p[0])) > 0 :
			continue

		new_problem = Problem()
		new_problem.prob_id = p[0]
		new_problem.index = p[1]
		new_problem.name = p[2]
		dacu = p[3]
		wa = p[16]

		if dacu != 0 and wa != 0:
			rating = min(3600 , max(800 ,3200 - (log2(dacu) * log2(wa/dacu) / 20 * 3200) + 600))
			new_problem.rating = str(int(rating))
			new_problem.difficulty = rating_to_difficulty(rating)
		elif dacu != 0 :
			rating = min(3600 , max(800 ,3200 - (log2(dacu) / 20 * 3200) + 600))
			new_problem.rating = str(rating)
			new_problem.difficulty = rating_to_difficulty(rating)

		new_problem.platform = 'U'
		new_problem.url = "https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem="+str(p[0])
		new_problem.save()