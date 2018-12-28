<template>
  <div class="grip">
    <h1>Welcome to Syllable</h1>
  </div>
</template>

<script>
import axios from 'axios';
const SERVER_URL = 'http://localhost:8000/'

export default {
  name: 'Landing',
  data: () => ({
  }),
  mounted() {
  },
  methods: {
  }
}
</script>
<style scoped>
.g-signout {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size: 16px;
  margin-top: 20px;
  border-width: 0;
  width: 120px;
  height: 40px;
}
</style>
