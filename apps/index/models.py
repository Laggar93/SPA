from django.db import models

class Spa(models.Model):

    created_at = models.DateField(verbose_name='Дата' ,auto_now_add=True)
    name = models.CharField(verbose_name='Название', max_length=255,
                             null=True)
    count = models.PositiveIntegerField(verbose_name='Количество',
                             default=1)
    distance = models.PositiveIntegerField(verbose_name='Расстояние',
                             default=1)
