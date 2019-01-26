<template>
  <div class="home">
    <div class="grids">
      <GripFeed/>
      <GripGrid
        :mainGrips="this.$store.state.mainGrips"
        :pinnedGrips="this.$store.state.pinnedGrips"/>
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
  mounted() {
    if (!this.$store.state.currentUser) {
      this.$router.push('/landing');
      return;
    }
    this.$store.dispatch('fetchAllGrips');
  },
}
</script>
<style scoped lang="scss">
.home {
  display: flex;
  flex-direction: column;
  flex: 1;
  max-width: 100vw;
  max-height: 100vh;
  margin-bottom: $small-margin;
}
.grids {
  display: flex;
  flex: 1;
}
</style>
