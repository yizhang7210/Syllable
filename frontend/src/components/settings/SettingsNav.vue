<template>
  <b-navbar class="settings-nav" type="light" variant="light">
    <b-navbar-nav>
      <b-nav-item href="#/app/settings/organization">Organization</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>

export default {
  name: 'SettingsNav',
  methods: {
    onSignOut: async function() {
      var auth2 = gapi.auth2.getAuthInstance();
      await auth2.signOut();
      this.$store.commit('updateUser', null);
      this.$router.push('/landing');
    },
  }
}
</script>
<style scoped lang="scss">
.settings-nav {
  display: flex;
}
</style>
