from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    counter = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={"name": self.name})
