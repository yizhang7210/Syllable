<template>
  <div class="landing">
    <h1>Welcome to Syllable</h1>
    <div id="gSignIn" class="g-signin2" data-onsuccess="onSignIn"></div>
    <button v-if="userName" class="g-signout" v-on:click="onSignOut">
      Sign out of <br/> {{ this.userName }}
    </button>
  </div>
</template>

<script>
import axios from 'axios';
const SERVER_URL = 'http://localhost:8000/'

export default {
  name: 'Landing',
  data: () => ({
      userName: null,
  }),
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
      this.$store.commit('updateUserToken', response.data.token);
      this.userName = profile.getName();
    },
    onSignOut: async function() {
      var auth2 = gapi.auth2.getAuthInstance();
      await auth2.signOut();
      this.userName = null;
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
