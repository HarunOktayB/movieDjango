from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.movies.urls'))
]
# Burada include fonksiyonunu kullanarak movies uygulamasını projemize dahil ediyoruz.
# Bu sayede movies uygulamasının urls.py dosyasına yönlendirme yapmış oluyoruz.
# Yani movies uygulamasının urls.py dosyasındaki yönlendirmeleri projemize dahil etmiş oluyoruz.
# Bu sayede movies uygulamasının urls.py dosyasındaki yönlendirmeleri projemizde kullanabiliriz.
# Buraya her projenin urls.py dosyasına yönlendirme yapılabilir.