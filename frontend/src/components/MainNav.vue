<template>
  <b-navbar class="main-nav" type="dark" variant="info">
    <b-navbar-brand href="#/home"> Syllable </b-navbar-brand>
    <div class="buttons">
      <div
        :style="{visibility: isSignedIn ? 'hidden' : 'visible'}"
        id="gSignIn">
      </div>
      <router-link
        to="/settings"
        class="nav-button"
        tag="button"
        v-if="this.isSignedIn"> Settings
      </router-link>
      <button
        class="nav-button"
        v-if="this.isSignedIn"
        v-on:click="onSignOut"> Sign out
      </button>
    </div>
  </b-navbar>
</template>

<script>
/* global gapi:false */
import http from '../utils/http'
export default {
  name: 'MainNav',
  computed: {
    isSignedIn() {
      return this.$store.state.currentUser;
    },
  },
  mounted() {
    gapi.signin2.render('gSignIn', {
      onsuccess: this.onSignIn
    });
    const checkSignIn = setInterval(() => {
      const googleUser = gapi.auth2.init().currentUser.get();
      if (googleUser && googleUser.isSignedIn()) {
        clearInterval(checkSignIn);
        if (this.$router.currentRoute.path === '/landing') {
          this.$router.push('/home');
        }
      }
    }, 1500);
  },
  methods: {
    onSignIn: async function(googleUser) {
      var profile = googleUser.getBasicProfile();
      const response = await http.post('v1/users/signin/google', {
        family_name: profile.getFamilyName(),
        given_name: profile.getGivenName(),
        email: profile.getEmail(),
        token: googleUser.getAuthResponse().id_token,
      });
      const token = response.data.token;
      this.$store.commit('updateUser', { token });
      this.$store.dispatch('refreshUser');
      if (this.$router.currentRoute.path === '/landing') {
        this.$router.push('/home');
      }
    },
    onSignOut: async function() {
      var auth2 = gapi.auth2.getAuthInstance();
      await auth2.signOut();
      this.$store.commit('clearUser');
      localStorage.removeItem('__syllable');
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
.buttons {
  display: flex;
}
.nav-button {
  font-size: $grip-title-font-size;
  background-color: inherit;
  color: $light-text-color;
  border-width: 0;
  cursor: pointer;
}
</style>
