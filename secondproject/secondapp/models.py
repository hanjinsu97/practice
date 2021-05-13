from django.db import models

class Member(models.Model):
    Name = models.CharField(max_length=200, default='')
    age = models.IntegerField(default=0)
    Class = models.IntegerField(default=0)
    Major = models.CharField(max_length=100, default='')
    Hobby = models.CharField(max_length=200, default='')
    


