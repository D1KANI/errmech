<template>
  <div id="app">
    <div class="page-wrapper">
      <header-app></header-app>
      <main class="main">
        <router-view></router-view>
      </main>
      <footer-app></footer-app>
    </div>
  </div>
</template>

<script>
import HeaderApp from '@/components/Header';
import FooterApp from '@/components/Footer';

export default ({
  name: 'layout',
  components: {
    HeaderApp,
    FooterApp,
  },
  // mounted() {
  //   this.$toasted.show('Товар добавлен в корзину', {
  //     theme: "toasted-primary", 
  //     position: "bottom-right", 
  //     duration : 5000,
  //     type: 'success',
  //     action : {
  //         text : 'Закрыть',
  //         onClick : (e, toastObject) => {
  //             toastObject.goAway(0);
  //         }
  //     },
  //   })
  // }

})
</script>


<style lang="scss">
  @import 'assets/css/constants';
  @import 'assets/css/base';
</style>
