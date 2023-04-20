from django.shortcuts import render



def iletisim(request):
    context={
        'isim':'hakan Mollaahmetoğlu_iletisim Sayfasındasınız'
    }
    return render(request,'pages/iletisim.html', context)