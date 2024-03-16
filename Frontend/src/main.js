import { createApp } from 'vue'
import App from './App.vue'
// 路由
import router from './configs/router/router'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

// 项目实例
const app = createApp(App);

app.use(router).use(vuetify);

app.mount('#app')
