import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ProductDetail from '../views/ProductDetail.vue'
import Cart from '../views/Cart.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: 'Главная страница'
    }
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart,
    meta: {
      title: 'Корзина'
    }
  },
  {
    path: '/products',
    name: 'ProductDetail',
    component: ProductDetail,
    meta: {
      title: 'Товар'
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
    meta: {
      title: 'О нас'
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

const DEFAULT_TITLE = 'ERR.MECH';
router.afterEach((to, from) => {
    Vue.nextTick(() => {
        document.title = DEFAULT_TITLE + ' | ' + to.meta.title || DEFAULT_TITLE;
    });
});