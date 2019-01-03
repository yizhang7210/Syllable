<template>
  <div class="grip-container">
    <div v-for="grip in grips" :key="grip.id">
      <Grip :grip="grip"/>
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
<style scoped>
.grip-container {
  display: flex;
  align-self: flex-start;
  flex-direction: row;
  flex-wrap: wrap;
  flex: 1;
}
</style>
