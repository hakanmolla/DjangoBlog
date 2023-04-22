from django.shortcuts import render, redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel
from django.views.generic import FormView


class IletisimFormView(FormView):
    template_name = 'pages/iletisim.html'
    form_class = IletisimForm
    success_url = '/email-gonderildi'

    def form_valid(self, form):
        form.save()
        form.send_email(mesaj=form.cleaned_data.get('mesaj'))
        return super().form_valid(form)






# from django.shortcuts import render,redirect
# from blog.forms import IletisimForm
# from blog.models import IletisimModel



# def iletisim(request):
#     form = IletisimForm(
#     #     initial={
#     #     'isim_soyisim':'hakanMollaahmetoğlu',
        
#     # }
#         )
#     if request.method == 'POST':
#         form = IletisimForm(request.POST)
#         if form.is_valid():
#         #    iletisim = IletisimModel()
#         #    iletisim.email = form.cleaned_data['email']
#         #    iletisim.isim_soyisim =form.cleaned_data['isim_soyisim']
#         #    iletisim.mesaj =form.cleaned_data['mesaj']
#         #    iletisim.save()
#         #    ModelForm olduğu için 
#             form.save()
#             return redirect('anasayfa')
#         else:
#             print('valid Değil')
        
        
        
        
        
        
#     context={
#         'form': form,
#     }
#     return render(request,'pages/iletisim.html', context)