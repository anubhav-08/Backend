from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from problem.models import Problem

# Create your views here.
def problem_index(request):

	return HttpResponse("Codeforces Problem Index Page (to be designed)")