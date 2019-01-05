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
      class="submit-grip"
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
      this.$store.commit('fetchGrips');
    }
  }
}
</script>
<style scoped>
.grip-input {
  display: flex;
  flex-direction: column;
  width: 300px;
  height: 250px;
  margin: 10px;
}
.title {
  display: flex;
  font-weight: bold;
  margin-bottom: 10px;
}
.content {
  display: flex;
  flex: 1;
  font-size: 13px;
}
.submit-grip {
  align-self: flex-end;
  width: 80px;
  text-align: center;
  margin-top: 5px;
}
</style>
