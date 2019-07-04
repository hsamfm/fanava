from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from website.utils import upload_image_path


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    see_post = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} :: {self.user}"

    def get_absolute_url(self):
        """
        :return url with parameter
        :argument id, title, date
        """
        return reverse('blog:detail', kwargs={'id': self.pk, 'title': self.title, 'date': self.created_at})

    def get_edit_url(self):
        return f"/posts/{self.title}/{self.created_at}/edit/"

    def get_delete_url(self):
        return f"/posts/{self.title}/delete/"
