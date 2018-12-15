<template>
  <div id="app">
    <Landing msg="Welcome to Syllable"/>
    <div id="gSignIn" class="g-signin2" data-onsuccess="onSignIn"></div>
    <button class="g-signout" v-on:click="onSignOut">Sign out</button>
  </div>
</template>

<script>
import Landing from './components/Landing.vue'

export default {
  name: 'app',
  components: {
    Landing
  },
  methods: {
    onSignIn: (googleUser) => {
      var profile = googleUser.getBasicProfile();
      console.log('auth response: ' + googleUser.getAuthResponse().id_token);
      console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
      console.log('Name: ' + profile.getName());
      console.log('Image URL: ' + profile.getImageUrl());
      console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    },
    onSignOut: (googleUser) => {
      var auth2 = gapi.auth2.getAuthInstance();
      auth2.signOut().then(function () {
        console.log('User signed out.');
      });
    },
  },
  mounted() {
    gapi.signin2.render('gSignIn', {
      onsuccess: this.onSignIn
    })
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10%;
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
