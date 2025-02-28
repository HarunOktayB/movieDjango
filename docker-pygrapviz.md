# Django Model İlişkilerini Docker içinde pygrapviz Kullanarak Görselleştirme

Bu dokümanda, Django projelerinizdeki model ilişkilerini Graphviz kullanarak Docker ortamında nasıl görselleştireceğinizi adım adım açıklıyoruz. Bu yöntem, sistemde Graphviz'i doğrudan kurup PATH'e ekleme yetkiniz olmadığında kullanılabilir.

---

## 1. Gerekli Bağımlılıkları Yükleme

Öncelikle, projenizin bağımlılıklarına `django-extensions` ve `graphviz` kütüphanelerini eklemelisiniz.

```sh
pip install django-extensions graphviz
```

Daha sonra, `settings.py` dosyanızda `INSTALLED_APPS` içerisine `django_extensions` ekleyin:

```python
INSTALLED_APPS = [
    ...
    'django_extensions',
]
```

## 2. Dockerfile Oluşturma

Docker ortamında Django projemizi çalıştırabilmek için aşağıdaki gibi bir `Dockerfile` oluşturun.

**Dockerfile:**
```dockerfile
# Python 3.12 image'ini kullan
FROM python:3.12-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinim dosyasını çalışma dizinine kopyala
COPY requirements.txt /app/

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Graphviz için gerekli bağımlılıkları yükle
RUN apt-get update && apt-get install -y graphviz

# Projenin tüm dosyalarını çalışma dizinine kopyala
COPY . /app/

# Portu expose et (varsayılan Django portu)
EXPOSE 8000

# Django'yu çalıştırmak için komut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

> Bu Dockerfile, Python 3.12 görüntüsünü kullanır, bağımlılıkları yükler ve Graphviz'i sistem içerisine kurar.

## 3. Docker Image Oluşturma

Aşağıdaki komut ile Docker imajınızı oluşturun:

```sh
docker build -t my_django_project .
```

## 4. Docker Container Çalıştırma

Projeyi bir Docker konteyneri içinde çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

```sh
docker run -d -p 8000:8000 --name my_django_container my_django_project
```

> `-d` parametresi, konteyneri arka planda çalıştırır.

## 5. Dosya Formatını Düzenleme (Opsiyonel)

Windows sistemlerinde satır sonları formatı nedeniyle `manage.py` çalışmayabilir. Eğer `/usr/bin/env: ‘python
’: No such file or directory` hatası alıyorsanız aşağıdaki komutu çalıştırarak dosyanın formatını Unix uyumlu hale getirin:

```sh
dos2unix manage.py
```

## 6. Django Model Grafiğini Oluşturma

Konteyner içerisinde aşağıdaki komut ile Django model ilişkilerini görselleştirebilirsiniz:

```sh
docker exec -it my_django_container python manage.py graph_models -a -g -o my_project_visualized.png
```

## 7. Oluşturulan Dosyayı Konteynerden Çekme

Görselleştirilmiş model çıktısını yerel makinenize almak için aşağıdaki komutu kullanabilirsiniz:

```sh
docker cp my_django_container:/app/my_project_visualized.png ./
```

Bu komut, Docker konteyneri içinde oluşturulan `my_project_visualized.png` dosyasını, bulunduğunuz dizine kopyalar.

## 8. Konteyneri ve İmajı Temizleme

İşiniz bittiğinde, gereksiz konteynerleri ve imajları temizlemek için aşağıdaki komutları kullanabilirsiniz:

```sh
docker stop my_django_container

docker rm my_django_container

docker rmi my_django_project
```

## Sonuç

Bu yöntem, sisteminizde Graphviz'i doğrudan kurup PATH'e ekleyemediğiniz durumlarda, Docker ortamında Django model ilişkilerinizi görselleştirmenize olanak tanır. Artık `my_project_visualized.png` dosyanızla model yapınızı inceleyebilirsiniz! 🚀

