<template>
  <section class="item">
    <div class="container">
      <div class="item__flex">
        <div class="item__left">
          <div class="images">
            <div class="images-big">
              <div class="images-big__image-wrapper">
                <img
                  :src="mainImage"
                  alt=""
                  class="images-big__image"
                />
              </div>
            </div>
            <div class="images-small">
              <div v-for="item in images.items" 
                   :key="item"
                   @click="swapImage($event)"
                   class="images-small__image-wrapper">
                <img
                  :src="`${item}`"
                  alt=""
                  class="images-small__image"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="item__right">
          <div class="item__info">
            <div class="item__category">Клавиатуры</div>
            <div class="item__name">
              <span>Varmilo</span> <span>VA87M Vintage Days</span>
            </div>
            <div class="item__desc-small">
              Давно мы не слышали писк модема и пароль от аськи совсем забыт. На
              мониторах больше нет защитных экранов и шарик от мышки больше не
              нужно чистить. Но, порой, так хочется хоть на минутку в 1998-й,
              заглянуть кто там в чате и оставить компьютер на ночь качать mp3
              (главное, чтоб никто трубку не поднял). Увы, прошлое не вернуть и
              многие вещи безнадёжно устарели. Но не Varmilo Vintage Days.
              Классическая серо-белая расцветка клавиш, проверенные
              переключатели и лучшие материалы, ностальгия ещё никогда не была
              такой качественной. В комплекте есть 9 ярких функциональных клавиш
              и 3 клавиши для Lock-ов с прорезью для индикации работы.
            </div>
            <div class="item-bottom">
              <div class="item__price"><span>13 490</span> ₽</div>
              <a href="#" class="item__btn btn">Добавить в корзину</a>
            </div>
          </div>
        </div>
      </div>
      <div class="item__flex">
        <div class="item__left">
          <div class="item-desc">
            <h3>Описание</h3>
            <p>
              Varmilo – производитель, которого по многим параметрам можно
              поставить на один уровень с Леопольд: они так же серьезно
              относятся к качеству своей продукции, так же не тратят уйму
              средств на маркетинг и точно так же используют премиальные
              материалы в своей продукции, но что же их отличает? А отличает их
              страсть к необычным цветовым решениям. Леопольд стараются
              выпускать свои продукты в сдержанных и классических тонах, Вармило
              же не боится экспериментировать и её продукцию можно найти как в
              классическом исполнении, так и в весьма необычных цветовых
              решениях.
            </p>
            <p>
              В данной модели основным цветом является холодный белый, почти все
              клавиши модификаторы представлены в сером цвете, тогда как клавиши
              shift/ctrl/windows/alt/fn имеют
              желтый/розово-красный/фиолетовый/голубой/оранжевый цвета
              соответственно (в комплекте есть дополнительные вышеперечисленные
              клавиши в сером цвете, а также Caps Lock и Scroll Lock с прорезями
              под светодиоды). Mini-USB порт спрятан в центре под корпусом, а на
              самой клавиатуре имеются центральная и две боковые канавки под
              кабель.
            </p>
            <h3>Особенности</h3>
            <div class="item-desc__item">
              <p class="before-dot">Мультимедиа и дополнительные FN функции</p>
              <p>
                Клавиатура поддерживает сочетания клавиш для регулировки
                громкости и управления музыкой. Также имеется возможность
                отключить кнопку windows и поменять клавиши Fn и Win/Ctrl и Caps
                Lock местами.
              </p>
            </div>
            <div class="item-desc__item">
              <p class="before-dot">Клавишные колпачки толщиной 1.4 мм</p>
              <p>
                Колпачки изготовлены из высокопрочного пластика PBT с
                применением dye-sublimation технологии, с выгравированными
                символами на боках. Использование dye-sub позволяет символам
                никогда не стираться и никак не чувствоваться при печати, а
                качественный PBT пластик гарантирует надежность и долговечность.
                Клавиши имеют слегка текстурированный верх и приятны на ощупь.
              </p>
            </div>
            <div class="item-desc__item">
              <p class="before-dot">Стабилизаторы, смазанные на заводе</p>
              <p>
                Сочетание стабилизаторов и смазки позволяет добиться максимально
                равномерного и плавного хода клавиш enter/space/shift/backspace,
                а сами колпачки легко снять с клавиатуры.
              </p>
            </div>
            <div class="item-desc__item">
              <p class="before-dot">Белая подсветка</p>
              <p>
                Имеется 3 разных режима (выключена, статичное свечение, эффект
                затухания) и 4 уровня яркости. Режимы меняются через FN +
                стрелка вправо, FN + стрелка вверх/вниз меняет яркость в режиме
                статичного свечения и скорость в режиме затухания.
              </p>
            </div>
            <h3>Комплектация</h3>
            <p class="before-dot before-dot_small">Клавиатура;</p>
            <p class="before-dot before-dot_small">Коробка;</p>
            <p class="before-dot before-dot_small">
              Крышка для защиты от пыли;
            </p>
            <p class="before-dot before-dot_small">
              Varmilo wire keycap puller – позволит легко снять колпачки с
              клавиатуры;
            </p>
            <p class="before-dot before-dot_small">
              Mini-USB кабель с велкро застежкой;
            </p>
            <p class="before-dot before-dot_small">
              Дополнительные серые клавиши-модификаторы: Caps Lock и Scroll Lock
              с прорезями под светодиоды.
            </p>
            <p class="before-dot before-dot_small">
              Инструкция на английском языке.
            </p>
          </div>
        </div>
        <div class="item__right">
          <div class="item-feature__box">
            <div class="item-feature__title">Основные характеристики</div>
            <div class="item-feature__flex">
              <div class="item-feature__item">Производитель: Varmilo</div>
              <div class="item-feature__item">
                Тип переключателей: Cherry MX
              </div>
              <div class="item-feature__item">
                Модель: VA87M Vintage Days CMYK
              </div>
              <div class="item-feature__item">Беспроводная: Нет</div>
              <div class="item-feature__item">Формат: TKL</div>
              <div class="item-feature__item">Подсветка: White LED</div>
              <div class="item-feature__item">Количество клавиш: 87</div>
              <div class="item-feature__item">Разъём: Mini USB</div>
              <div class="item-feature__item">Материал корпуса: Пластик</div>
              <div class="item-feature__item">Размер: 35.6x13.4x3.3 см</div>
              <div class="item-feature__item">Материал клавиш: PBT-пластик</div>
              <div class="item-feature__item">Вес: 0.85 кг</div>
              <div class="item-feature__item">Раскладка: ANSI</div>
              <div class="item-feature__item">Гарантия: 1 год</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import imageFirst from '../assets/image/item/item.png';
import imageSecond from '../assets/image/item/item2.png';
export default {
  name: "ProductDetail",
  data() {
    return {
      images: {
        items: [
          imageFirst,
          imageSecond,
        ]
      },
      mainImage: imageFirst,
    };
  },
  methods: {
    swapImage(event) {
      this.mainImage = event.target.querySelector('img').src
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../assets/css/constants.scss";
@import "../assets/css/item.scss";
</style>
