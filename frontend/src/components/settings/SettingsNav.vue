<template>
  <b-navbar class="settings-nav" type="light" variant="light">
    <b-navbar-nav>
      <b-nav-item to="/settings/organization">Organization</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>

export default {
  name: 'SettingsNav',
  methods: {
  }
}
</script>
<style scoped lang="scss">
.settings-nav {
  display: flex;
  width: 100% - $main-section-max-width;
  justify-content: flex-end;
}
</style>
