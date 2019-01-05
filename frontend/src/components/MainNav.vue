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
<style scoped>
.main-nav {
  display: flex;
  background-color: #008CBA !important;
}
.g-signout {
  display: flex;
  align-self: flex-end;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size: 16px;
  border-width: 0;
  height: 40px;
  background-color: inherit;
  color: white;
}
</style>
