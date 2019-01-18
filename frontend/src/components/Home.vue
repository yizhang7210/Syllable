<template>
  <div class="home">
    <b-form-input
      class="search"
      type="text"
      @input="this.onSearchInput"
      placeholder="Search">
    </b-form-input>

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
    if (!this.$store.state.currentUser) {
      this.$router.push('/landing');
      return;
    }
    this.$store.dispatch('fetchAllGrips');
  },
  methods: {
    onSearchInput: function(value) {
      if (!value) {
        this.$store.dispatch('fetchAllGrips');
        return;
      }
      this.$store.dispatch('searchGrips', value);
    }
  }
}
</script>
<style scoped lang="scss">
.home {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.grids {
  display: flex;
  flex: 1;
}
.search {
  display: flex;
  align-self: center;
  max-width: $main-section-max-width;
  margin-top: $small-margin;
}
</style>
