import { createRouter, createWebHistory } from 'vue-router'
import HomeView from './views/HomeView.vue'
import LoginSignUp from './views/LoginSignUp.vue'
import Profile from './pages/Profile.vue'
import Dashboard from './pages/Dashboard.vue'
import Artist from './pages/Artist.vue'
import Music from './pages/Music.vue'
import Album from './pages/Album.vue'
import AlbumDetail from './pages/AlbumDetail.vue'
import ArtistDetail from './pages/ArtistDetail.vue'
import MusicDetail from './pages/MusicDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
     {
      path: '/login',
      name: 'LoginSignUp',
      component: LoginSignUp
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
    },{
      path: '/profile',
      name: 'profile',
      component: Profile
    },{
      path: '/artist',
      name: 'artist',
      component: Artist
    },{
      path: '/music',
      name: 'music',
      component: Music
    },{
      path: '/album',
      name: 'album',
      component: Album
    },{
      path: '/album/:id',
      name: 'albumDetail',
      component: AlbumDetail
    },{
      path: '/music/:id',
      name: 'musicDetail',
      component:  MusicDetail
    },{
      path: '/artist/:id',
      name: 'artistDetail',
      component: ArtistDetail
    },
  ]
})

export default router
