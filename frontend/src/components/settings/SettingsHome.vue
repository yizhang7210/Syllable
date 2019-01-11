<template>
  <div class="settings">

    adsfa
  </div>
</template>

<script>

export default {
  name: 'SettingsHome',
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
.settings {
  display: flex;
  flex-direction: column;
  flex: 1;
}
</style>
