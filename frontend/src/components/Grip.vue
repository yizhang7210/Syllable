<template>
  <div class="grip">
    <span class="title">{{ title }}</span>
    <span class="content">{{ content }}</span>
  </div>
</template>

<script>
export default {
  name: 'Landing',
  data: () => ({
  }),
  props: [
    'title',
    'content',
  ],
  mounted() {
  },
  methods: {
  }
}
</script>
<style scoped>
.grip {
  display: flex;
  flex-direction: column;
  border-radius: 5px;
  border-width: 1px;
  border-style: solid;
  border-color: black;
  padding: 5px;
  width: 250px;
  height: 250px;
  margin: 10px;
}
.title {
  font-weight: bold;
}
</style>
