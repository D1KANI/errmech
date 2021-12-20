<template>
  <header class="header">
    <div class="container">
      <div class="header__flex">
        <div @click="menuToggle()" class="header-burger">
          <span></span>
          <span></span>
          <span></span>
        </div>
        <logo class="header__logo"></logo>
        <nav class="nav">
          <a href="#" class="nav__link">Клавиатуры</a>
          <a href="#" class="nav__link">Аксессуары</a>
          <a href="/categories.html" class="nav__link">Категории</a>
        </nav>
        <div class="header__buttons">
          <a href="#" class="profile-btn">
            <img
              src="../assets/image/SVG/profile.svg"
              alt=""
              class="profile-btn__image"
            />
            <p>Профиль</p>
          </a>
          <router-link :to="{ name: 'Cart' }" class="cart-btn">
            <img
              src="../assets/image/SVG/cart.svg"
              alt=""
              class="cart-btn__image"
            />
            <p>Корзина</p>
          </router-link>
        </div>
      </div>
    </div>
    <div class="menu" id="menu">
      <nav class="menu-nav">
        <a href="#" class="menu-nav__link">Клавиатуры</a>
        <a href="#" class="menu-nav__link">Переключатели</a>
        <a href="#" class="menu-nav__link">Кейкапы</a>
        <a href="#" class="menu-nav__link">Аксессуары</a>
        <a href="#" class="menu-nav__link">Новости</a>
        <a href="/categories.html" class="menu-nav__link">Категории</a>
      </nav>
      <a href="#" class="menu-profile">
        <img
          src="../assets/image/SVG/profile.svg"
          alt=""
          class="menu-profile__image"
        />
        <p>Профиль</p>
      </a>
    </div>
  </header>
</template>

<script>
import Logo from "@/components/Logo";

export default {
  name: "HeaderApp",
  data() {
    return {

    }
  },
  components: {
    Logo,
  },
  methods: {
    menuToggle() {
      this.slideToggle(document.getElementById("menu"), 400);
    },
    slideUp(target, duration = 500) {
      target.style.transitionProperty = "height, margin, padding";
      target.style.transitionDuration = duration + "ms";
      target.style.boxSizing = "border-box";
      target.style.height = target.offsetHeight + "px";
      target.offsetHeight;
      target.style.overflow = "hidden";
      target.style.height = 0;
      target.style.paddingTop = 0;
      target.style.paddingBottom = 0;
      target.style.marginTop = 0;
      target.style.marginBottom = 0;
      window.setTimeout(() => {
        target.style.display = "none";
        target.style.removeProperty("height");
        target.style.removeProperty("padding-top");
        target.style.removeProperty("padding-bottom");
        target.style.removeProperty("margin-top");
        target.style.removeProperty("margin-bottom");
        target.style.removeProperty("overflow");
        target.style.removeProperty("transition-duration");
        target.style.removeProperty("transition-property");
      }, duration);
    },
    slideDown(target, duration = 500) {
      target.style.removeProperty("display");
      let display = window.getComputedStyle(target).display;
      if (display === "none") display = "block";
      target.style.display = display;
      let height = target.offsetHeight;
      target.style.overflow = "hidden";
      target.style.height = 0;
      target.style.paddingTop = 0;
      target.style.paddingBottom = 0;
      target.style.marginTop = 0;
      target.style.marginBottom = 0;
      target.offsetHeight;
      target.style.boxSizing = "border-box";
      target.style.transitionProperty = "height, margin, padding";
      target.style.transitionDuration = duration + "ms";
      target.style.height = height + "px";
      target.style.removeProperty("padding-top");
      target.style.removeProperty("padding-bottom");
      target.style.removeProperty("margin-top");
      target.style.removeProperty("margin-bottom");
      window.setTimeout(() => {
        target.style.removeProperty("height");
        target.style.removeProperty("overflow");
        target.style.removeProperty("transition-duration");
        target.style.removeProperty("transition-property");
      }, duration);
    },
    slideToggle(target, duration = 500) {
      if (window.getComputedStyle(target).display === "none") {
        return this.slideDown(target, duration);
      } else {
        return this.slideUp(target, duration);
      }
    },
  },
};
</script>

<style scoped lang="scss">
@import "../assets/css/constants.scss";
@import "../assets/css/layout.scss";
</style>
