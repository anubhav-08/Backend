from django.shortcuts import render
from django.http import HttpResponse
from .cron import codeforces_update_users , codeforces_update_contest , alter_tables
from .models import organization , country , user , contest , user_contest_rank , organization_contest_participation, country_contest_participation



# # #


# Create your views here.
def index(request):
	alter_tables()
	codeforces_update_contest()
	return HttpResponse("OKAY")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

"""
obj, created = Person.objects.get_or_create(
    first_name='John',
    last_name='Lennon',
    defaults={'birthday': date(1940, 10, 9)},
)
"""