from datetime import datetime
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    no_of_pages = models.IntegerField(default=0)
    overall_rating = models.IntegerField(default=0)
    published = models.BooleanField(default=True)
    price = models.IntegerField(null=True)
    publish_date = models.DateField(auto_now_add=True, null=True ,blank=True) 

    def __str__(self):
        return self.title
