<template>
  <div class="settings-org">
    abcde
  </div>
</template>

<script>
export default {
  name: 'SettingsOrganization',
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
.settings-org {
  display: flex;
  flex-direction: column;
  flex: 1;
  max-width: $main-section-max-width;
}
</style>
