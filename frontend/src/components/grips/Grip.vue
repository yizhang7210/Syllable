<template>
  <div class="grip">
    <div class="title-line">
      <div class="title">{{ grip.title }}</div>
      <div class="cross" v-on:click="this.onDelete"> x </div>
    </div>
    <div class="content">{{ grip.content }}</div>
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
  methods: {
    onDelete: async function() {
      const uri = this.$store.state.serverUrl + 'v1/grips/' + this.grip.id;
      await axios.delete(uri, {
        headers: {
          Authorization: 'Bearer ' + this.$store.state.currentUser.token,
        }
      });
      this.$store.commit('fetchAllGrips');
    }
  }
}
</script>
<style scoped>
.grip {
  display: flex;
  flex-direction: column;
  width: 300px;
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
  margin-bottom: 5px;
}
.cross {
  cursor: pointer;
}
.content {
  display: flex;
  flex: 1;
  white-space: pre;
  font-size: 13px;
  overflow: scroll;
}
</style>
