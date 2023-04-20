from django.contrib import admin
from blog.models import KategoriModel
from blog.models import YazilarModel
from blog.models import YorumModel
from blog.models import IletisimModel

admin.site.register(KategoriModel)


# iletisim admin panel
@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    search_fields=('email',)
    list_display=(
        'email','olusturma_tarihi',
    )


# Yorum admin panel
@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    search_fields=('yazan__username',)
    list_display=(
        'yazan','olusturma_tarihi','duzenleme_tarihi',
    )

# yazılar admin panel 
@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik','icerik')
    list_display=(
        'baslik','olusturma_tarihi','duzenleme_tarihi',
    )
