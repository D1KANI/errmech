<template>
  <div class="home">
    <slider-app></slider-app>
    <section class="popular">
      <div class="container">
        <h1>Популярные товары</h1>
        <div class="popular__flex">
          <product-box
            v-for="item in products.items"
            :key="item"
          ></product-box>
        </div>
      </div>
    </section>
    <gradient-app></gradient-app>
    <articles-index></articles-index>
  </div>
</template>

<script>
import SliderApp from '@/components/Slider';
import ProductBox from '@/components/ProductBox';
import ArticlesIndex from '@/components/ArticlesIndex';
import GradientApp from '@/components/GradientApp';

export default {
  name: 'Home',
  components: {
    SliderApp,
    ProductBox,
    ArticlesIndex,
    GradientApp
  },
  data() {
    return {
      products: {
        items: [1, 2, 3, 4, 5, 6, 7]
      },
      title: "ERR MECH"
    }
  }
}
</script>

<style lang="scss" scoped>
.popular {
  margin-top: 100px;
  &__flex {
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    flex-wrap: wrap;
    margin: 0 -20px;
    margin-top: 50px;
  }
}

@media screen and (max-width: 1366px) {
  .popular {
    &__flex {
      justify-content: flex-start;
      margin-right: -15px;
      margin-left: -15px;
    }
  }
}

@media screen and (max-width: 1040px) {
  .popular {
    &__flex {
      justify-content: flex-start;
      margin-right: -10px;
      margin-left: -10px;
    }
  }
}

@media screen and (max-width: 690px) {
  .popular {
    &__flex {
      justify-content: flex-start;
      margin-right: 0;
      margin-left: 0;
    }
  }
}
</style>
