from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH

from django.db import models
from django.utils import timezone

# Create your models here.
CATEGORY_LIST = (
    ("RESTAURANT", "Restaurant"),
    ("ATTRACTIONS", "Attractions"),
    ("PARTYS", "Partys"),
    ("OTHER", "Other")
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

