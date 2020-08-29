from django.db import models

class List(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class Entry(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)