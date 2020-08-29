from django.db import models

class List(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class Link(models.Model):
    address = models.CharField(max_length=100)

class Entry(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300)
    long_description = models.TextField()
    active = models.BooleanField(default=True)
    web_address = models.ForeignKey(Link, on_delete=models.CASCADE)