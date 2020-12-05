from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length=500)
    prob_id = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    tags = models.CharField(max_length = 500,default = "")
    contest_id = models.CharField(max_length=100,default="")
    index = models.CharField(max_length=5,default="")
    rating = models.CharField(max_length=10,default="")
    platform = models.CharField(max_length=100,default="")
    # contest id , index(a,b,c,d...) , name, tag, rating, platform

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    