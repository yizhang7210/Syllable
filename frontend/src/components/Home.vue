<template>
  <div class="home">
    <MainNav/>
    <GripGrid :grips="grips"/>
    <GripFeed :grips="grips"/>
  </div>
</template>

<script>
import axios from 'axios';
import GripFeed from './grips/GripFeed'
import GripGrid from './grips/GripGrid'
import MainNav from './MainNav'

export default {
  name: 'Home',
  components: {
    GripFeed,
    GripGrid,
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
</style>
