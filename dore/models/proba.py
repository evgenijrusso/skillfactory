from django.db import models
from django.shortcuts import render
from django.views import View


class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Author(models.Model):
    full_name = models.CharField(max_length=64)
    name = models.CharField(null=True, max_length=64)

    def some_method(self):
        self.name = self.full_name.split()[0]
        self.save()


b = Author.some_method()