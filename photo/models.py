from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to = 'images/',default='DEFAULT VALUE')
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    location = models.ForeignKey(Location,on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name