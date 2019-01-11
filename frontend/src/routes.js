import Landing from './components/Landing.vue'
import Home from './components/Home.vue'
import AppContainer from './components/AppContainer.vue'
import SettingsHome from './components/settings/SettingsHome.vue'

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
    path: '/app',
    component: AppContainer,
    children: [
        {
          path: 'home',
          component: Home,
        },
        {
          path: 'settings',
          component: SettingsHome
        }
      ]
  },
];
