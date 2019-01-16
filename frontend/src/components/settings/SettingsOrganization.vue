<template>
  <div class="settings-org">
    <div class="title">
      Organization
    </div>

    <div v-if="this.userOrg">
      <div class="subtitle">
        You are {{this.role}} of the Organization {{this.userOrg.name}}.
      </div>
      <div v-if="this.isAdmin">
        <div class="title">
          Access control
        </div>
        <div class="action">
          Give access to everyone with @
          <b-form-input
            v-model="orgDomain"
            class="org-input"
            type="text"
            placeholder="yourcompany.com"
            prefix="@">
          </b-form-input>
          emails.
        </div>
        <b-button
          class="submit-button"
          v-on:click="this.onUpdateDomain"
          :disabled="this.submitting">
          Update
        </b-button>
        <span class="error-message"> {{this.error}} </span>
      </div>

    </div>

    <div v-else>
      <div class="subtitle">
        You are not part of any Organization yet.
      </div>
      <div class="action">
        Create one now:
        <b-form-input
          v-model="newOrgName"
          class="org-input"
          type="text"
          placeholder="Name of your Organization">
        </b-form-input>
      </div>
      <b-button
        class="submit-button"
        v-on:click="this.onCreateOrg"
        :disabled="this.submitting">
        Create
      </b-button>
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
    orgDomain: '',
    submitting: false,
  }),
  mounted() {
    this.$store.dispatch('refreshUser');
    this.orgDomain = this.userOrg && this.userOrg.domain;
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
    },
    onUpdateDomain: function() {
      this.submitting = true;
      http.patch('v1/organizations/' + this.userOrg.id, {
        domain: this.orgDomain
      }).then(() => {
        this.submitting = false;
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
  margin-top: $large-margin;
}
.subtitle {
  margin: $small-margin 0;
}
.org-input {
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
  margin: $small-margin 0;
}
.error-message {
  color: red;
  font-size: $content-font-size;
  margin-left: $small-margin;
}
</style>
