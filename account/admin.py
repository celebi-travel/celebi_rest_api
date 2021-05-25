from django.contrib import admin

# Register your models here.
from account import models

admin.site.register(models.UserBase)
