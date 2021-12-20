<template>
  <div class="product-small">
    <div class="product-small__image-wrapper">
      <img src="/image/product/1.png" alt="" class="product-small__image" />
      <a href="#" class="product-small__link">Подробнее</a>
    </div>
    <a href="#" class="product-small__name">
      <span class="company">Ducky </span>
      <span class="name">Shine 7 Blackout</span>
    </a>
    <div class="product-small__switches">
      <div class="product-small__switches-head">Переключатели:</div>
      <ul class="product-small__switches-body">
        <li class="swBrown">Brown</li>
        <li class="swBlue">Blue</li>
        <li class="swRed">Red</li>
        <li class="swClear">Clear</li>
        <li class="swSilentRed">Silent Red</li>
        <li class="swSpeedSilver">Speed Silver</li>
        <li class="swBlack">Black</li>
      </ul>
    </div>
    <div class="product-small__price">
      Цена: от <span>3 000</span> <span>₽</span>
    </div>
  </div>
</template>
<script>
export default {
  name: "ProductBox",
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/css/constants";
@import "../assets/css/product";
</style>
