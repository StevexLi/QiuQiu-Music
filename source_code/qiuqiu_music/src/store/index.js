import { createStore } from 'vuex'
import NowPlayMusicList from '../components/nowPlayingMusicList'
import User from "@/components/User";
import createPersistedState from 'vuex-persistedstate';
import imageToDataUrl from '@/components/utils'
import { ref } from "vue";


export default createStore({
  state: {
    globalLogin: false,
    globalUserID: 0,
    globalUserToken: '',
    nowPlayMusic : null,
    nowPlayingMusicSet : new NowPlayMusicList(),
    currentVolume:0,
    loginUser : ref(null),
    globalIsLoaded:true,
    currentSongList: ref(null),
    searchKeywords: null,
    globalLyric: '丘丘音乐，听我想听',
    globalLyricSets:{
      ti: "", //歌曲名
      ar: "", //演唱者
      al: "", //专辑名
      by: "", //歌词制作人
      offset: 0, //时间补偿值，单位毫秒，用于调整歌词整体位置
      kana:"",
      ms: [] //歌词数组{t:时间,c:歌词}
    },
    globalLyric2: '丘丘音乐，听我想听',
    globalLyricSets2:{
      ti: "", //歌曲名
      ar: "", //演唱者
      al: "", //专辑名
      by: "", //歌词制作人
      offset: 0, //时间补偿值，单位毫秒，用于调整歌词整体位置
      kana:"",
      ms: [] //歌词数组{t:时间,c:歌词}
    }
  },
  getters: {
  },
  mutations: {
    CHANGENOWPLAYINGMUSIC(state,music){
      state.nowPlayMusic = music;
    },
    CHANGENOWPLAYINGLYRIC(state, lyric) {
      state.globalLyric = lyric;
    },
    CHANGENOWPLAYINGLYRICSETS(state, lyricsets) {
      state.globalLyricSets = lyricsets;
    },
    CHANGENOWPLAYINGLYRIC2(state, lyric) {
      state.globalLyric2 = lyric;
    },
    CHANGENOWPLAYINGLYRICSETS2(state, lyricsets) {
      state.globalLyricSets2 = lyricsets;
    },
    updateLoginUser(state, value) {
      state.loginUser = value;
    },
    updateImageDataUrl(state,dataUrl,i){
      state.testUserList[i].icon = dataUrl;
    },
    addAttentionUser(state,user){
      state.loginUser.attentionUser.splice(state.loginUser.attentionUser.length, 0, user);
    },
    updateIsLoaded(state,value){
      state.globalIsLoaded = value;
    },
    updateuid(state,uid){
      state.globalUserID=uid;
      state.globalLogin=true;
    },
    updatetoken(state,token){
      state.globalUserToken=token;
    },
    updateRecentPlay(state,playMax){
      state.loginUser.recentPlayMax=playMax;
    },
    GLOBALLOGOUT(state,user){
      state.globalLogin = false;
      state.globalUserID = 0;
      state.globalUserToken = '';
      state.loginUser = ref(null);
      state.globalIsLoaded = true;
      state.currentSongList = ref(null);
      state.searchKeywords = null;
    },
  },
  actions: {
    ChangeNowPlayMusic(context,music){
      context.commit('CHANGENOWPLAYINGMUSIC',music);
    }
  },
  modules: {
  },
  plugins: [
    createPersistedState({
      paths: ['loginUser','visitUser','globalLogin','globalUserID','globalUserToken'],

    }),
  ],
})
