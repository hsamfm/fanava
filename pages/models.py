from django.db import models
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} :: {self.description}"

    class Meta:
        ordering = ['-created_at', '-updated_at']