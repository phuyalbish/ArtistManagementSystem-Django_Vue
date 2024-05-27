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
      component: HomeView,

      meta: {auth:false}
    },
     {
      path: '/login',
      name: 'LoginSignUp',
      component: LoginSignUp,

      meta: {auth:false}
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      meta: {auth:true}
    },{
      path: '/profile',
      name: 'profile',
      component: Profile,
      meta: {auth:true}
    },{
      path: '/artist',
      name: 'artist',
      component: Artist,
      meta: {auth:true}
    },{
      path: '/music',
      name: 'music',
      component: Music,
      meta: {auth:true}
    },{
      path: '/album',
      name: 'album',
      component: Album,
      meta: {auth:true}
    },{
      path: '/album/:id',
      name: 'albumDetail',
      component: AlbumDetail,
      meta: {auth:true}
    },{
      path: '/music/:id',
      name: 'musicDetail',
      component:  MusicDetail,
      meta: {auth:true}
    },{
      path: '/artist/:id',
      name: 'artistDetail',
      component: ArtistDetail,
      meta: {auth:true}
    },
  ]
});
router.beforeEach((to, from, next) =>{
  if ( to.meta.auth && !localStorage.getItem('access_token')){
    next('/login')
  }
  else if(!to.meta.auth && localStorage.getItem('access_token')){
    next('/dashboard')
  }else{
    next()
  }
})

export default router
