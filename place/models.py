from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH

from django.db import models
from django.utils import timezone

# Create your models here.
CATEGORY_LIST = (
    ("RESTAURANTS", "Restaurants"),
    ("ATTRACTIONS", "Attractions"),
    ("PARTIES", "Parties"),
    ("OTHER", "Other")
)
RATING_LIST = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
)

class Place(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    thumb = models.ImageField(upload_to='thumb-places')
    category = models.CharField(max_length=15, choices=CATEGORY_LIST)
    adress = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    place = models.ForeignKey("Place", related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    rating = models.CharField(max_length=5, choices=RATING_LIST)
    creation_date = models.DateTimeField(default=timezone.now)
