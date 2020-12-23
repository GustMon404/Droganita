from django.db import models
from django.contrib.auth.models import User


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Diretor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Diretores"

    def __str__(self):
        return self.user.username


class Pedido(models.Model):
    produto = models.CharField(max_length=25, null=False, blank=False)
    descricao = models.CharField(max_length=25, null=True, blank=True)
    marca = models.CharField(max_length=15, null=True, blank=True)

    data = models.DateField(auto_now_add=True)

    SITUACAO_CHOICES = [
        ('FT', 'falta'),
        ('PD', 'pedido'),
        ('AB', 'aberto')
    ]

    situacao = models.CharField(max_length=2, choices=SITUACAO_CHOICES, default='AB')

    TIPO_PRODUTO = [
        ('PF', 'Perfumaria'),
        ('SM', 'Similar'),
        ('GN', 'Genérico'),
        ('ET', 'Ético')
    ]

    tipo = models.CharField(max_length=2, choices=TIPO_PRODUTO, default='ET')

    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)

    encomenda = models.BooleanField()
    falta = models.BooleanField()

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.produto

# Create your models here.
