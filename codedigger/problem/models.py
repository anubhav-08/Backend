from django.db import models

from enum import Enum
from django_enum_choices.fields import EnumChoiceField


class platform(Enum):
    Codeforces = 0
    Codechef = 1
    Spoj = 2
    Uva = 3
    Atcoder = 4

class difficulty(Enum):
    Very_Easy = 0
    Easy = 1
    Medium = 2
    Hard = 3
    Super_Hard = 4
    Extreme_Hard = 5


class Problem(models.Model):
    name = models.CharField(max_length=500)
    prob_id = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    tags = models.CharField(max_length = 500,default = "")
    contest_id = models.CharField(max_length=100,default="")
    index = models.CharField(max_length=5,default="")
    rating = models.CharField(max_length=10,default="")
    #platform = models.CharField(max_length=100,default="")
    platform = EnumChoiceField(platform)
    # contest id , index(a,b,c,d...) , name, tag, rating, platform
    # difficulty (enum)
    # editorial link (official / video editorial)
    # video editorial 

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    