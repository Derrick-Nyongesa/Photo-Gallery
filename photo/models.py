from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to = 'images/',default='DEFAULT VALUE')
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name