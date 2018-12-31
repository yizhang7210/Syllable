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
  width: 280px;
  height: 250px;
  margin: 10px;
  padding: 5px;
  border-radius: 5px;
  border-width: 1px;
  border-style: solid;
  border-color: black;
}
.title {
  font-weight: bold;
}
.content {
  display: flex;
  flex: 1;
}
</style>
