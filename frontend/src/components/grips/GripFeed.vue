<template>
  <div class="grip-container">
    <GripInput/>
    <div v-for="grip in grips" :key="grip.id">
      <Grip :grip="grip" />
    </div>
  </div>
</template>

<script>
import Grip from './Grip'
import GripInput from './GripInput'

export default {
  name: 'GripFeed',
  components: {
    Grip,
    GripInput,
  },
  props: [
    'grips',
  ],
}
</script>
<style scoped lang="scss">
.grip-container {
  display: flex;
  flex-direction: column;
  align-self: flex-start;
  margin: 0 $big-margin;
  overflow: auto;
}
</style>
