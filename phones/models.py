from django.db import models


class Phone(models.Model):
    name = models.CharField('name', max_length=50)
    slug = models.SlugField('URL', unique=True)
    price = models.IntegerField('price')
    image = models.CharField('image', max_length=1000)
    release_date = models.CharField('release_date', max_length=30)
    lte_exists = models.BooleanField('lte_exists')