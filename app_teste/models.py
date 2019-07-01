from django.db import models

# Create your models here.
class Equipe(models.Model):
    nome = models.CharField(max_length=250)
    quantidade_integrantes = models.IntegerField()
    descricao = models.CharField(max_length=250)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    sobrenome = models.CharField(max_length=250)
    data_nascimento = models.DateTimeField()
    idade = models.IntegerField()
    nota = models.DecimalField(max_digits = 4, decimal_places=2)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome