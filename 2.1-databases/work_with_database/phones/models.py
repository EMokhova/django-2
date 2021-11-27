from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.SlugField(max_length=50)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
