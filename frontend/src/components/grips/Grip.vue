<template>
  <div class="grip">
    <div class="title-line">
      <div class="title">{{ grip.title }}</div>
      <div class="cross" v-on:click="this.onDelete"> x </div>
    </div>
    <span class="content">{{ grip.content }}</span>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Landing',
  data: () => ({
  }),
  props: [
    'grip',
  ],
  mounted() {
  },
  methods: {
    onDelete: async function() {
      const uri = this.$store.state.serverUrl + 'v1/grips/' + this.grip.id;
      const response = await axios.delete(uri, {
        headers: {
          Authorization: 'Bearer ' + this.$store.state.currentUser.token,
        }
      });
      this.$router.go();
    }
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
.title-line {
  display: flex;
  justify-content: space-between;
  font-weight: bold;
}
.cross {
  cursor: pointer;
}
.content {
  display: flex;
  flex: 1;
}
</style>
