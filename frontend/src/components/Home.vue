<template>
  <div class="home">
    <MainNav/>
    <div class="grip-container">
      <div v-for="grip in grips" :key="grip.id">
        <Grip
          :title="grip.title"
          :content="grip.content">
        </Grip>
      </div>
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
.home {
  display: flex;
  flex-direction: row;
  flex: 1;
  align-items: center;
}
.grip-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  flex: 1;
}
</style>
