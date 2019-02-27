<template>
  <div class="grips-container">
    <b-form-input
      class="search"
      type="text"
      @input="this.debouncedSearch"
      placeholder="Search">
    </b-form-input>
    <span class="section-title" v-if="this.showPinnedGrips"> Pinned </span>
    <div class="grip-slide" v-if="this.showPinnedGrips">
        <Grip v-for="grip in pinnedGrips" :key="grip.id" :grip="grip"/>
    </div>
    <span class="section-title" v-if="this.showPinnedGrips"> Others </span>
    <div class="grip-grid">
        <Grip v-for="grip in mainGrips" :key="grip.id" :grip="grip"/>
    </div>
  </div>
</template>

<script>
import Grip from './Grip'
const _ = require('lodash');

export default {
  name: 'GripGrid',
  components: {
    Grip,
  },
  props: [
    'mainGrips',
    'pinnedGrips',
  ],
  computed: {
    showPinnedGrips() {
      return this.pinnedGrips.length > 0
    },
  },
  created() {
    this.debouncedSearch = _.debounce(this.onSearchInput, 400);
  },
  methods: {
    onSearchInput: function(value) {
      if (!value) {
        this.$store.dispatch('fetchAllGrips');
        return;
      }
      this.$store.dispatch('searchGrips', value);
    }
  },
}
</script>
<style scoped lang="scss">
.grips-container {
  display: flex;
  flex-direction: column;
  flex: 1;
  overflow: auto;
}
.grip-slide {
  display: flex;
  overflow: auto;
  margin-right: $big-margin;
}
.grip-grid {
  display: flex;
  flex: 1;
  flex-wrap: wrap;
  overflow: auto;
}
.section-title {
  font-size: $grip-title-font-size;
  font-weight: bold;
  margin: $tiny-margin 0;
}
.search {
  display: flex;
  align-self: center;
  max-width: $main-section-max-width;
  margin: $small-margin 0;
}
</style>
