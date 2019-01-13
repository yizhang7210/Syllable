import Landing from './components/Landing.vue'
import Home from './components/Home.vue'
import SettingsHome from './components/settings/SettingsHome.vue'
import SettingsOrganization from './components/settings/SettingsOrganization.vue'

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
  {
    path: '/settings',
    component: SettingsHome,
    children: [
      {
        path: '',
        redirect: 'organization'
      },
      {
        path: 'organization',
        component: SettingsOrganization
      }
    ]
  }
];
