from django import forms
from blog.models import YazilarModel


class YaziEkleModelForm(forms.ModelForm):
    class Meta:
        model = YazilarModel
        exclude=('yazar','slug')  #(bunların dışındaki hepsini kullanmak istiyorum deme)
        # fields = ('resim','baslik','icerik','kategoriler')