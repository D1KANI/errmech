import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import font from '../src/assets/fonts/Gilroy/stylesheet.css'
import Toasted from 'vue-toasted';
 
Vue.use(Toasted, {
  iconPack : 'material' // set your iconPack, defaults to material. material|fontawesome|custom-class
})

axios.defaults.baseURL = "http://127.0.0.1:8000"

Vue.config.productionTip = false

new Vue({
  router,
  store,
  axios,
  font,
  render: h => h(App)
}).$mount('#app')
