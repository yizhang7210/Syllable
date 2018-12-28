<template>
  <div class="main-nav">
    <button class="g-signout" v-on:click="onSignOut">
      Sign out of <br/> {{ userName }}
    </button>
  </div>
</template>

<script>
/* global gapi:false */
export default {
  name: 'MainNav',
  computed: {
    userName() {
      return this.$store.state.currentUser.name;
    }
  },
  mounted() {
  },
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
  position: absolute;
  top: 0;
  left: 0;
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
