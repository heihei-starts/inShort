import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../pages/Home.vue'
import About from '../pages/About.vue'
import Login from '../pages/Login.vue'
import Register from '../pages/Register.vue'
import Explain from '../pages/Explain.vue'
import User from '../pages/User.vue'
import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About,
    beforeEnter(to, from, next) {
      if (store.getters.idToken) { //idTokenがあれば、そのまま"/about"に
        next();
      } else { //なければ"/login"に飛ばす
        next("/login");
      }
    },
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    beforeEnter(to, from, next) {
      if (Vue.$cookies.isKey('token')) {//すでにidTokenがあれば、"/"に飛ばす
        next("/");
      } else { //なければそのまま"/login"に
        next();
      }
    },
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    beforeEnter(to, from, next) {
      if (Vue.$cookies.isKey('token')) {//すでにidTokenがあれば、"/"に飛ばす
        next("/");
      } else {//なければそのまま"/register"に
        next();
      }
    },
  },
  {
    path: '/explain',
    name: 'Explain',
    component: Explain,
  },
  {
    path: '/user',
    name: 'User',
    component: User,
    beforeEnter(to, from ,next) {
      if (Vue.$cookies.isKey('token')) {
        next()
      } else {
        next('login')
      }
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
