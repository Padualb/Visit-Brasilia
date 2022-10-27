from django.contrib import admin

from .models import Comment, Place

# Register your models here.
admin.site.register(Place)
admin.site.register(Comment)
