from django.shortcuts import render

kategori_liste = ["macera" ,"romantik" ,"dram", "etiket"]
film_liste =   [{"isim": "film 1", "id": 1,
                 "kategori": "macera", 
                 "puan": 8.5, 
                 "resim": "1.jpg", 
                 "qualityPic":"picsum.photos/800/400?random=1"
                 }, 

                {"isim":"film 2", "id":2, "kategori": "romantik", "puan": 7.5, "resim": "2.jpg", "qualityPic":"picsum.photos/800/400?random=2"}, 
                {"isim":"film 3", "id":3, "kategori": "dram", "puan": 6.5, "resim": "3.jpg", "qualityPic":"picsum.photos/800/400?random=3"}, 
                {"isim":"film 4", "id":4, "kategori": "etiket", "puan": 9.5, "resim": "4.jpg" ,"qualityPic":"picsum.photos/800/400?random=4"}
            ]
# Create your views here.
def home(request):
    data = {
        "kategoriler": kategori_liste,
        "filmler": film_liste
    }
    return render(request, "movies/index.html", data)

def movies(request):
    data= {
        "kategoriler": kategori_liste,
        "filmler": film_liste
    }
    return render(request, "movies/movies.html", data)

def movie_details(request, id):
    data= {
        "id": id,
        "filmler": film_liste
    }
    return render(request, "movies/details.html", data)