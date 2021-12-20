<template>
  <div class="slider">
    <VueSlickCarousel v-bind="settings">
      <div class="slider-item slide1">
        <p class="slider-item__title">SA Dualshot Keycap Set</p>
        <p class="slider-item__subtitle">Лимитированое издание даблшот кейкапов SA профиля</p>
        <a href="#" class="slider-item__btn">Подробнее</a>
      </div>
      <div class="slider-item slide2">
        <p class="slider-item__title">SA Dualshot Keycap Set</p>
        <p class="slider-item__subtitle">Лимитированое издание даблшот кейкапов SA профиля</p>
        <a href="#" class="slider-item__btn">Подробнее</a>
      </div>
      <div class="slider-item slide3">
        <p class="slider-item__title">SA Dualshot Keycap Set</p>
        <p class="slider-item__subtitle">Лимитированое издание даблшот кейкапов SA профиля</p>
        <a href="#" class="slider-item__btn">Подробнее</a>
      </div>
    </VueSlickCarousel>
  </div>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
export default {
  name: "SliderApp",
  components: {
    VueSlickCarousel,
  },
  data() {
    return {
      settings: {
        arrows: true,
        dots: true,
        draggable: false, 
        fade: true,
        autoplay: true,
        autoplaySpeed: 4000,
        infinity: true,
        responsive: [
          {
            breakpoint: 1140,
            settings: {
              arrows: false,
            }
          },
        ]
      },
    };
  },
};
</script>

<style lang="scss">
.slider {
  position: relative;
  &-item {
    padding: 248px 150px 248px 250px;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center center;
    outline: none;
    &__title {
      font-weight: 500;
      font-size: 60px;
      line-height: 71px;
      color: #fff;
    }
    &__subtitle {
      margin: 30px 0;
      font-weight: normal;
      font-size: 20px;
      line-height: 24px;
      color: #fff;
    }
    &__btn {
      display: block;
      width: max-content;
      padding: 15px 40px;
      text-transform: uppercase;
      font-weight: 600;
      font-size: 16px;
      line-height: 19px;
      color: #fff;
      border: 1px solid #ffffff;
      border-radius: 3px;
    }
  }
  .slick {
    &-dots {
      position: absolute;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%);
      display: flex !important;
      list-style-type: none;
      li {
        margin: 0 6px;
        button {
          display: block;
          font-size: 0;
          line-height: 0;
          width: 12px;
          height: 12px;
          border-radius: 50%;
          background-color: #adadad;
          border: none;
          transition: background-color 250ms ease-out;
          cursor: pointer;
        }
        &.slick-active {
          button {
            background-color: #fff;
          }
        }
      }
    }
    &-arrow {
      position: absolute;
      z-index: 1;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0;
      line-height: 0;
      cursor: pointer;
      background-color: transparent;
      border: none;
      padding: 10px 0;
      &:before {
        content: "";
        display: block;
        width: 50px;
        height: 18px;
        background: url(../assets/image/SVG/arrow.svg) no-repeat center center /
          contain;
      }
    }
    &-prev {
      left: 100px;
    }
    &-next {
      right: 100px;
      &:before {
        transform: rotate(180deg);
      }
    }
  }
}

@media screen and (max-width: 1820px) {
  .slider {
    &-item {
      padding-left: 200px;
    }
    .slick {
      &-prev {
        left: 50px;
      }
      &-next {
        right: 50px;
      }
    }
  }
}

@media screen and (max-width: 1140px) {
  .slider {
    &-item {
      padding: 150px 50px;
    }
  }
}

@media screen and (max-width: 800px) {
  .slider {
    &-item {
      padding: 100px 30px 130px;
      &__title {
        text-align: center;
        font-weight: 500;
        font-size: 50px;
        line-height: 59px;
      }
      &__subtitle {
        text-align: center;
        font-size: 20px;
        line-height: 24px;
      }
      &__btn {
        margin: 0 auto;
      }
    }
  }
}

@media screen and (max-width: 480px) {
  .slider {
    &-item {
      padding: 70px 15px 130px;
      &__title {
        font-size: 40px;
        line-height: 47px;
      }
      &__subtitle {
        font-size: 18px;
        line-height: 24px;
      }
    }
    .slick {
      &-dots {
        bottom: 20px;
      }
    }
  }
}

.slide1 {
  background-image: url(../assets/image/banner/SADualshotSet.png);
}

.slide2 {
  background-image: url(../assets/image/banner/Keyboard.png);
}

.slide3 {
  background-image: url(../assets/image/banner/RedDragon.png);
}
</style>