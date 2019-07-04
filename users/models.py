from django.db import models
from django.contrib.auth.models import User
from website.utils import upload_image_path, random_string
# Create your models here.


# class Admin(models.Model):
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_admin = models.ForeignKey(User, on_delete=models.CASCADE)

# class AdminTodo(models.Model):
#     title = models.CharField()