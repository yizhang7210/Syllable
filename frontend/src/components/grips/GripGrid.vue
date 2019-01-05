<template>
  <div class="grip-grid">
    <b-form-input
      class="search"
      v-model="searchTerm"
      type="text"
      placeholder="Search">
    </b-form-input>
    <div class="grip-container">
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
  data: () => ({
    searchTerm: '',
  }),
  props: [
    'grips',
  ],
}
</script>
<style scoped>
.grip-grid {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.search {
  display: flex;
  align-self: center;
  max-width: 75%;
  margin-top: 10px;
}
.grip-container {
  display: flex;
  flex: 1;
  flex-wrap: wrap;
}
</style>
