<template>
  <div id="app">
    <Landing/>
  </div>
</template>

<script>
import Landing from './components/Landing.vue'

export default {
  name: 'app',
  components: {
    Landing
  }
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
