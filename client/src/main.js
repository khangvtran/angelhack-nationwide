// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import VueLocalStorage from 'vue-localstorage'
import * as VueGoogleMaps from "vue2-google-maps";
import key from './../config/config.js'

Vue.config.productionTip = false
Vue.use(Vuetify)
Vue.use(VueLocalStorage)

Vue.use(VueGoogleMaps, {
  load: {
    key: key,
    libraries: "places" // necessary for places input
  }
});


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
