from django.urls import path

from . import views

urlpatterns = [
    path('problems', views.problem_index, name='index'),
]