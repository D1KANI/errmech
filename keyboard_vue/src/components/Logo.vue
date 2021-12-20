<template>
  <router-link :to="{name:'Home'}" class="cybr-btn">
    err.mech<span aria-hidden></span>
    <span aria-hidden class="cybr-btn__glitch">err.mech</span>
    <!-- <span aria-hidden class="cybr-btn__tag">R25</span> -->

  </router-link>
</template>

<script>

export default {
  name: "Logo",
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
  @import '../assets/css/constants';
  @import '../assets/css/logo';
</style>
