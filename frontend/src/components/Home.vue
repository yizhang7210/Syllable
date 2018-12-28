<template>
  <div class="home">
    <MainNav/>
    <h1>Get a Grip!</h1>
    <div v-for="grip in grips" :key="grip.id">
      <Grip
        :title="grip.title"
        :content="grip.content">
      </Grip>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Grip from './Grip'
import MainNav from './MainNav'

export default {
  name: 'Home',
  components: {
    Grip,
    MainNav,
  },
  data: () => ({
    grips: []
  }),
  mounted() {
    if (!this.$store.state.currentUser.token) {
      this.$router.push('/landing');
      return;
    }
    this.initGrips();
  },
  methods: {
    initGrips: async function() {
      const response = await axios.get(this.$store.state.serverUrl + 'v1/grips', {
        headers: {
          Authorization: 'Bearer ' + this.$store.state.currentUser.token,
        }
      });
      this.grips = response.data;
    }
  }
}
</script>
<style scoped>

</style>
