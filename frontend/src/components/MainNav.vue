<template>
  <b-navbar class="main-nav" type="dark" variant="info">
    <b-navbar-brand href="#/landing"> Syllable </b-navbar-brand>
    <button class="g-signout" v-on:click="onSignOut">
      Sign out
    </button>
  </b-navbar>
</template>

<script>
/* global gapi:false */
export default {
  name: 'MainNav',
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
.main-nav {
  display: flex;
  background-color: $primary-color !important;
}
.g-signout {
  display: flex;
  font-family: $primary-font-family;
  font-size: $title-font-size;
  background-color: inherit;
  color: $light-text-color;
  border-width: 0;
  cursor: pointer;
}
</style>
