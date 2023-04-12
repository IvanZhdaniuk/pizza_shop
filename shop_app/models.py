from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пицца')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(verbose_name='Рейтинг')
    photo = models.ImageField(upload_to='shop_app/static/images')
    compound = models.TextField(max_length=300)

    def __str__(self):
        return self.name


