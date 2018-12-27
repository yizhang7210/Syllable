import Landing from './components/Landing.vue'
import Home from './components/Home.vue'

export default [
  {
    path: '/',
    redirect: '/landing'
  },
  {
    path: '/landing',
    component: Landing,
  },
  {
    path: '/home',
    component: Home,
  },
];
