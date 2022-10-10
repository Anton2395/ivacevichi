import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueCookies from 'vue-cookies'


// import store from '@/store/index'

// axios.defaults.withCredentials = true;
// axios.defaults.baseURL = 'http://127.0.0.1:8000/'
// let cookie = document.cookie
// cookie.split(' ').forEach(item => {
//     if (item.includes('access_token')) {
//         axios.defaults.headers.common['Authorization'] = 'Bearer ' + item.split('=')[1].slice(0, -1)
//     }
// })

createApp(App).use(ElementPlus).use(store).use(router).use(VueAxios, axios).use(VueCookies).mount('#app')



