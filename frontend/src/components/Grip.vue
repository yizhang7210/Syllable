<template>
  <div class="grip">
    <h3>{{ title }}</h3>
    <span>{{ content }}</span>
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
.g-signout {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size: 16px;
  margin-top: 20px;
  border-width: 0;
  width: 120px;
  height: 40px;
}
</style>
