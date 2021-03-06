from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    # number_of_books = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(1000)])

    def __str__(self):
        return self.first_name +' '+ self.middle_name + ' ' +self.last_name


class Book(models.Model):
    author = models.ManyToManyField(Author)
    title = models.CharField(max_length= 120)
    date_published = models.DateField()
    buy_link = models.URLField(max_length=120, blank=True)
    images = models.ImageField(upload_to="photobook", blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    review = models.TextField()
    avg_star = models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(5)])
    createdOn = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User)

