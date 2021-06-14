from django.db import models

# Create your models here.

class reg(models.Model):
	NAME=models.CharField(max_length=30)
	EMAIL=models.EmailField()
	MOBILE=models.IntegerField()
	DISTRICT=models.CharField(max_length=30)