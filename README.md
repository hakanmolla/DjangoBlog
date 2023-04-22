# DjangoBlog
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)


# Blog Sistemi

Bu, Python-Django kullanılarak geliştirilmiş bir blog sistemi projesidir. Bu projede aşağıdaki özellikler bulunmaktadır:

- Yazı ekleme: Kullanıcılar, bloga yeni yazılar ekleyebilirler. Yazılar, başlık, içerik, kategori ve yayın tarihi gibi bilgilerle birlikte kaydedilir.
- Yorum ekleme: Kullanıcılar, yazılara yorumlar ekleyebilirler. Yorumlar, kullanıcı adı, e-posta adresi ve yorum içeriği gibi bilgilerle birlikte kaydedilir.
- Kategori ekleme: Kullanıcılar, yazıları kategorilere ayırabilirler. Kategoriler, isim ve açıklama gibi bilgilerle birlikte kaydedilir.
- Login ve Logout: Kullanıcılar, sisteme giriş yapabilir ve çıkış yapabilirler. Giriş yapmamış kullanıcılar, sadece blog yazılarını okuyabilirler.
- Kullanıcı ekleme: Admin kullanıcıları, sisteme yeni kullanıcılar ekleyebilirler. Kullanıcılar, kullanıcı adı, e-posta adresi ve şifre gibi bilgilerle birlikte kaydedilir.
- Kullanıcı profil düzenleme: Kullanıcılar, kendi profil bilgilerini düzenleyebilirler. Profil bilgileri, kullanıcı adı, e-posta adresi ve profil fotoğrafı gibi bilgileri içerebilir.
- İletişim sayfası: Kullanıcılar, iletişim sayfası aracılığıyla site yöneticisine mesaj gönderebilirler. Mesajlar, isim, e-posta adresi ve mesaj içeriği gibi bilgilerle birlikte kaydedilir.

## Gereksinimler

Bu proje, aşağıdaki yazılımları kullanmaktadır:

- Python 3.x
- Django 3.x
- Django REST Framework 3.x

Projeyi çalıştırmadan önce, yukarıdaki yazılımları sistemine yüklemeniz gerekmektedir.

## Kurulum

Proje kodunu indirip, gerekli bağımlılıkları yükledikten sonra aşağıdaki adımları takip ederek projeyi çalıştırabilirsiniz:

1. Proje kodunu indirin veya kopyalayın.
2. Proje klasörüne gidin ve sanal ortam oluşturun: `python -m venv venv`
3. Sanal ortamı etkinleştirin:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Gerekli bağımlılıkları yükleyin: `pip install -r requirements.txt`
5. Veritabanını oluşturun: `python manage.py migrate`
6. Admin kullanıcısı oluşt