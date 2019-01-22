<template>
  <div class="grip-grid">
    <div class="grips-container">
        <Grip v-for="grip in grips" :key="grip.id" :grip="grip"/>
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
}
</script>
<style scoped lang="scss">
.grip-grid {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.grips-container {
  display: flex;
  flex: 1;
  flex-wrap: wrap;
  max-height: $grip-grid-height;
  overflow: scroll;
}
</style>
