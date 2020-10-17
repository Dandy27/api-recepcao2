from django.db import models
from cpf_field.models import CPFField
from phone_field import PhoneField


class Pessoa(models.Model):
    SEXO_CHOICES = (
    (u'Masculino', u'Masculino'),
    (u'Feminino', u'Feminino'),
)
    nome = models.CharField(max_length=255)
    cpf = CPFField('CPF')
    data_de_nascimento = models.DateField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    sexo = models.CharField(max_length=9, null=False, choices=SEXO_CHOICES)
    data = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.nome
        






