<template>
  <div>
    <h1>Buscar Operadoras</h1>
    <input v-model="termoBusca" @input="buscarOperadoras" placeholder="Digite o nome da operadora" />
    <ul>
      <li v-for="operadora in operadoras" :key="operadora.RegistroANS">
        {{ operadora.NomeFantasia }} - {{ operadora.RazaoSocial }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      termoBusca: "",
      operadoras: [],
    };
  },
  methods: {
    async buscarOperadoras() {
      if (this.termoBusca.length < 2) {
        this.operadoras = [];
        return;
      }
      try {
        const response = await axios.get(`http://127.0.0.1:5000/buscar?termo=${this.termoBusca}`);
        this.operadoras = response.data;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
      }
    },
  },
};
</script>

<style>
input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
}
</style>
