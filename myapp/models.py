from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyProfile(models.Model):
    user = models.OneToOneField(User, 
						on_delete=models.CASCADE, related_name='profile')
    description = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):

    if kwargs.get('created', False):
        MyProfile.objects.create(user=kwargs['instance'])

class Servico(models.Model):
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    data = models.CharField(max_length=10)
    solicitante = models.CharField(max_length=50)
    contato = models.CharField(max_length=13)
    def __str__(self):
        return self.codigo
    def __str__(self):
        return self.descricao
    def __str__(self):
        return self.data
    def __str__(self):
        return self.solicitante
    def __str__(self):
        return self.contato