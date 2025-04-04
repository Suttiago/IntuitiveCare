<template>
  <div>
    <h2>Buscar Operadoras</h2>
    <input v-model="termoBusca" @keyup.enter="buscarOperadoras" placeholder="Digite um nome..."/>
    <button @click="buscarOperadoras">Buscar</button>

    <div v-if="loading">Carregando...</div>
    <div v-if="erro" class="erro">{{ erro }}</div>

    <ul v-if="operadoras.length">
      <li v-for="op in operadoras" :key="op.registro_ans">
        <strong>{{ op.nome_fantasia }}</strong> - {{ op.modalidade }} ({{ op.uf }})
      </li>
    </ul>

    <p v-if="operadoras.length === 0 && !loading && !erro">Nenhuma operadora encontrada.</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      termoBusca: "",
      operadoras: [],
      loading: false,
      erro: "",
    };
  },
  methods: {
    async buscarOperadoras() {
      this.loading = true;
      this.erro = "";
      this.operadoras = [];

      try {
        const response = await axios.get(`http://127.0.0.1:8080/operadoras?q=${this.termoBusca}`);
        this.operadoras = response.data;
      } catch (error) {
        this.erro = error.response?.data?.mensagem || "Erro ao buscar operadoras.";
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.erro {
  color: red;
}
</style>
