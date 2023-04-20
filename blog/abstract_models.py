from django.db import models


class DateAbstractModel(models.Model):
     olusturma_tarihi = models.DateTimeField(auto_now_add=True)
     duzenleme_tarihi = models.DateTimeField(auto_now=True)
     
     class Meta:
         abstract = True