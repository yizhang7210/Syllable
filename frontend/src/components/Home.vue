<template>
  <div class="home">
    <MainNav/>
    <div class="grids">
      <GripFeed/>
      <GripGrid :grips="this.$store.state.gripsOnGrid"/>
    </div>
  </div>
</template>

<script>
import GripFeed from './grips/GripFeed'
import GripGrid from './grips/GripGrid'
import MainNav from './MainNav'

export default {
  name: 'Home',
  components: {
    GripFeed,
    GripGrid,
    MainNav,
  },
  data: () => ({
    grips: []
  }),
  mounted() {
    if (!this.$store.state.currentUser.token) {
      this.$router.push('/landing');
      return;
    }
    this.$store.commit('fetchGrips');
  },
}
</script>
<style scoped>
.home {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.grids {
  display: flex;
  flex: 1;
}
</style>
