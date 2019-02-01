<template>
  <div class="settings-org">
    <div class="title">
      Organization
    </div>

    <div v-if="this.userOrg">
      <div class="action">
        You are {{this.role}} of the Organization {{this.userOrg.name}}.
      </div>
      <div class="title">
        Access control
      </div>
      <div v-if="this.isAdmin">
        <div class="subtitle">
          Invite your organization
        </div>
        <div class="action">
          Give access to everyone with @
          <b-form-input
            v-model="orgDomain"
            class="org-input"
            type="text"
            placeholder="yourcompany.com">
          </b-form-input>
          emails.
          <b-button
            class="submit-button"
            v-on:click="this.onUpdateDomain"
            :disabled="this.submitting">
            Update
          </b-button>
        </div>
        <span class="error-message"> {{this.orgError}} </span>
        <span class="success-message"> {{this.orgSuccess}} </span>
      </div>

      <div>
        <div class="subtitle">
          Invite individuals
        </div>
        <div class="action">
          with emails:
          <b-form-input
            v-model="inviteEmails"
            class="email-input"
            type="text"
            placeholder="john@gmail.com, ann@hotmail.com">
          </b-form-input>
          <b-button
            class="submit-button"
            v-on:click="this.onEmailInvite"
            :disabled="this.submitting">
            Invite
          </b-button>
        </div>
        <span class="error-message"> {{this.inviteError}} </span>
        <span class="success-message"> {{this.inviteSuccess}} </span>
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
      <span class="error-message"> {{this.createError}} </span>
      <span class="success-message"> {{this.createSuccess}} </span>
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
    orgError: '',
    orgSuccess: '',
    inviteError: '',
    inviteSuccess: '',
    createError: '',
    createSuccess: '',
    newOrgName: '',
    orgDomain: '',
    submitting: false,
    inviteEmails: '',
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
        this.createError = '';
        this.createSuccess = 'success!';
        this.$store.dispatch('refreshUser');
      }).catch((error) => {
        this.submitting = false;
        this.createError = error.response.data.detail;
        this.createSuccess = '';
      });
    },
    onUpdateDomain: function() {
      this.submitting = true;
      http.patch('v1/organizations/' + this.userOrg.id, {
        domain: this.orgDomain
      }).then(() => {
        this.submitting = false;
        this.orgError = '';
        this.orgSuccess = 'success!';
        this.$store.dispatch('refreshUser');
      }).catch((error) => {
        this.submitting = false;
        this.orgError = error.response.data.detail;
        this.orgSuccess = '';
      });
    },
    onEmailInvite: function() {
      this.submitting = true;
      http.post('v1/organizations/' + this.userOrg.id + '/invite', {
        emails: this.inviteEmails.split(',').map(s => s.trim())
      }).then(() => {
        this.submitting = false;
        this.inviteEmails = '';
        this.inviteError = '';
        this.inviteSuccess = 'success!';
        this.$store.dispatch('refreshUser');
      }).catch((error) => {
        this.submitting = false;
        this.inviteError = error.response.data.detail;
        this.inviteSuccess = '';
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
  margin-top: $big-margin;
}
.subtitle {
  font-size: $subtitle-font-size;
  margin: $small-margin 0;
}
.org-input {
  max-width: 250px;
  margin: $small-margin $tiny-margin;
}
.email-input {
  max-width: 430px;
  margin: $small-margin;
}
.action {
  display: flex;
  align-items: center;
}
.submit-button {
  background-color: $primary-color !important;
  border-width: 0;
  margin: 0 $big-margin;
  min-width: $button-width;
}
.error-message {
  color: $error-message-color;
  font-size: $content-font-size;
}
.success-message {
  color: $success-message-color;
  font-size: $content-font-size;
}
</style>
