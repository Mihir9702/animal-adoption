from django.db import models
from users.models import CustomUser as User  # Import User model

class Animal(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, blank=True)
    age = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(blank=True)
    adopted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
