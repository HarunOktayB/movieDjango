from django.shortcuts import render
from . models import Category, Movie

# kullanıcıya gösterilecek olan veriler burada organize edilir.
# eğer bir veritabanı işlemi yapılacaksa burada yapılır.
# bu basit bir proje olduğu için class tabanlı view yapısını kullanmadık.
# view fonksiyonları işimizi görmüş oldu.
def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all()
    }
    return render(request, "movies/index.html", data)

def movies(request):
    data= {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all()
    }
    return render(request, "movies/movies.html", data)

def movie_details(request, id):
    data= {
        "id": Movie.objects.get(id=id),
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all()
    }
    return render(request, "movies/details.html", data)