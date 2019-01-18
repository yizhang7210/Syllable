<template>
  <div class="grip-container"
    @mouseover="showActionBar = true"
    @mouseleave="showActionBar = false">

    <div v-if="this.hasOrg" class="left-bar">
      <div
        v-bind:class="['votes', grip.has_voted ? 'voted' : 'not-voted']"
        v-on:click="this.toggleVote">
        {{ grip.votes }}
      </div>
      <div class="action-bar" v-if="this.grip.is_editable && this.showActionBar">
        <span v-on:click="this.deleteGrip"><i class="fas fa-times"></i></span>
        <div>
          <span v-if="!grip.is_shared" v-on:click="this.shareGrip">
            <i class="fas fa-share"></i>
          </span>
          <span v-else v-on:click="this.unshareGrip">
            <i class="fas fa-arrow-circle-left"></i>
          </span>
        </div>
      </div>
    </div>
    <div v-else class="left-bar">
      <div class="action-bar">
        <span v-on:click="this.deleteGrip">
          <i class="fas fa-times"></i>
        </span>
      </div>
    </div>

    <div v-bind:class="['grip', this.grip.is_shared ? 'shared' : 'not-shared']">
      <div class="title">{{ grip.title }}</div>
      <span class="content"> {{grip.content}} </span>
      <span class="source" v-if="grip.source">
        source: &nbsp;
        <a v-if="validations.isLink(grip.source)"
          v-bind:href="grip.source" target="_blank"> click here </a>
        <span v-else> {{ grip.source }} </span>
      </span>
    </div>
  </div>
</template>

<script>
import http from '../../utils/http'
import validations from '../../utils/validations'

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
    validations: validations,
  }),
  methods: {
    deleteGrip: async function() {
      await http.delete('v1/grips/' + this.grip.id);
      this.$store.dispatch('fetchAllGrips');
    },
    shareGrip: async function() {
      await http.patch('v1/grips/' + this.grip.id, {share: true});
      this.$store.dispatch('fetchAllGrips');
      this.showActionBar = false;
    },
    unshareGrip: async function() {
      await http.patch('v1/grips/' + this.grip.id, {share: false});
      this.$store.dispatch('fetchAllGrips');
      this.showActionBar = false;
    },
    toggleVote: async function() {
      if (this.grip.has_voted) {
        await http.post('v1/grips/' + this.grip.id + '/action', {vote: false});
      } else {
        await http.post('v1/grips/' + this.grip.id + '/action', {vote: true});
      }
      this.$store.dispatch('fetchAllGrips');
    },
  }
}
</script>
<style scoped lang="scss">
.grip-container {
  display: flex;
  flex-direction: row;
  margin: $small-margin;
}
.grip {
  display: flex;
  flex: 1;
  flex-direction: column;
  width: $grip-width;
  height: $grip-height;
  border-radius: $primary-border-radius;
  border: 1px solid $light-grey;
  padding: $small-padding;
}
.left-bar {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  color: $primary-color;
  margin: $tiny-margin;
}
.shared {
  background-color: $shared-grip;
}
.not-shared {
  background-color: $not-shared-grip;
}
.action-bar {
  display: flex;
  flex-direction: column-reverse;
  align-items: center;
  cursor: pointer;
}
.title {
  display: flex;
  font-weight: bold;
  margin-bottom: $tiny-margin;
  overflow: scroll;
}
.content {
  flex: 1;
  white-space: pre-wrap;
  word-break: break-all;
  font-size: $content-font-size;
  overflow: scroll;
}
.source {
  display: flex;
  justify-content: center;
  margin-top: $tiny-margin;
  font-size: $content-font-size;
}
.votes {
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: $small-border-radius;
  width: 20px;
  cursor: pointer;
}
.voted {
  background-color: $primary-color-light;
  color: white;
}
.not-voted {
  background-color: white;
  color: black;
  border: 1px solid black;
}
</style>
