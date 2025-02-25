from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('movies', views.movies, name='movies'),
    path('movies/<int:id>', views.movie_details, name='details'),
    path('movies/category/<int:id>/', views.category_movies, name='category_movies'),  # ✅ Eklendi!

    #Burada id parametresi alıyoruz ve bu id parametresi ile movie_details fonksiyonuna yönlendiriyoruz.
    #Bu sayede her bir film için ayrı bir sayfa oluşturmuş oluyoruz.
    #id obje id'si oluyor ve bu id'yi kullanarak o id'ye ait olan filmi çekiyoruz. slug görevi görüyor.
    #movie details movie_details sayfasının oluşması için gerekli olan bir parametre.
    #name='details' ise bu sayfaya bir isim veriyoruz.
    #Bu sayede bu sayfaya yönlendirme yaparken bu ismi kullanabiliriz.
    #Örneğin: <a href="{% url 'details' id=movie.id %}">Detaylar</a>
]
