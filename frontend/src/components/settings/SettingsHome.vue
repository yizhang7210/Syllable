<template>
  <div class="settings">
    <SettingsNav/>
    <router-view></router-view>
  </div>
</template>

<script>
import SettingsNav from './SettingsNav'

export default {
  name: 'SettingsHome',
  components: {
    SettingsNav,
  },
}
</script>
<style scoped lang="scss">
.settings {
  display: flex;
  flex-direction: row;
  flex: 1;
}
</style>
