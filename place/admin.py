from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Comment, Place, User

fields = list(UserAdmin.fieldsets)
fields.append(
    ("Registered Places", {'fields': ('registered_places',)})
)

UserAdmin.fieldsets = tuple(fields)
# Register your models here.
admin.site.register(Place)
admin.site.register(Comment)
admin.site.register(User, UserAdmin)
