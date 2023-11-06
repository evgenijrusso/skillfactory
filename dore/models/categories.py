from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=70, db_index=True, verbose_name='Категория')
    fruit = models.CharField(max_length=70, db_index=True, verbose_name='Фрукты')
    vegetables = models.CharField(max_length=70, db_index=True, verbose_name='Овощи')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


def __str__(self):
    return self.name


def get_absolute_url(self):
    return reverse('work:product_by_category', args=[self.slug])

