from rest_framework import serializers
from condominio.models import (
    Sindico, Morador, Condominio, Bloco, Unidade, 
    Salao, Quadra, Veiculo, MoradorVeiculo, UnidadeAreaComum,
    Reserva, Ocorrencia, FaturaFinanceira, ComprovantePagamento
)

class SindicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sindico
        fields = '__all__'

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'

class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = '__all__'

class BlocoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloco
        fields = '__all__'

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'

class SalaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salao
        fields = '__all__'

class QuadraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadra
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

class MoradorVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoradorVeiculo
        fields = '__all__'

class UnidadeAreaComumSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeAreaComum
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

class FaturaFinanceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaturaFinanceira
        fields = '__all__'

class ComprovantePagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprovantePagamento
        fields = '__all__'