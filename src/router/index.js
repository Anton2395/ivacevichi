import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/LoginView.vue'

const routes = [
  {
    path: '/',
    redirect: () => {
      return 'login'
    }
  },
  {
    path: '/settings',
    name: 'settings',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/ConfigView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
    
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
