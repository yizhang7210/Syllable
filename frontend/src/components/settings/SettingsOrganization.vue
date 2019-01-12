<template>
  <div class="settings-org">
    <div v-if="this.userOrg">
      You are {{this.role}} of the Organization {{this.userOrg.name}}.
      <div v-if="this.isAdmin">
        White list
      </div>
    </div>

    <div v-if="!this.userOrg">
      Create an Organization.
      <b-form-input
        v-model="newOrgName"
        class="new-org"
        type="text"
        placeholder="Name of your Organization">
      </b-form-input>
      <span class="error-message"> {{this.error}} </span>
      <b-button
        class="submit-button"
        v-on:click="this.onCreateOrg"
        :disabled="this.submitting">
        Create
      </b-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

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
      axios.post(this.$store.state.serverUrl + 'v1/organizations', {
        name: this.newOrgName
      }, {
        headers: {
          Authorization: 'Bearer ' + this.$store.state.currentUser.token,
        }
      }).then((response) => {
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
  max-width: $main-section-max-width;
}
</style>
