from django.contrib import admin

# Register your models here.

from .models import Category, Movie

#admin panelinde Category ve Movie modellerini manipule edebilmek için ekledik. buradan veri eklenip silinebilir.
admin.site.register(Category)
admin.site.register(Movie)
