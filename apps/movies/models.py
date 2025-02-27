from pyclbr import Class
from pydoc import classname
from django import db
from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # category = models.ForeignKey(Category, default="BOS", on_delete=models.SET_DEFAULT)
    #Eğer bir kategori silinirse o kategoriye ait filmler de silinir.
    puan = models.FloatField()
    resim = models.CharField(max_length=100)
    qualityPic = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True, db_index=True)
    #slug alanı url'de görünecek olan kısmı belirler.

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)  # Başlıktan slug oluştur
            slug = base_slug
            counter = 1

            # Aynı slug varsa, film ID'sini veya rastgele bir kısa UUID ekleyerek benzersiz yap
            while Movie.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{uuid.uuid4().hex[:6]}"  # 6 karakterlik benzersiz bir ekleme yap
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    