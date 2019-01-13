<template>
  <div class="settings-org">
    <div class="title">
      Organization
    </div>

    <div v-if="this.userOrg">
      You are {{this.role}} of the Organization {{this.userOrg.name}}.
      <!-- <div v-if="this.isAdmin">
        TODO: Add section on whitelisted domains
      </div> -->
    </div>

    <div v-if="!this.userOrg">
      <div class="subtitle">
        You are not part of any Organization yet.
      </div>
      <div class="action">
        Create one now:
        <b-form-input
          v-model="newOrgName"
          class="new-org"
          type="text"
          placeholder="Name of your Organization">
        </b-form-input>
        <b-button
          class="submit-button"
          v-on:click="this.onCreateOrg"
          :disabled="this.submitting">
          Create
        </b-button>
      </div>
      <span class="error-message"> {{this.error}} </span>
    </div>
  </div>
</template>

<script>
import http from '../../utils/http'

export default {
  name: 'SettingsOrganization',
  computed: {
    userOrg() { return this.$store.state.currentUser.organization },
    isAdmin() { return this.userOrg && this.userOrg.role === 'ADMIN' },
    role() { return this.isAdmin ? 'an Admin' : 'a member' },
  },
  data: () => ({
    error: '',
    newOrgName: '',
    submitting: false,
  }),
  mounted() {
    this.$store.dispatch('refreshUser');
  },
  methods: {
    onCreateOrg: function() {
      this.submitting = true;
      http.post('v1/organizations', {
        name: this.newOrgName
      }).then(() => {
        this.submitting = false;
        this.newOrgName = '';
        this.error = '';
        this.$store.dispatch('refreshUser');
      }).catch((error) => {
        this.submitting = false;
        this.error = error.response.data.detail;
      });
    }
  }
}
</script>
<style scoped lang="scss">
.settings-org {
  display: flex;
  flex-direction: column;
  flex: 1;
  width: $main-section-max-width;
  padding-left: $section-padding;
}
.title {
  display: flex;
  font-size: $section-title-font-size;
  margin: $large-margin 0;
}
.subtitle {
  margin: $small-margin 0;
}
.new-org {
  max-width: 250px;
  margin: $small-margin;
}
.action {
  display: flex;
  align-items: center;
}
.submit-button {
  background-color: $primary-color !important;
  border-width: 0;
  margin: $small-margin;
}
.error-message {
  color: red;
  font-size: $content-font-size;
}
</style>
