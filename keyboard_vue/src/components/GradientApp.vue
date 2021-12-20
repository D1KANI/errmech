<template>
  <section class="gradient" id="gradient">
    <div class="container">
      <div class="gradient__flex">
        <div class="gradient-head">
          <p>Клавиатуры с RGB подсветкой</p>
          <a href="#" class="gradient-head__link">Подробнее</a>
        </div>
        <div class="gradient__btn" :class="btnClass" @click="stopGradient()">
          <span> Остановить </span>
          <span class="pause"> Продолжить </span>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: "GradientApp",
  data() {
    return {
      gradientSpeed: 0.005,
      colors: [
        [62, 35, 255],
        [60, 255, 60],
        [255, 35, 98],
        [45, 175, 230],
        [255, 0, 255],
        [255, 128, 0],
      ],
      step: 0,
      colorIndices: [0, 1, 2, 3],
      btnClass: '',
      onPLay: true,
      gradient: null
    };
  },
  methods: {
    async changeGradientColor() {
      this.gradient = setInterval(this.updateGradient, 10);
    },
    updateGradient() {
      var c0_0 = this.colors[this.colorIndices[0]];
      var c0_1 = this.colors[this.colorIndices[1]];
      var c1_0 = this.colors[this.colorIndices[2]];
      var c1_1 = this.colors[this.colorIndices[3]];
      var istep = 1 - this.step;
      var r1 = Math.round(istep * c0_0[0] + this.step * c0_1[0]);
      var g1 = Math.round(istep * c0_0[1] + this.step * c0_1[1]);
      var b1 = Math.round(istep * c0_0[2] + this.step * c0_1[2]);
      var color1 = "rgb(" + r1 + "," + g1 + "," + b1 + ")";

      var r2 = Math.round(istep * c1_0[0] + this.step * c1_1[0]);
      var g2 = Math.round(istep * c1_0[1] + this.step * c1_1[1]);
      var b2 = Math.round(istep * c1_0[2] + this.step * c1_1[2]);
      var color2 = "rgb(" + r2 + "," + g2 + "," + b2 + ")";

      document.getElementById("gradient").style.background =
        "-webkit-gradient(linear, left top, right top, from(" +
        color1 +
        "), to(" +
        color2 +
        "))";
      document.getElementById("gradient").style.background =
        "-moz-linear-gradient(left, " + color1 + " 0%, " + color2 + " 100%)";

      this.step += this.gradientSpeed;
      if (this.step >= 1) {
        this.step %= 1;
        this.colorIndices[0] = this.colorIndices[1];
        this.colorIndices[2] = this.colorIndices[3];
        this.colorIndices[1] =
          (this.colorIndices[1] +
            Math.floor(1 + Math.random() * (this.colors.length - 1))) %
          this.colors.length;
        this.colorIndices[3] =
          (this.colorIndices[3] +
            Math.floor(1 + Math.random() * (this.colors.length - 1))) %
          this.colors.length;
      }
    },
    stopGradient() {
      if (this.onPLay) {
        this.btnClass = 'active';
        this.gradientSpeed = 0;
        this.onPLay = false;
      } else {
        this.btnClass = '';
        this.gradientSpeed = 0.005;
        this.onPLay = true;
      }
    }
  },
  mounted() {
    this.changeGradientColor();
  },
  destroyed() {
    clearInterval(this.gradient)
  }
};
</script>
<style lang="scss" scoped>
.gradient {
  padding: 100px 0;
  &__flex {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  &-head {
    display: flex;
    align-items: center;
    p {
      color: #fff;
      font-weight: 600;
      font-size: 40px;
      line-height: 48px;
      margin-right: 50px;
    }
    &__link {
      display: inline-block;
      color: #fff;
      text-transform: uppercase;
      font-weight: bold;
      font-size: 16px;
      line-height: 19px;
      padding: 15px 40px;
      border: 1px solid #fff;
      border-radius: 3px;
      transition: all 175ms ease-out;
      &:hover {
        color: #fff;
        border-color: transparent;
        background-color: rgba(255, 255, 255, 0.1);
      }
    }
  }
  &__btn {
    text-transform: uppercase;
    color: #fff;
    padding: 15px 40px;
    user-select: none;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    width: 210px;
    height: 50px;
    border: 1px solid #fff;
    border-radius: 3px;
    cursor: pointer;
    opacity: 0.5;
    transition: opacity 175ms ease-out;
    position: relative;
    overflow: hidden;
    &:before {
      content: "";
      display: block;
      width: 14px;
      height: 14px;
      background-color: #fff;
      border-radius: 2px;
      margin-right: 10px;
      position: absolute;
      top: 50%;
      left: 30px;
      transform: translateY(-50%);
      transition: all 175ms ease-out;
    }
    &:hover {
      opacity: 1;
    }
    span {
      font-weight: bold;
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      transition: all 175ms ease-out;
      &.pause {
        top: 150%;
      }
    }
    &.active {
      span {
        top: -150%;
        &.pause {
          top: 50%;
        }
      }
      &:before {
        height: 0;
        width: 0;
        background-color: transparent;
        border: 8px solid rgba(0, 0, 0, 0);
        border-left: 14px solid #fff;
        margin-right: 2px;
      }
    }
  }
}

@media screen and (max-width: 1170px) {
  .gradient {
    &-head {
      display: block;
      p {
        margin: 0;
      }
      &__link {
        display: block;
        width: max-content;
        margin-top: 20px;
      }
    }
    &__btn {
      &:hover {
        opacity: 0.5;
      }
    }
  }
}

@media screen and (max-width: 890px) {
  .gradient {
    padding: 70px 0 50px;
    &__flex {
      display: block;
    }
    &-head {
      p {
        text-align: center;
      }
      &__link {
        margin: 20px auto 30px;
      }
    }
    &__btn {
      margin: 0 auto;
    }
  }
}

@media screen and (max-width: 650px) {
  .gradient {
    &-head {
      p {
        font-size: 30px;
        line-height: 36px;
      }
    }
  }
}

@media screen and (max-width: 460px) {
  .gradient {
    &-head {
      p {
        font-size: 28px;
        line-height: 33px;
      }
    }
  }
}
</style>