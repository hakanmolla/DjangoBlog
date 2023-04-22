
from django.urls import path
from account.views import cikis,sifre_degistir,profil_guncelle,kayit_user
from django.contrib.auth import views as auth_views

urlpatterns = [
      path('giris', auth_views.LoginView.as_view(
           template_name='pages/giris.html') , name='giris' ),
     path('cikis', cikis , name='cikis' ),
     path('sifre-degistir', sifre_degistir , name='sifre-degistir' ),
     path('sifre-guncelle', profil_guncelle , name='sifre-guncelle' ),
     path('kayit', kayit_user , name='kayit' ),
     
]
