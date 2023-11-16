from django.db import models


class StatusManager(models.Manager):
    pass

class Status:
    name = models.CharField('name', max_length=50, blank=True)
    name_en = models.CharField('name_en', max_length=50, blank=True)
    name_ru = models.CharField('name_ru', max_length=50, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'

    objects = StatusManager()
# ---------------  --------------------

DATA_REPAIR = {
    'Completed': (
        'Completed', 'Завершен',
    ),
    'Rejected':
        ('Rejected', 'Отклонен'),
}



for objname in DATA_REPAIR:
    obj = Status.objects.filter(name=objname).first()
    if obj:
         obj.name = DATA_REPAIR[objname][0]
         obj.name_en = DATA_REPAIR[objname][0]
         obj.name_ru = DATA_REPAIR[objname][1]
         obj.save()
