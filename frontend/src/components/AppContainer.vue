<template>
  <div class="app-container">
    <MainNav/>
    <router-view></router-view>
  </div>
</template>

<script>
import MainNav from './MainNav'

export default {
  name: 'AppContainer',
  components: {
    MainNav,
  },
}
</script>
<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  flex: 1;
}
</style>
