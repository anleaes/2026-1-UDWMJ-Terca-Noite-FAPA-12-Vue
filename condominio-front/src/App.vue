<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8010/api/moradores/'

const moradores = ref([])
const exibindoFormulario = ref(false)
const editando = ref(false)

const formMorador = ref({
  id: null,
  nome: '',
  cpf: '',
  telefone: ''
})

const buscarMoradores = async () => {
  try {
    const response = await axios.get(API_URL)
    moradores.value = response.data
  } catch (error) {
    console.error("Erro ao buscar moradores:", error)
  }
}

const salvarMorador = async () => {
  try {
    if (editando.value) {
      await axios.put(`${API_URL}${formMorador.value.id}/`, formMorador.value)
    } else {
      await axios.post(API_URL, formMorador.value)
    }
  
    await buscarMoradores()
    fecharFormulario()
  } catch (error) {
    alert("Erro ao salvar dados. Verifique os campos ou a conexão com a Oracle.")
    console.error(error)
  }
}

const prepararEdicao = (morador) => {
  formMorador.value = { ...morador }
  editando.value = true
  exibindoFormulario.value = true
}

// Excluir Morador
const excluirMorador = async (id) => {
  if (confirm("Tem certeza que deseja remover este morador do sistema?")) {
    try {
      await axios.delete(`${API_URL}${id}/`)
      await buscarMoradores()
    } catch (error) {
      console.error("Erro ao excluir morador:", error)
    }
  }
}

const abrirNovoCadastro = () => {
  formMorador.value = { id: null, nome: '', cpf: '', telefone: '' }
  editando.value = false
  exibindoFormulario.value = true
}

// Fechar formulário
const fecharFormulario = () => {
  exibindoFormulario.value = false
  editando.value = false
}

// Inicialização
onMounted(() => {
  buscarMoradores()
})
</script>

<template>
  <div class="container mt-5" style="max-width: 900px;">
    
    <div v-if="exibindoFormulario" class="card shadow mb-4 animate-fade-in">
      <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center">
        <h5 class="mb-0">{{ editando ? 'Editar Morador' : 'Cadastrar Novo Morador' }}</h5>
        <button @click="fecharFormulario" class="btn-close btn-close-white" aria-label="Close"></button>
      </div>
      <div class="card-body">
        <form @submit.prevent="salvarMorador">
          <div class="row g-3">
            <div class="col-md-6">
              <label class="form-label fw-semibold">Nome Completo</label>
              <input v-model="formMorador.nome" type="text" class="form-control" placeholder="Ex: João Silva" required>
            </div>
            <div class="col-md-3">
              <label class="form-label fw-semibold">CPF</label>
              <input v-model="formMorador.cpf" type="text" class="form-control" placeholder="000.000.000-00" required>
            </div>
            <div class="col-md-3">
              <label class="form-label fw-semibold">Telefone</label>
              <input v-model="formMorador.telefone" type="text" class="form-control" placeholder="(51) 99999-9999" required>
            </div>
          </div>
          <div class="mt-4 d-flex justify-content-end gap-2">
            <button @click="fecharFormulario" type="button" class="btn btn-secondary px-4">Cancelar</button>
            <button type="submit" class="btn btn-success px-4">
              {{ editando ? 'Salvar Alterações' : 'Salvar no Banco Oracle' }}
            </button>
          </div>
        </form>
      </div>
    </div>

    <div class="card shadow">
      <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center py-3 px-4">
        <h3 class="mb-0 fs-4 fw-bold">Gestão de Condomínio - Moradores</h3>
        <button v-if="!exibindoFormulario" @click="abrirNovoCadastro" class="btn btn-light btn-sm fw-bold px-3">
        </button>
      </div>
      
      <div class="card-body p-0">
        <table class="table table-hover table-striped align-middle mb-0">
          <thead class="table-light">
            <tr>
              <th class="py-3 px-4">Nome</th>
              <th class="py-3">CPF</th>
              <th class="py-3">Telefone</th>
              <th class="py-3 text-end px-4">Ações</th>
            </tr>
          </thead>
          
          <tbody>
            <tr v-for="morador in moradores" :key="morador.id">
              <td class="py-3 px-4 fw-semibold text-secondary">{{ morador.nome }}</td>
              <td class="py-3 text-muted">{{ morador.cpf }}</td>
              <td class="py-3 text-muted">{{ morador.telefone }}</td>
              <td class="py-3 text-end px-4">
                <button @click="prepararEdicao(morador)" class="btn btn-warning btn-sm me-2 fw-semibold px-3">
                  Editar
                </button>
                <button @click="excluirMorador(morador.id)" class="btn btn-danger btn-sm fw-semibold px-3">
                  Excluir
                </button>
              </td>
            </tr>
            
            <tr v-if="moradores.length === 0">
              <td colspan="4" class="text-center text-muted py-5 fs-5">
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</template>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.3s ease-in-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>