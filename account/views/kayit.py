
from django.shortcuts import render,redirect

from django.contrib import messages
from account.forms import kayitFormu
from django.contrib.auth import login,authenticate



def kayit_user(request):
        if request.method == 'POST':
               form = kayitFormu(request.POST)
               if form.is_valid():
                   form.save()  
                   username = form.cleaned_data.get('username')
                   password = form.cleaned_data.get('password1')
                   user = authenticate(username=username, password=password)
                   login(request,user)
                   return redirect('anasayfa')
                     
        else:
               form = kayitFormu()
            
        return render (request,'pages/kayit.html',context={
            'form':form,
        })