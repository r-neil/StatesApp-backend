#from __future__ import unicode_literals

from django.db import models

class State(models.Model):
	state_name = models.CharField(max_length=100)
	state_abbrev = models.CharField(max_length=2)
	capital = models.CharField(max_length=20)
	population = models.CharField(max_length=100)
	population_rank = models.IntegerField()
	joined_union = models.DateField()
	nicknames = models.CharField(max_length=200)
	