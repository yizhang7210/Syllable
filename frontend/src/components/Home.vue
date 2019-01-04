<template>
  <div class="home">
    <MainNav/>
    <GripGrid :grips="this.$store.state.gripsOnGrid"/>
    <GripFeed :grips="this.$store.state.gripsOnGrid"/>
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
  flex-direction: row;
  flex: 1;
  align-items: center;
}
</style>
