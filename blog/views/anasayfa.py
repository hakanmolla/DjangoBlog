from django.shortcuts import render
from blog.models import YazilarModel
from django.core.paginator import Paginator





def anasayfa(request):
    yazilar = YazilarModel.objects.order_by('-id')
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar,9)
    print(paginator.get_page(sayfa))
    context={
        'yazilar': paginator.get_page(sayfa)
    }
    return render(request,'pages/anasayfa.html', context)