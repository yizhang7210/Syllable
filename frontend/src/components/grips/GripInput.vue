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
    <div class="submit-line">
      <span class="error-message"> {{this.error}} </span>
      <b-button
        class="submit-button"
        v-on:click="this.onClick"
        :disabled="this.isDisabled">
        Post
      </b-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GripInput',
  data: () => ({
    title: '',
    content: '',
    error: '',
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
      })
      .then((response) => {
        this.isDisabled = false;
        this.title = '';
        this.content = '';
        this.error = '';
        this.$store.commit('fetchAllGrips');
      })
      .catch((error) => {
        this.isDisabled = false;
        this.error = error.response.data.detail;
        return;
      });
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
.submit-line {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.error-message {
  flex: 1;
  color: red;
  font-size: $content-font-size;
}
.submit-button {
  min-width: $button-width;
  margin-top: $small-margin;
  border: none;
  background-color: $primary-color;
  color: $light-text-color;
  text-align: center;
}
</style>
