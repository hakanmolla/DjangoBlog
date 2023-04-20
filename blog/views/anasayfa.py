from django.shortcuts import render



def anasayfa(request):
    context={
        'isim':'hakan Mollaahmetoğlu_Anasayfadasınız'
    }
    return render(request,'pages/anasayfa.html', context)