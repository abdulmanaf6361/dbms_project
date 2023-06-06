from django.db import models
from djongo.models import CheckConstraint, Q
from djongo import models
from pymongo.read_concern import ReadConcern

class modelsignup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)