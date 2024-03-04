import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'musicClub',
    component: () => import('../views/MusicClub.vue')
  },
  {
    path: '/login',
    name: 'login',
    component:() => import('../views/NewLogin.vue')
  },
  {
    path: '/upLoadSong',
    name: 'upLoadSong',
    component: () => import('../views/UpLoadSong.vue')
  },
  {
    path: '/createSongList',
    name: 'createSongList',
    component: () => import('../views/CreateSongList.vue')
  },
  {
    path: '/user/noLogin',
    name: 'userNoLogin',
    component: () => import('../views/UserNoLogin.vue')
  },
  {
    path: '/user/info/:uid',
    name: 'userLogined',
    component: () => import('../views/UserLogined.vue')
  },
  {
    path: '/user/songList/:songListId',
    name: 'songList',
    component: () => import('../views/songList.vue')
  },
  {
    path: '/mySongList/:uid',
    name: 'mySongList',
    component: () => import('../views/MySongList.vue')
  },
  {
    path: '/music/:musicId',
    name: 'musicItem',
    component: () => import('../views/musicItem.vue')
  },
  {
    path: '/search/:keywords',
    name: 'search',
    component: () => import('../views/Search.vue')
  },
  {
    path: '/history/:uid',
    name: 'history',
    component: () => import('../views/History.vue')
  },
  {
    path: '/manage',
    name: 'manage',
    component: () => import('../views/Manage.vue')
  },
  {
    path: '/partition/:tag',
    name: 'partition',
    component: () => import('../views/Partition.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
