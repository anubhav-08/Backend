from django.db import models

class organisation(models.Model):
	name = models.CharField(max_length=50)
	number = models.CharField(max_length=6)
	def __str__(self):
		return self.name

class country(models.Model):
	name = models.CharField(max_length=50)
	number = models.CharField(max_length=6)
	def __str__(self):
		return self.name
    
class user(models.Model):
	name = models.CharField(max_length=50 , blank=True, null=True,)
	handle = models.CharField(max_length=50)
	rating = models.CharField(max_length=4)
	maxRating = models.CharField(max_length=4)
	rank = models.CharField(max_length=50)
	maxRanking = models.CharField(max_length=50)
	worldRank = models.CharField(max_length=6 , blank=True, null=True,)
	countryRank = models.CharField(max_length=6, blank=True, null=True,)
	organisationRank = models.CharField(max_length=6, blank=True, null=True,)
	country = models.ForeignKey(country , on_delete=models.SET_NULL, blank=True, null=True,)
	organisation = models.ForeignKey(organisation , on_delete=models.SET_NULL, blank=True, null=True,)
	photoUrl = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class contest(models.Model):
	TYPE = (
		('R' , 'Regular'),
		('G' , 'Gym')
	)
	name = models.CharField(max_length=50)
	contestId = models.CharField(max_length=10)
	duration = models.CharField(max_length=50)
	startTime = models.CharField(max_length=50)
	participants = models.CharField(max_length=6)
	Type = models.CharField(max_length=1, choices=TYPE)
	
	def __str__(self):
		return self.name

class user_contest_rank(models.Model):
	user = models.ForeignKey(user , on_delete=models.CASCADE)
	contest = models.ForeignKey(contest , on_delete=models.CASCADE)
	worldRank = models.CharField(max_length=6)
	countryRank = models.CharField(max_length=6)
	organisationRank = models.CharField(max_length=6)

	def __str__(self):
		return self.user.name + self.contest.name

class organisation_contest_participation(models.Model):
	organisation = models.ForeignKey(organisation , on_delete=models.CASCADE)
	contest = models.ForeignKey(contest , on_delete=models.CASCADE)
	number = models.CharField(max_length=6)

	def __str__(self):
		return self.organisation.name + self.contest.name

class country_contest_participation(models.Model):
	country = models.ForeignKey(country , on_delete=models.CASCADE)
	contest = models.ForeignKey(contest , on_delete=models.CASCADE)
	number = models.CharField(max_length=6)

	def __str__(self):
		return self.country.name + self.contest.name

