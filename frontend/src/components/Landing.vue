<template>
  <div class="landing">
    <h1>Welcome to Syllable</h1>
    <div id="gSignIn" class="g-signin2" data-onsuccess="onSignIn"></div>
  </div>
</template>

<script>
/* global gapi:false */
import axios from 'axios';

export default {
  name: 'Landing',
  mounted() {
    gapi.signin2.render('gSignIn', {
      onsuccess: this.onSignIn
    })
  },
  methods: {
    onSignIn: async function(googleUser) {
      var profile = googleUser.getBasicProfile();
      const response = await axios.post(this.$store.state.serverUrl+ 'v1/users/signin/google', {
        family_name: profile.getFamilyName(),
        given_name: profile.getGivenName(),
        email: profile.getEmail(),
        token: googleUser.getAuthResponse().id_token,
      });
      this.$store.commit('updateUser', {
        token: response.data.token,
        name: profile.getGivenName()
      });
      this.$router.push('/home');
    },
  }
}
</script>
<style scoped>
.landing {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 100px;
}
</style>
