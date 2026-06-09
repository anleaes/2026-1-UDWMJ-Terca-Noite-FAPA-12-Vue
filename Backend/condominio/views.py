from rest_framework import viewsets
from condominio.models import (
    Sindico, Morador, Condominio, Bloco, Unidade, 
    Salao, Quadra, Veiculo, MoradorVeiculo, UnidadeAreaComum,
    Reserva, Ocorrencia, FaturaFinanceira, ComprovantePagamento
)
from condominio.serializers import *

class SindicoViewSet(viewsets.ModelViewSet):
    queryset = Sindico.objects.all()
    serializer_class = SindicoSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer

class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer

class BlocoViewSet(viewsets.ModelViewSet):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class SalaoViewSet(viewsets.ModelViewSet):
    queryset = Salao.objects.all()
    serializer_class = SalaoSerializer

class QuadraViewSet(viewsets.ModelViewSet):
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class MoradorVeiculoViewSet(viewsets.ModelViewSet):
    queryset = MoradorVeiculo.objects.all()
    serializer_class = MoradorVeiculoSerializer

class UnidadeAreaComumViewSet(viewsets.ModelViewSet):
    queryset = UnidadeAreaComum.objects.all()
    serializer_class = UnidadeAreaComumSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer

class FaturaFinanceiraViewSet(viewsets.ModelViewSet):
    queryset = FaturaFinanceira.objects.all()
    serializer_class = FaturaFinanceiraSerializer

class ComprovantePagamentoViewSet(viewsets.ModelViewSet):
    queryset = ComprovantePagamento.objects.all()
    serializer_class = ComprovantePagamentoSerializer