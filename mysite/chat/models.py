from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import CASCADE
from datetime import datetime, timedelta
from PIL import Image


class CuentaU(models.Model):
    iduser = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    username = models.CharField(max_length=20)
    foto = models.ImageField(blank=True, null=True, upload_to="images/")
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Chats(models.Model):
    idcuenta = models.ForeignKey(CuentaU, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=23)

    def __str__(self):
        return self.titulo


class Mensajes(models.Model):
    idchat = models.ForeignKey(Chats, on_delete=models.CASCADE)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length=1000)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texto





# Create your models here.
