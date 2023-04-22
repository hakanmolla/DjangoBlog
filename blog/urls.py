
from django.urls import path
from blog.views import ( IletisimFormView,anasayfa,kategori,yazilarim,
                        detay,YaziEkleCreateView,yazi_guncelle,yazi_sil,yorum_sil)
from django.views.generic import TemplateView, RedirectView





urlpatterns = [
     path('',anasayfa , name='anasayfa'),
     path('iletisim/',IletisimFormView.as_view(), name='iletisim' ),
     path('yazi-ekle/',YaziEkleCreateView.as_view(), name='yazi-ekle' ),
     path('email-gonderildi', TemplateView.as_view(
        template_name = 'pages/email-gonderildi.html'
    ), name='email-gonderildi'),
     path('kategori/<slug:kategoriSlug>',kategori, name='kategori' ),
     path('yazilarim/',yazilarim, name='yazilarim' ),
     path('detay/<slug:slug>',detay, name='detay' ),
     path('yazi-sil/<slug:slug>',yazi_sil, name='yazi-sil' ),
     path('yorum-sil/<int:id>',yorum_sil, name='yorum-sil' ),
     path('yazi-guncelle/<slug:slug>',yazi_guncelle, name='yazi-guncelle' ),
]
