<template>
  <div v-bind:class="['grip-container', this.grip.is_shared ? 'shared' : 'not-shared']"
    @mouseover="showActionBar = true"
    @mouseleave="showActionBar = false">
    <div class="grip">
      <div class="title">{{ grip.title }}</div>
      <span class="content" v-html="this.linkify(grip.content)"></span>
    </div>
    <div class="action-bar" v-if="this.grip.is_editable && this.showActionBar">
      <span v-on:click="this.onDelete"><i class="fas fa-times"></i></span>
      <div v-show="this.hasOrg">
        <span v-if="!this.grip.is_shared" v-on:click="this.shareGrip">
          <i class="fas fa-share"></i>
        </span>
        <span v-else v-on:click="this.unshareGrip">
          <i class="fas fa-arrow-circle-left"></i>
        </span>
      </div>

    </div>
  </div>
</template>

<script>
import http from '../../utils/http'
import linkifyHtml from 'linkifyjs/html';

export default {
  name: 'Landing',
  props: [
    'grip',
  ],
  computed: {
    hasOrg() {
      return this.$store.state.currentUser.organization !== null
    },
    isAdmin() {
      const currentUser = this.$store.state.currentUser;
      return currentUser.organization && currentUser.organization.role === 'ADMIN';
    },
  },
  data: () => ({
    showActionBar: false,
  }),
  methods: {
    onDelete: async function() {
      await http.delete('v1/grips/' + this.grip.id);
      this.$store.dispatch('fetchAllGrips');
    },
    shareGrip: async function() {
      await http.post('v1/grips/' + this.grip.id, {share: true});
      this.$store.dispatch('fetchAllGrips');
      this.showActionBar = false;
    },
    unshareGrip: async function() {
      await http.post('v1/grips/' + this.grip.id, {share: false});
      this.$store.dispatch('fetchAllGrips');
      this.showActionBar = false;
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
.grip-container {
  display: flex;
  flex-direction: column;
  width: $grip-width;
  height: $grip-height;
  margin: $small-margin;
  border-radius: $primary-border-radius;
  border: 1px solid $light-grey;
  justify-content: space-between;
}
.grip {
  display: flex;
  flex-direction: column;
  padding: $small-padding;
}
.action-bar {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
  color: $primary-color;
  cursor: pointer;
  margin: $tiny-margin;
}
.shared {
  background-color: $shared-grip;
}
.not-shared {
  background-color: $not-shared-grip;
}
.title {
  font-weight: bold;
  margin-bottom: $tiny-margin;
}
.content {
  white-space: pre-wrap;
  word-break: break-all;
  font-size: $content-font-size;
  overflow: scroll;
}
</style>
