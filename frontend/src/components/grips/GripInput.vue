<template>
  <div class="grip-input">
    <b-form-input
      class="title"
      v-model="title"
      type="text"
      placeholder="New Grip">
    </b-form-input>
    <b-form-textarea
      class="content"
      v-model="content"
      placeholder="TL;DR"
      :no-resize="true">
    </b-form-textarea>
    <b-button
      class="submit-button"
      v-on:click="this.onClick"
      :disabled="this.isDisabled">
      Post
    </b-button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GripInput',
  data: () => ({
    title: '',
    content: '',
    isDisabled: false,
  }),
  methods: {
    onClick: async function() {
      if (!this.title || !this.content) {
        return;
      }

      this.isDisabled = true;
      await axios.post(this.$store.state.serverUrl + 'v1/grips', {
        title: this.title,
        content: this.content,
        created_by: this.$store.state.currentUser.email
      }, {
        headers: {
          Authorization: 'Bearer ' + this.$store.state.currentUser.token,
        }
      });
      this.title = '';
      this.content = '';
      this.isDisabled = false;
      this.$store.commit('fetchAllGrips');
    }
  }
}
</script>
<style scoped lang="scss">
.grip-input {
  display: flex;
  flex-direction: column;
  width: $grip-width;
  height: $grip-width;
  margin: $small-margin;
}
.title {
  display: flex;
  font-weight: bold;
  margin-bottom: $small-margin;
}
.content {
  display: flex;
  flex: 1;
  font-size: $content-font-size;
}
.submit-button {
  align-self: flex-end;
  min-width: $button-width;
  margin-top: $small-margin;
  border: none;
  background-color: $primary-color;
  color: $light-text-color;
  text-align: center;
}
</style>
