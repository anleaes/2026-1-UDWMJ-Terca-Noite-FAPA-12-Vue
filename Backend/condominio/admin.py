from django.contrib import admin

from django.contrib import admin
from .models import (
    Sindico, Morador, Condominio, Bloco, Unidade, 
    Salao, Quadra, Veiculo, MoradorVeiculo, 
    UnidadeAreaComum, Reserva, Ocorrencia, 
    FaturaFinanceira, ComprovantePagamento
)

# Registros simples para aparecerem no painel
admin.site.register(Sindico)
admin.site.register(Condominio)
admin.site.register(Bloco)
admin.site.register(Salao)
admin.site.register(Quadra)
admin.site.register(Veiculo)
admin.site.register(MoradorVeiculo)
admin.site.register(UnidadeAreaComum)
admin.site.register(Reserva)
admin.site.register(Ocorrencia)
admin.site.register(FaturaFinanceira)
admin.site.register(ComprovantePagamento)

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('numero', 'andar', 'bloco_id', 'morador_responsavel_id')
    list_filter = ('tipo',)
    search_fields = ('numero',)

@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'is_adimplente')
    search_fields = ('nome', 'cpf')