<template>
  <div class="home">
    <div class="grids">
      <GripFeed/>
      <GripGrid :grips="this.$store.state.gripsOnGrid"/>
    </div>
  </div>
</template>

<script>
import GripFeed from './grips/GripFeed'
import GripGrid from './grips/GripGrid'

export default {
  name: 'Home',
  components: {
    GripFeed,
    GripGrid,
  },
  data: () => ({
    grips: []
  }),
  mounted() {
    if (!this.$store.state.currentUser.token) {
      this.$router.push('/landing');
      return;
    }
    this.$store.dispatch('fetchAllGrips');
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
