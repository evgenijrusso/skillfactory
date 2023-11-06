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


# DATA_REPAIR = {
#     'Completed': (
#         'Completed', 'Завершен',
#     ),
#     'Rejected':
#         ('Rejected', 'Отклонен'),
# }
#
#
# # не работает
# for objname in DATA_REPAIR:
#     obj = Status.objects.filter(name=objname).first()
#     if obj:
#          obj.name = DATA_REPAIR[objname][0]
#          obj.name_en = DATA_REPAIR[objname][0]
#          obj.name_ru = DATA_REPAIR[objname][1]
#          obj.save()
