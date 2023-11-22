from django.db import models
from django.utils import timezone

class Itens(models.Model):
    nome_alimento = models.CharField(max_length=30, null=True, blank=True)


    def __str__(self):
        return self.nome_alimento

class Donate(models.Model):
    nome = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=25, null=True, blank=True)

    LOCAL_CHOICES = (
        ('prefeitura', 'prefeitura'),
        ('igreja', 'igreja'),
        ('praca', 'praça')
    )

    local = models.CharField(max_length=50, choices=LOCAL_CHOICES, null=True, blank=True)

    itens = models.ManyToManyField(Itens, related_name='itens_doado')

    data = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.nome