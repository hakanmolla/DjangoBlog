from django.shortcuts import render,get_object_or_404
from blog.models import YazilarModel,KategoriModel
from django.core.paginator import Paginator






def kategori(request, kategoriSlug):
    kategori = get_object_or_404(KategoriModel,slug=kategoriSlug)
    
    yazilar = kategori.yazi.order_by('-id')
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar,9)
   
    context={
        'yazilar': paginator.get_page(sayfa),
        'kategor_isim': kategori.isim,
    }
    return render(request,'pages/kategori.html', context)