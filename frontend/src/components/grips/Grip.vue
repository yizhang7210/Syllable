<template>
  <div class="grip">
    <div class="title-line">
      <div class="title">{{ grip.title }}</div>
      <div class="cross" v-on:click="this.onDelete"> x </div>
    </div>
    <span class="content" v-html="this.linkify(grip.content)"></span>
  </div>
</template>

<script>
import axios from 'axios';
import linkifyHtml from 'linkifyjs/html';

export default {
  name: 'Landing',
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
    },
    linkify: (text) => {
      if (text.indexOf('http://') !== -1 || text.indexOf('https://') !== -1) {
        return linkifyHtml(text);
      } else {
        return text;
      }
    }
  }
}
</script>
<style scoped lang="scss">
.grip {
  display: flex;
  flex-direction: column;
  width: $grip-width;
  height: $grip-height;
  margin: $small-margin;
  padding: $tiny-padding;
  border-radius: $primary-border-radius;
  border-width: 1px;
  border-style: solid;
  border-color: black;
}
.title-line {
  display: flex;
  justify-content: space-between;
  font-weight: bold;
  margin-bottom: $tiny-margin;
}
.cross {
  cursor: pointer;
}
.content {
  white-space: pre-wrap;
  word-break: break-all;
  font-size: $content-font-size;
  overflow: scroll;
}
</style>
