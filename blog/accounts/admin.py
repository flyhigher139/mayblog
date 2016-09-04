from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Account)
admin.site.register(models.SocialInfo)