from django.db import models

# Create your models here.
from django_countries.fields import CountryField

"""
rota, mekan vs
"""


class Place(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField()
    description = models.TextField()
    created_by = models.ForeignKey('account.UserBase',on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
