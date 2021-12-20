import Vue from 'vue'
import Vuex, { Store } from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token: '',
    isLoading: false,
  },
  getters: {
    cart(state) {
      return state.cart;
    },
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
    token(state) {
      return state.token;
    },
    isLoading(state) {
      return state.isLoading;
    },
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
      } else {
          state.token = ''
          state.isAuthenticated = false
      } 
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id);

      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity);
      } else {
        state.cart.items.push(item);
      }

      localStorage.setItem('cart', JSON.stringify(state.cart));
    },
    setIsLoading(state, status) {
      state.isLoading = status;
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = '';
      state.isAuthenticated = false;
    },
  },
  actions: {
  },
  modules: {
  }
})
