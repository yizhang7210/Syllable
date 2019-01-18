<template>
  <div class="grip-input-container">
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
        placeholder="TL;DR."
        :no-resize="true">
      </b-form-textarea>
      <b-form-input
        class="source"
        v-model="source"
        type="text"
        size="sm"
        placeholder="a link to where this is from.">
      </b-form-input>
    </div>
    <div class="submit-line">
      <b-button
        class="submit-button"
        v-on:click="this.onClick"
        :disabled="this.isDisabled">
        Post
      </b-button>
      <div v-if="this.hasOrg">
        <input id="is-shared"
          type="checkbox"
          v-model="isShared"/>
        <label for="is-shared" class="is-shared-label">
          Share with your organization
        </label>
      </div>
    </div>
    <span class="error-message"> {{this.error}} </span>
  </div>
</template>

<script>
import http from '../../utils/http'

export default {
  name: 'GripInput',
  computed: {
    hasOrg() { return this.$store.state.currentUser.organization !== null },
  },
  data: () => ({
    title: '',
    content: '',
    source: '',
    error: '',
    isDisabled: false,
    isShared: true,
  }),
  mounted() {
    this.isShared = this.hasOrg;
  },
  methods: {
    onClick: function() {
      if (!this.title) {
        this.error = 'You need a title.'
        return;
      }
      this.isDisabled = true;

      http.post('v1/grips', {
        title: this.title,
        content: this.content,
        created_by: this.$store.state.currentUser.email,
        is_shared: this.isShared,
        source: this.source,
      }).then(() => {
        this.isDisabled = false;
        this.title = '';
        this.content = '';
        this.error = '';
        this.source = '';
        this.$store.dispatch('fetchAllGrips');
      }).catch((error) => {
        this.isDisabled = false;
        this.error = error.response.data.detail;
      });
    }
  }
}
</script>
<style scoped lang="scss">
.grip-input-container {
  margin: $small-margin;
}
.grip-input {
  display: flex;
  flex-direction: column;
  width: $grip-width;
  height: $grip-height;
}
.title {
  display: flex;
  font-weight: bold;
  margin-bottom: $tiny-margin;
}
.content {
  display: flex;
  flex: 1;
  font-size: $content-font-size;
}
.source {
  margin-top: $tiny-margin;
}
.submit-line {
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
  justify-content: space-between;
  font-size: $content-font-size;
  margin-top: $small-margin;
}
.is-shared-label {
  margin: 0 $tiny-margin;
}
.error-message {
  color: red;
  font-size: $content-font-size;
}
.submit-button {
  min-width: $button-width;
  border: none;
  background-color: $primary-color;
  color: $light-text-color;
  text-align: center;
}
</style>
