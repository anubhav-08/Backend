import requests
import json
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from .models import organization , country , user , contest , user_contest_rank , organization_contest_participation, country_contest_participation
from problem.models import Problem 

def alter_tables():	
	cursor = connection.cursor()
	cursor.execute('ALTER TABLE codeforces_organization CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci')
	cursor.execute('ALTER TABLE codeforces_user CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci')
	cursor.execute('ALTER TABLE codeforces_country CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci')
	cursor.execute('ALTER TABLE codeforces_contest CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci')


def codeforces_update_users():
	url = "https://codeforces.com/api/user.ratedList"
	res = requests.get(url)
	data= res.json()

	if(data["status"] != 'OK') :
		return 

	user.objects.all().delete()
	country.objects.all().delete()
	organization.objects.all().delete()
	rank = 0
	for codeforces_user in data["result"]:
		newUser = user()

		name = ""
		if 'firstName' in codeforces_user:
			name += codeforces_user['firstName']
			name += " "
		if 'lastName' in codeforces_user:
			name += codeforces_user['lastName']

		if len(name) > 100 : 
			newUser.name = name[:100]
		else :
			newUser.name = name

		newUser.handle = codeforces_user['handle']
		newUser.rating = codeforces_user['rating']
		newUser.maxRating = codeforces_user['maxRating']
		newUser.rank = codeforces_user['rank']
		newUser.maxRank  = codeforces_user['maxRank']
		rank+=1
		newUser.worldRank = rank
		newUser.photoUrl = codeforces_user['titlePhoto'][2:]

		if 'country' in codeforces_user :

			obj, created = country.objects.get_or_create(
				name=  codeforces_user['country'] ,
				defaults={'number': '0'}, 
				)

			obj.number = str(int(obj.number) + 1)
			obj.save()
			newUser.country = obj
			newUser.countryRank = obj.number

		if 'organization' in codeforces_user :

			obj, created = organization.objects.get_or_create(
				name=  codeforces_user['organization'] ,
				defaults={'number': '0'}, 
				)

			obj.number = str(int(obj.number) + 1)
			obj.save()
			newUser.organization = obj
			newUser.organizationRank = obj.number

		newUser.save()
	return 

def codeforces_update_contest():
	url = "https://codeforces.com/api/contest.list"
	res = requests.get(url)
	data = res.json()

	if(data["status"] != 'OK') :
		return 

	contest.objects.all().delete()
	user_contest_rank.objects.all().delete()
	organization_contest_participation.objects.all().delete()
	country_contest_participation.objects.all().delete()

	for codeforces_contest in data["result"]:
		new_contest = contest()

		if 'startTimeSeconds' in codeforces_contest:
			new_contest.startTime = codeforces_contest['startTimeSeconds']

		new_contest.Type = 'R'
		new_contest.contestId = codeforces_contest['id']
		new_contest.name = codeforces_contest['name']
		new_contest.duration = codeforces_contest['durationSeconds']

		url = "https://codeforces.com/api/contest.ratingChanges?contestId=" + str(codeforces_contest['id'])
		res = requests.get(url)
		data = res.json()

		if(data["status"] != 'OK') :
			continue

		new_contest.participants = len(data['result'])
		new_contest.save()

		for participant in data['result']:
			user_handle = participant['handle']
			rank = participant['rank']

			try:
				contest_user = user.objects.get(handle = user_handle)
			except ObjectDoesNotExist:
				continue

			ucr = user_contest_rank()

			ucr.user = contest_user
			ucr.contest = new_contest
			ucr.worldRank = rank

			if contest_user.organization : 
				contest_user_org = contest_user.organization
				
				# check for organization_contest_participation 

				org_contest_participation,created = organization_contest_participation.objects.get_or_create(
					organization = contest_user_org,
					contest = new_contest,
					defaults= {
						'number' : '0'
					}
				)
				org_contest_participation.number = str(int(org_contest_participation.number) + 1)
				org_contest_participation.save()

				ucr.organizationRank = org_contest_participation.number

			if contest_user.country : 

				contest_user_country = contest_user.country

				# check for country_contest_participation

				cntry_contest_participation,created = country_contest_participation.objects.get_or_create(
					country = contest_user_country,
					contest = new_contest,
					defaults= {
						'number' : '0'
					}
				)
				cntry_contest_participation.number = str(int(cntry_contest_participation.number) + 1)
				cntry_contest_participation.save()

				ucr.countryRank = cntry_contest_participation.number

			ucr.save()

#def codeforces_update_problems():
	# check whether we have updated the problems of a particular contest , 
	# if no , update the problems , else not .. 