#  Music Player – PyQt + MongoDB

Bu proje, PyQt5 ile geliştirilmiş basit bir masaüstü müzik oynatıcıdır.  
MongoDB kullanılarak kullanıcı giriş/kayıt sistemi entegre edilmiştir.

##  Özellikler

- Kullanıcı girişi ve kayıt sistemi (MongoDB ile)
- Şarkı ekleme ve oynatma (tek oturum)
- Ses seviyesi kontrolü
- Parça süresi göstergesi
- Tema seçimi (Light, Dark, Blue, vb.)
- PyQt5 ile sade ve fonksiyonel arayüz

##  Kullanılan Teknolojiler

- **Python 3.x**
- **PyQt5**
- **MongoDB (Localhost)**
- `pymongo` kütüphanesi

##  Kurulum

1. MongoDB'yi kur ve çalıştır  
2. Gerekli Python kütüphanelerini yükle:
   ```bash
   pip install -r requirements.txt

## Mongo shell'den test kullanıcı oluştur:

use deneme
db.kullanicilar.insertOne({ kullanici_adi: "test", sifre: "123" })

## uygulamayı başlat:

python main.py


