from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

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
    published = models.BooleanField(default=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="book")
    price = models.IntegerField(null=True)
    publish_date = models.DateField(auto_now_add=True, null=True ,blank=True) 
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    #  on_delete : means if someone dlt movie, all reviews will be dltd
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + " - " + self.book.title
