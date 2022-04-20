from django.db import models
from django.urls import reverse

class Libro(models.Model):

 titulo = models.CharField(max_length=200)
 sinopsis = models.TextField(max_length=1000)
 isbn = models.CharField(max_length=13)
 pags = models.IntegerField(default=0)
 año = models.IntegerField(default=1970)

 class Meta:
    db_table = 'libro'
    ordering = ['titulo']

 def get_absolute_url(self):
    """Devuelve la url para localizar la instancia de un libro concreto"""
    return reverse('libro_detail', args=[str(self.id)])
 def __str__(self):
    """Representación en forma cadena del objeto"""
    return self.isbn
