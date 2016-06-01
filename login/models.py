from __future__ import unicode_literals

from django.db import models

# Create your models here.
class USER(models.Model):
	user_id = models.CharField(max_length=15)
	name = models.CharField(max_length=10)
	password = models.IntegerField(max_length=15)
	age = models.IntegerField(max_length=3)