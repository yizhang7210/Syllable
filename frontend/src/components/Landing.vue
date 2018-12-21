<template>
  <div class="landing">
    <h1>Welcome to Syllable</h1>
    <div id="gSignIn" class="g-signin2" data-onsuccess="onSignIn"></div>
    <button class="g-signout" v-on:click="onSignOut"> Sign out {{ this.userName }}</button>
  </div>
</template>

<script>
export default {
  name: 'Landing',
  data: () => ({
      userName: ''
  }),
  mounted() {
    gapi.signin2.render('gSignIn', {
      onsuccess: this.onSignIn
    })
  },
  methods: {
    onSignIn(googleUser) {
      var profile = googleUser.getBasicProfile();
      console.log('auth response: ' + googleUser.getAuthResponse().id_token);
      console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
      console.log('Name: ' + profile.getName());
      console.log('Image URL: ' + profile.getImageUrl());
      console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
      this.userName = '(' + profile.getName() + ')';
      console.log(this.userName);
      this.$forceUpdate();

    },
    onSignOut(googleUser) {
      var auth2 = gapi.auth2.getAuthInstance();
      auth2.signOut().then(() => {
        this.userName = '';
        this.$forceUpdate();
      });
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
