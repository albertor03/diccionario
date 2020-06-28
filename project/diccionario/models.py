from django.db import models
from datetime import datetime

# Create your models here.


class Letra(models.Model):
    id = models.AutoField(primary_key=True)
    letra = models.CharField(max_length=10)
    created_at = models.DateTimeField(datetime.now, auto_now_add=True, blank=True, null=False)
    updated_at = models.DateTimeField(datetime.now, auto_now=True, blank=True, null=False)

    def __str__(self):
        return self.letra

    def __unicode__(self):
        return


class Termino(models.Model):
    id = models.AutoField(primary_key=True)
    termino = models.CharField(max_length=100)
    letra = models.ForeignKey(Letra, on_delete=models.CASCADE)
    created_at = models.DateTimeField(datetime.now, auto_now_add=True, blank=True, null=False)
    updated_at = models.DateTimeField(datetime.now, auto_now=True, blank=True, null=False)

    def __str__(self):
        return self.termino

    def __unicode__(self):
        return


class Definicion(models.Model):
    id = models.AutoField(primary_key=True)
    definicion = models.TextField(blank=True, null=True)
    termino = models.ForeignKey(Termino, on_delete=models.CASCADE)
    created_at = models.DateTimeField(datetime.now, auto_now_add=True, blank=True, null=False)
    updated_at = models.DateTimeField(datetime.now, auto_now=True, blank=True, null=False)

    def __str__(self):
        return self.definicion

    def __unicode__(self):
        return
