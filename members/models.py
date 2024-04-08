from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Member2(models.Model):
  myname=models.CharField(max_length=255)
  myage=models.IntegerField()