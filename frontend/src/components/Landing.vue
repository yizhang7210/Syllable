<template>
  <div class="landing">
    <div class="intro">
      <h3> Have you ever ... </h3>
      <ul>
        <li>needed a place to stash your <b> reading digest</b>?</li>
        <li>lost track of that <b> magic script</b>?</li>
        <li>gotten tired of your colleague asking the <b> same question over and over again</b>?</li>
        <li>wondered <b>who decides </b> this policy?</li>
      </ul>
    </div>
    <b-carousel class="demo"
      controls
      indicators
      :interval="4000">
      <b-carousel-slide caption="Syllable"
        caption-tag="h1"
        text-tag="h5"
        text="Never lose track of knowledge again<br/><br/><br/><br/><br/><br/><br/><br/><br/>"
        :img-src="require('../../public/demos/background.png')"/>
      <b-carousel-slide :img-src="require('../../public/demos/sign-up.png')" />
      <b-carousel-slide :img-src="require('../../public/demos/create-grip.png')" />
      <b-carousel-slide :img-src="require('../../public/demos/search-grip.png')" />
      <b-carousel-slide :img-src="require('../../public/demos/invite.png')" />
      <b-carousel-slide :img-src="require('../../public/demos/grip-actions.png')" />
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
  margin: $large-margin;
}
.intro {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  max-width: 30%;
}
li {
  margin: 20px 0;
}
.demo {
  display: flex;
  flex: 1;
  border: 2px solid $light-grey;
}
</style>
