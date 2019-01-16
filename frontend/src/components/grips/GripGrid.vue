<template>
  <div class="grip-grid">
    <b-form-input
      class="search"
      type="text"
      @input="this.onSearchInput"
      placeholder="Search">
    </b-form-input>
    <div class="grips-container">
      <div v-for="grip in grips" :key="grip.id">
        <Grip :grip="grip"/>
      </div>
    </div>
  </div>
</template>

<script>
import Grip from './Grip'

export default {
  name: 'GripGrid',
  components: {
    Grip,
  },
  props: [
    'grips',
  ],
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
.grip-grid {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.search {
  display: flex;
  align-self: center;
  max-width: $main-section-max-width;
  margin-top: $small-margin;
}
.grips-container {
  display: flex;
  flex: 1;
  flex-wrap: wrap;
  max-height: $grip-grid-height;
  overflow: scroll;
}
</style>
