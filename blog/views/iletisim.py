from django.shortcuts import render



def iletisim(request):
    context={
        'sayi':5,
        'isim':'hakan Mollaahmetoğlu',
    }
    return render(request,'pages/iletisim.html', context)