from django.db import models
# Create your models here.


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(max_length=200, blank=True, verbose_name='Description')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category_type = models.ForeignKey('Category', related_name='products', blank=True, null=True,
                                     on_delete=models.CASCADE, verbose_name='Выберите категорию')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self)->str:
        return f'{self.name} {self.created}'

    def get_absolute_url(self):
        return reverse('work:product_detail', args=[self.id, self.slug])

