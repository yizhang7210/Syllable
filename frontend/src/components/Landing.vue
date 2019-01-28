<template>
  <div class="landing">
    <div class="intro">
      <h3>Welcome to Syllable</h3>
    </div>
    <b-carousel class="demo"
      controls
      indicators
      :interval="4000">
      <b-carousel-slide caption="Explore Syllable"
                        :img-src="require('../../public/demo0.png')"/>
      <b-carousel-slide :img-src="require('../../public/demo1.png')" />
    </b-carousel>
  </div>
</template>

<script>
export default {
  name: 'Landing',
}
</script>
<style scoped lang="scss">
.landing {
  display: flex;
  flex: 1;
  align-items: center;
}
.intro {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100% - $main-section-max-width;
}
.demo {
  display: flex;
  flex: 1;
  margin: $large-margin;
  border: 2px solid $light-grey;
}
</style>
