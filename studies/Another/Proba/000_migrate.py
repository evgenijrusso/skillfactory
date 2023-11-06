from proba1 import Status

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
