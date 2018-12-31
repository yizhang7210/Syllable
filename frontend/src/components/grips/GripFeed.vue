<template>
  <div class="grip-container">
    <GripInput/>
    <div v-for="grip in grips" :key="grip.id">
      <Grip
        :title="grip.title"
        :content="grip.content">
      </Grip>
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
<style scoped>
.grip-container {
  display: flex;
  flex: 1;
  flex-direction: column;
  align-self: flex-start;
  max-width: 25%;
  margin-right: 10px;
  overflow: scroll;
}
</style>
