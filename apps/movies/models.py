from pyclbr import Class
from pydoc import classname
from django.db import models

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    puan = models.FloatField()
    resim = models.CharField(max_length=100)
    qualityPic = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    