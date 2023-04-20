from django.contrib import admin
from blog.models import KategoriModel
from blog.models import YazilarModel
from blog.models import YorumModel

admin.site.register(KategoriModel)




# Yorum admin panel
class YorumAdmin(admin.ModelAdmin):
    search_fields=('yazan__username',)
    list_display=(
        'yazan','olusturma_tarihi','guncelleme_tarihi',
    )



admin.site.register(YorumModel,YorumAdmin)






# yazılar admin panel 
class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik','icerik')
    list_display=(
        'baslik','olusturma_tarihi','duzenleme_tarihi',
    )

admin.site.register(YazilarModel,YazilarAdmin)

