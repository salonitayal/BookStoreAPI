from django.contrib import admin
from booklistapp.models import Book, Publisher, Review

# Register your models here.
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Review)