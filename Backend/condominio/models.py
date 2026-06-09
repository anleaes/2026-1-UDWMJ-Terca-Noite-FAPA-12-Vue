from django.db import models

from django.db import models

# =================
# CLASSES ABSTRATAS 
# =================
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    senha_hash = models.CharField(max_length=255)

    class Meta:
        abstract = True 

class AreaComum(models.Model):
    nome = models.CharField(max_length=100)
    taxa_reserva = models.DecimalField(max_digits=10, decimal_places=2)
    capacidade_maxima = models.IntegerField()
    horario_funcionamento = models.CharField(max_length=100)

    class Meta:
        abstract = True

# ==================================
# CLASSES QUE VÃO HERDAR DO USUARIO
# ==================================
class Sindico(Usuario):
    inicio_mandato = models.DateField()
    fim_mandato = models.DateField()
    status_gestao = models.CharField(max_length=20, default="Ativo")

    def __str__(self):
        return f"Síndico: {self.nome}"

class Morador(Usuario):
    eh_proprietario = models.BooleanField(default=True)
    is_adimplente = models.BooleanField(default=True)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Morador: {self.nome}"

class Condominio(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    telefone_portaria = models.CharField(max_length=20)
    total_vagas_visitantes = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Bloco(models.Model):
    nome = models.CharField(max_length=50)
    total_andares = models.IntegerField()
    total_unidades_por_andar = models.IntegerField()
    condominio_id = models.ForeignKey(Condominio, on_delete=models.CASCADE, db_column='condominio_id')

    def __str__(self):
        return f"{self.nome}"

class Unidade(models.Model):
    numero = models.CharField(max_length=10)
    andar = models.IntegerField()
    tipo = models.CharField(max_length=50, default="Apartamento")
    fracao_ideal = models.DecimalField(max_digits=10, decimal_places=4)
    bloco_id = models.ForeignKey(Bloco, on_delete=models.CASCADE, db_column='bloco_id')
    morador_responsavel_id = models.ForeignKey(Morador, on_delete=models.SET_NULL, null=True, blank=True, db_column='morador_responsavel_id')

    def __str__(self):
        return f"Apto {self.numero}"

# ==============
# ÁREAS COMUNS 
# =============
class Salao(AreaComum):
    permite_som_alto = models.BooleanField(default=True)
    quantidade_cadeiras = models.IntegerField()
    tipo_cozinha = models.CharField(max_length=50)

class Quadra(AreaComum):
    tipo_piso = models.CharField(max_length=50)
    possui_iluminacao_noturna = models.BooleanField(default=False)
    esporte_principal = models.CharField(max_length=50)

# =============================
# RELACIONAMENTOS MANY-TO-MANY 
# =============================
class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    data_registro_veiculo = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

class MoradorVeiculo(models.Model):
    morador_id = models.ForeignKey(Morador, on_delete=models.CASCADE, db_column='morador_id')
    veiculo_id = models.ForeignKey(Veiculo, on_delete=models.CASCADE, db_column='veiculo_id')
    data_vinculo = models.DateField(auto_now_add=True)
    is_veiculo_principal = models.BooleanField(default=True)

class UnidadeAreaComum(models.Model):
    data_liberacao_acesso = models.DateField(auto_now_add=True)
    is_bloqueado_por_inadimplencia = models.BooleanField(default=False)
    unidade_id = models.ForeignKey(Unidade, on_delete=models.CASCADE, db_column='unidade_id')
    salao_id = models.ForeignKey(Salao, on_delete=models.CASCADE, null=True, blank=True, db_column='salao_id')
    quadra_id = models.ForeignKey(Quadra, on_delete=models.CASCADE, null=True, blank=True, db_column='quadra_id')

# ==========================================
# FLUXOS DE NEGÓCIO (RESERVA, OCORRÊNCIA, FINANCEIRO)
# ==========================================
class Reserva(models.Model):
    data_reserva = models.DateField()
    status = models.CharField(max_length=20, default="Pendente")
    valor_cobrado = models.DecimalField(max_digits=10, decimal_places=2)
    data_solicitacao = models.DateField(auto_now_add=True)
    morador_id = models.ForeignKey(Morador, on_delete=models.CASCADE, db_column='morador_id')
    salao_id = models.ForeignKey(Salao, on_delete=models.CASCADE, null=True, blank=True, db_column='salao_id')
    quadra_id = models.ForeignKey(Quadra, on_delete=models.CASCADE, null=True, blank=True, db_column='quadra_id')

class Ocorrencia(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    data_registro = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Aberta")
    resposta_sindico = models.TextField(null=True, blank=True)
    morador_id = models.ForeignKey(Morador, on_delete=models.CASCADE, db_column='morador_id')
    salao_id = models.ForeignKey(Salao, on_delete=models.CASCADE, null=True, blank=True, db_column='salao_id')
    quadra_id = models.ForeignKey(Quadra, on_delete=models.CASCADE, null=True, blank=True, db_column='quadra_id')

class FaturaFinanceira(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    status_pagamento = models.CharField(max_length=20, default="Pendente")
    codigo_barras = models.CharField(max_length=48)
    data_emissao = models.DateField(auto_now_add=True)
    unidade_id = models.ForeignKey(Unidade, on_delete=models.CASCADE, db_column='unidade_id')

class ComprovantePagamento(models.Model):
    autenticacao_bancaria = models.CharField(max_length=100)
    data_pagamento = models.DateField()
    canal_pagamento = models.CharField(max_length=50)
    fatura_id = models.OneToOneField(FaturaFinanceira, on_delete=models.CASCADE, db_column='fatura_id') # OneToOne