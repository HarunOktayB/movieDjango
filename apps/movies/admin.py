import html
from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.

from .models import Category, Movie

admin.site.site_header = "Film Sitesi Admin Paneli"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'puan', 'resim', 'qualityPic', 'slug',"selected_categories"]
    list_editable = ['puan', 'resim', 'qualityPic']
    search_fields = ['name', 'category__name']
    list_filter = ['category']
    def selected_categories(self, obj):
        html = ""
        for category in obj.category.all():
            html += f"<span style='background-color: #f2f2f2; padding: 3px; border-radius: 5px; margin-right: 5px;'>{category.name}</span>"
        return mark_safe(html)
    
#admin panelinde Category ve Movie modellerini manipule edebilmek için ekledik. buradan veri eklenip silinebilir.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)
