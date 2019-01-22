<template>
  <div class="grips-container">
    <b-form-input
      class="search"
      type="text"
      @input="this.onSearchInput"
      placeholder="Search">
    </b-form-input>
    <span class="section-title" v-if="this.showPinnedGrips"> Pinned </span>
    <div class="grip-slide" v-if="this.showPinnedGrips">
        <Grip v-for="grip in pinnedGrips" :key="grip.id" :grip="grip"/>
    </div>
    <span class="section-title" v-if="this.showPinnedGrips"> Others </span>
    <div class="grip-grid">
        <Grip v-for="grip in allGrips" :key="grip.id" :grip="grip"/>
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
    'allGrips',
    'pinnedGrips',
  ],
  data: () => ({
    showPinnedGrips: false,
  }),
  mounted() {
    this.showPinnedGrips = this.pinnedGrips.length > 0;
  },
  methods: {
    onSearchInput: function(value) {
      if (!value) {
        this.showPinnedGrips = true;
        this.$store.dispatch('fetchAllGrips');
        return;
      }
      this.showPinnedGrips = false;
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
  overflow: scroll;
  margin-right: $large-margin;
}
.grip-grid {
  display: flex;
  flex: 1;
  flex-wrap: wrap;
  max-height: $grip-grid-height;
  overflow: scroll;
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
  margin-top: $small-margin;
}
</style>
