import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './components/mis_rutas/rutas'
import store from './store/index.js';

createApp(App) 
.use(router)
.use(store)
.mount('#app')
