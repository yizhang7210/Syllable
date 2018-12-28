<template>
  <div class="landing">
    <h1>Welcome to Syllable</h1>
    <div id="gSignIn" class="g-signin2" data-onsuccess="onSignIn"></div>
  </div>
</template>

<script>
/* global gapi:false */
import axios from 'axios';
const SERVER_URL = 'http://localhost:8000/'

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
      let response = await axios.post(SERVER_URL+ 'v1/users/signin/google', {
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
.g-signout {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  font-size: 16px;
  margin-top: 20px;
  border-width: 0;
  width: 120px;
  height: 40px;
}
</style>
