<template>
  <div class="landing">
    <h1>Welcome to Syllable</h1>
    <div id="gSignIn" class="g-signin2" data-onsuccess="onSignIn"></div>
  </div>
</template>

<script>
/* global gapi:false */
import http from '../utils/http'

export default {
  name: 'Landing',
  mounted() {
    gapi.signin2.render('gSignIn', {
      onsuccess: this.onSignIn
    })
    const checkSignIn = setInterval(() => {
      const googleUser = gapi.auth2.init().currentUser.get();
      if (googleUser && googleUser.isSignedIn()) {
        clearInterval(checkSignIn);
        this.$router.push('/app/home');
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
      this.$router.push('/app/home');
    },
  },
}
</script>
<style scoped>
.landing {
  display: flex;
  flex: 1;
  flex-direction: column;
  align-items: center;
  margin-top: 100px;
}
</style>
