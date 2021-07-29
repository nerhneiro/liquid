from django.db import models

# Create your models here.
class Product(models.Model):
    cost = models.PositiveIntegerField(verbose_name='Стоимость')
    name = models.CharField(verbose_name='Название', max_length=180)
    description = models.CharField(verbose_name='Описание', max_length=300)
    colors = models.ManyToManyField('Color', verbose_name='Цвета')
    # image = models.ImageField(verbose_name='Фотография')

class Color(models.Model):
    color = models.CharField(verbose_name='Код цвета HEX', max_length=128)

class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=128)