from django.shortcuts import render, redirect,get_object_or_404
from blog.models import YorumModel
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def yorum_sil(request,id):
    yorum = get_object_or_404(YorumModel,id=id)
    if yorum.yazan == request.user or yorum.yazi.yazar == request.user:
        yorum.delete()
        return redirect('detay',slug=yorum.yazi.slug)
    
    return redirect('anasayfa')
        
    