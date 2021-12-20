<template>
  <section class="index-news">
    <div class="container">
      <div class="index-news__wrapper">
        <div class="index-news__head">
          <h2>Новые статьи</h2>
          <a href="/articles.html" class="index-news__link">Все статьи →</a>
        </div>
        <div class="index-news__flex">
          <new-box
          v-for="item in news.items"
          :key="item"
          ></new-box>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import newBox from '@/components/NewBox'
export default {
  name: "",
  data() {
    return {
      news: {
        items: [1, 2, 3, 4]
      }
    };
  },
  components: {
    newBox
  },
};
</script>
<style lang="scss" scoped>
@import '../assets/css/constants';
.index-news {
  margin: 50px 0 100px;
  &__wrapper {
    display: flex;
    justify-content: space-between;
  }
  &__flex {
    flex-grow: 1;
    display: flex;
    justify-content: space-between;
  }
  &__head {
    min-width: calc((100% - 220px) / 5);
    margin-right: 55px;
  }
  &__link {
    position: relative;
    display: block;
    width: max-content;
    color: $blue;
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    margin-top: 10px;
    &:before {
      content: "";
      display: block;
      background-color: $blue;
      height: 1px;
      width: 0;
      position: absolute;
      bottom: 0;
      left: 0;
      transition: width 175ms ease-out;
    }
    &:hover::before {
      width: 100%;
    }
  }
}

@media screen and (max-width: 1440px) {
  .index-news {
    &__head {
      min-width: calc((100% - 75px) / 4);
      margin-right: 25px;
    }
  }
}

@media screen and (max-width: 1220px) {
  .index-news {
    &__wrapper {
      display: block;
    }
    &__head {
      margin-bottom: 30px;
      min-width: auto;
    }
  }
} 

@media screen and (max-width: 620px) {
  .index-news {
    h2 {
      text-align: center;
    }
    &__link {
      margin: 10px auto 0;
    }
  }
}

@media screen and (max-width: 570px) {
  .index-news {
    &__flex {
      display: block;
    }
  }
}

</style>