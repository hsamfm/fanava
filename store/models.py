from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from category.models import Category
from store.manager import ProductManager
from website.utils import upload_image_path, random_string


# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=600)
    description = models.TextField(max_length=1000)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, to_field='name')
    tech = models.CharField(max_length=30)
    is_free = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def __str__(self):
        return f"{self.name} :: {self.created_at} :: {self.user}"

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def get_absolute_url(self):
        return reverse('store-detail', kwargs={'id': self.id})

    @property
    def display_name(self):
        og_name = get_file_name(self.image.name)

        if self.name:
            return self.name
        return og_name
