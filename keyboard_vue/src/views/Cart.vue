<template>
  <section class="cart">
    <div class="container">
      <h1>Корзина</h1>
      <div class="cart-wrapper">
        <div class="cart__flex">
          <div class="cart-box">
            <div v-if="!cartLength" class="cart__content">
              <div class="cart-item">
                <div class="cart-item-image">
                  <img
                    src="/image/item/item.png"
                    alt=""
                    class="cart-item-image__img"
                  />
                </div>
                <div class="cart-item__inner">
                  <p class="cart-item__category">Клавиатура</p>
                  <p class="cart-item__name">Varmilo VA87M Vintage Days</p>
                  <div class="cart-item-count">
                    <div class="count">
                      <div class="count-minus count__btn">-</div>
                      <input
                        type="text"
                        name=""
                        id=""
                        class="count-value"
                        value="1"
                        readonly
                      />
                      <div class="count-plus count__btn">+</div>
                    </div>
                  </div>
                  <div class="cart-item-price">
                    <div class="cart-item-price__head">Цена:</div>
                    <div class="cart-item-price__content">
                      <span>13 490</span> ₽
                    </div>
                  </div>
                </div>
                <div class="cart-item__delete">Удалить</div>
              </div>
            </div>
            <div class="cart-default" v-else>
              <div class="cart-default-image">
                <img
                  src="../assets/image/SVG/cart-default.svg"
                  alt=""
                  class="cart-default-image__img"
                />
              </div>
              <p class="cart-default__title">Ваша корзина пуста</p>
              <a href="/" class="cart-default__link btn">Перейти к покупкам</a>
            </div>
          </div>
          <div class="cart-result">
            <div class="cart-result__box">
              <div class="cart-result-head">
                <p class="cart-result-head__title">Итого:</p>
                <p class="cart-result-head__body"><span>13 490</span> ₽</p>
              </div>
              <form class="cart-result-promocode cart-promocode"></form>
              <div class="btn cart-result__btn">Перейти к оформлению</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: "Cart",
  data() {
    return {
      cart: {
        items: [1],
        quantity: 1,
      },
    };
  },
  computed: {
    cartLength() {
      return this.cart.items.length > 0 ? false : true;
    },
  },
  methods: {
    increment() {

    },
    decrement() {
      
    }
  }
};
</script>
<style lang="scss" scoped>
@import "../assets/css/constants.scss";
@import "../assets/css/cart.scss";
</style>