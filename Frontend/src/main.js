import { createApp } from 'vue'
import App from './App.vue'

// App instance
const app = createApp(App);

// vue-router
import router from './configs/router/router'

// Event emitter
// import mitt from 'mitt';
// const emitter = mitt();
// app.config.globalProperties.emitter = emitter;

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

app.use(router).use(vuetify);

app.mount('#app')
