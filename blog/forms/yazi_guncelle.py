from django import forms
from blog.models import YazilarModel


class YaziGuncelleModelForm(forms.ModelForm):
    class Meta:
        model = YazilarModel
        exclude=('yazar','slug')  #(bunların dışındaki hepsini kullanmak istiyorum deme)
        # fields = ('resim','baslik','icerik','kategoriler')