# -*- coding: utf-8 -*-
from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length =30)


    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category

    def save_category(self):
    
