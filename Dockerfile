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
