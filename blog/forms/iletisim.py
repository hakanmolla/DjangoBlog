from django import forms
from blog.models import IletisimModel


# class IletisimForm(forms.Form):
#     email = forms.EmailField(label='E-mail',max_length=100,)
#     isim_soyisim = forms.CharField(label='İsim Soyisim',max_length=25)
#     mesaj = forms.CharField(label='Mesajısınız',widget=forms.Textarea())

class IletisimForm(forms.ModelForm):
    class Meta:
        model=IletisimModel
        fields =('isim_soyisim','email','mesaj')