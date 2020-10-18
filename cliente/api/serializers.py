from rest_framework.serializers import ModelSerializer
from cliente.models import Pessoa

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'cpf', 'data_de_nascimento', 'phone', 'sexo', 'data')
