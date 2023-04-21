
from django.urls import path
from blog.views import ( iletisim,anasayfa,kategori,yazilarim,
                        detay,YaziEkle,yazi_guncelle,yazi_sil,yorum_sil)





urlpatterns = [
     path('',anasayfa , name='anasayfa'),
     path('iletisim/',iletisim, name='iletisim' ),
     path('yazi-ekle/',YaziEkle, name='yazi-ekle' ),
     path('kategori/<slug:kategoriSlug>',kategori, name='kategori' ),
     path('yazilarim/',yazilarim, name='yazilarim' ),
     path('detay/<slug:slug>',detay, name='detay' ),
     path('yazi-sil/<slug:slug>',yazi_sil, name='yazi-sil' ),
     path('yorum-sil/<int:id>',yorum_sil, name='yorum-sil' ),
     path('yazi-guncelle/<slug:slug>',yazi_guncelle, name='yazi-guncelle' ),
]
