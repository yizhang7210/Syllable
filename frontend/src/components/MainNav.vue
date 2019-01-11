<template>
  <b-navbar class="main-nav" type="dark" variant="info">
    <b-navbar-brand href="#/app/home"> Syllable </b-navbar-brand>
    <div>
      <router-link to="/app/settings" class="nav-button" tag="button">
        Settings
      </router-link>
      <button class="nav-button" v-on:click="onSignOut">
        Sign out
      </button>
    </div>
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
.gear {
  font-family: $primary-font-family;
  font-size: $title-font-size;
  background-color: inherit;
  color: $light-text-color;
  border-width: 0;
  cursor: pointer;
}
.nav-button {
  font-family: $primary-font-family;
  font-size: $title-font-size;
  background-color: inherit;
  color: $light-text-color;
  border-width: 0;
  cursor: pointer;
}
</style>
