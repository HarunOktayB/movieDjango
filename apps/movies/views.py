from django.shortcuts import render
from .models import Category, Movie
from django.http import HttpResponse

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all()
    }
    return render(request, "movies/index.html", data)

def movies(request):
    sort_order = request.GET.get('sort', 'decreasing')  # Varsayılan: decreasing
    if sort_order == 'increasing':
        filmler = Movie.objects.all().order_by('puan')  # Küçükten büyüğe
    else:
        filmler = Movie.objects.all().order_by('-puan')  # Büyükten küçüğe

    data = {
        "kategoriler": Category.objects.all(),
        "filmler": filmler,
        "current_sort": sort_order
    }
    return render(request, "movies/movies.html", data)

def movie_details(request, slug):
    data = {
        "id": Movie.objects.get(slug=slug),
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all()
    }
    return render(request, "movies/details.html", data)

def category_movies(request, id):
    kategori = Category.objects.get(id=id)  # Seçilen kategori
    sort_order = request.GET.get('sort', 'decreasing')  # Varsayılan: decreasing
    if sort_order == 'increasing':
        filmler = Movie.objects.filter(category=kategori).order_by('puan')  # Küçükten büyüğe
    else:
        filmler = Movie.objects.filter(category=kategori).order_by('-puan')  # Büyükten küçüğe

    data = {
        "secilen_kategori": kategori,
        "kategoriler": Category.objects.all(),
        "filmler": filmler,
        "current_sort": sort_order
    }
    
    return render(request, "movies/movies.html", data)


def movie_search(request):
    query = request.GET.get('search', '').strip()
    if query:
        movies = Movie.objects.filter(name__icontains=query)  # Film ismine göre arama yap
    else:
        movies = []

    return render(request, "movies/search_results.html", {"movies": movies})
