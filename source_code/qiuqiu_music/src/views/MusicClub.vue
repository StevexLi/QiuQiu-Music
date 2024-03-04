<template>
  <div v-if="!isLoaded" style="position: fixed; top: 0; min-width: 1200px;width: 100%;height: 100%;">
    <div v-loading="!isLoaded" element-loading-text="正在加载..." style="height: 100%;width: 100%;"></div>
  </div>
  <div class="musicClub" v-if="isLoaded">
    <h1 style="font-weight: 500;letter-spacing:15px; margin-top: 50px;">
      歌单推荐
    </h1>
    <div>
      <span id="MusicSet1" @mouseover="mouseOverClass('MusicSet1')" @mouseout="mouseOutClass('MusicSet1')"
        @click="mouseClickClass('MusicSet1')" class="MusicClass">
        为你推荐
      </span>
      <span id="MusicSet2" @mouseover="mouseOverClass('MusicSet2')" @mouseout="mouseOutClass('MusicSet2')"
        @click="mouseClickClass('MusicSet2')" class="MusicClass">
        经典
      </span>
      <span id="MusicSet3" @mouseover="mouseOverClass('MusicSet3')" @mouseout="mouseOutClass('MusicSet3')"
        @click="mouseClickClass('MusicSet3')" class="MusicClass">
        轻音乐
      </span>
      <span id="MusicSet4" @mouseover="mouseOverClass('MusicSet4')" @mouseout="mouseOutClass('MusicSet4')"
        @click="mouseClickClass('MusicSet4')" class="MusicClass">
        ACG
      </span>
      <span id="MusicSet5" @mouseover="mouseOverClass('MusicSet5')" @mouseout="mouseOutClass('MusicSet5')"
        @click="mouseClickClass('MusicSet5')" class="MusicClass">
        治愈
      </span>
      <span id="MusicSet6" @mouseover="mouseOverClass('MusicSet6')" @mouseout="mouseOutClass('MusicSet6')"
         class="MusicClass" @click="this.$router.push('/partition/国语')">
        更多
      </span>
    </div>
    <div id="musicClass" v-if="recommandMusicSet.length > 0">
      <span v-for="(music, index) in nowMusicSet" :key="index" class="musicClassSpan">
        <div class="musicPicContainer">
          <img :src="music.coverPath" class="musicPic" @click="playaudio(music)" style="cursor: pointer;">
        </div>
        <span :title="music.name" class="musicClassName" :id="`musicClass-${index}`"
          @mouseover='mouseOverClass(`musicClass-${index}`)' @mouseout='mouseOutClass(`musicClass-${index}`)'
          @click="playaudio(music)" style="cursor: pointer;">
          {{ music.name }}
        </span>
      </span>
    </div>
    <el-carousel indicator-position="outside" @arrow-click="handleArrowClick" style="height: 400px;margin-top: 20px;">
      <el-carousel-item v-for="(item, index) in nowIcon" :key="index" style="height: 400px;">
        <div class="carousel-item-wrapper" style="width: 80%;margin-left: 10%;">
          <div class="carousel-item-content" v-if="item[0] != undefined">
            <img :src="item[0].icon" style="height: 175px;width: 175px;cursor: pointer;" @click="toListRoute(item[0].id)">
            <br>
            <span :id="'light' + index">{{ item[0].name }}</span>
          </div>
          <div class="carousel-item-content" v-if="item[1] != undefined">
            <img :src="item[1].icon" style="height: 175px;width: 175px;cursor: pointer;" @click="toListRoute(item[1].id)">
            <br>
            <span :id="'light' + index">{{ item[1].name }}</span>
          </div>
          <div class="carousel-item-content" v-if="item[2] != undefined">
            <img :src="item[2].icon" style="height: 175px;width: 175px;cursor: pointer;" @click="toListRoute(item[2].id)">
            <br>
            <span :id="'light' + index">{{ item[2].name }}</span>
          </div>
          <div class="carousel-item-content" v-if="item[3] != undefined">
            <img :src="item[3].icon" style="height: 175px;width: 175px;cursor: pointer;" @click="toListRoute(item[3].id)">
            <br>
            <span :id="'light' + index">{{ item[3].name }}</span>
          </div>
          <div class="carousel-item-content" v-if="item[4] != undefined">
            <img :src="item[4].icon" style="height: 175px;width: 175px;cursor: pointer;" @click="toListRoute(item[4].id)">
            <br>
            <span>{{ item[4].name }}</span>
          </div>
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
  <div class="musicClub" v-if="isLoaded">
    <h1 style="font-weight: 500;letter-spacing:15px; margin-top: 50px;">
      音乐推荐
    </h1>
    <div>
      <span id="Music1" @mouseover="mouseOverClass('Music1')" @mouseout="mouseOutClass('Music1')"
        @click="mouseClickClass('Music1')" class="MusicClass">
        为你推荐
      </span>
      <span id="Music2" @mouseover="mouseOverClass('Music2')" @mouseout="mouseOutClass('Music2')"
        @click="mouseClickClass('Music2')" class="MusicClass">
        电子
      </span>
      <span id="Music3" @mouseover="mouseOverClass('Music3')" @mouseout="mouseOutClass('Music3')"
        @click="mouseClickClass('Music3')" class="MusicClass">
        流行
      </span>
      <span id="Music4" @mouseover="mouseOverClass('Music4')" @mouseout="mouseOutClass('Music4')"
        @click="mouseClickClass('Music4')" class="MusicClass">
        ACG
      </span>
      <span id="Music5" @mouseover="mouseOverClass('Music5')" @mouseout="mouseOutClass('Music5')"
        @click="mouseClickClass('Music5')" class="MusicClass">
        摇滚
      </span>
      <span id="Music6" @mouseover="mouseOverClass('Music6')" @mouseout="mouseOutClass('Music6')" class="MusicClass" @click="this.$router.push('/partition/国语')">
        更多
      </span>
    </div>
    <div id="musicClass" v-if="recommandMusicSet.length > 0">
      <span v-for="(music, index) in nowMusicSet" :key="index" class="musicClassSpan">
        <div class="musicPicContainer">
          <img :src="music.coverPath" class="musicPic" @click="playaudio(music)" style="cursor: pointer;">
        </div>
        <span :title="music.name" class="musicClassName" :id="`musicClass-${index}`"
          @mouseover='mouseOverClass(`musicClass-${index}`)' @mouseout='mouseOutClass(`musicClass-${index}`)'
          @click="playaudio(music)" style="cursor: pointer;">
          {{ music.name }}
        </span>
      </span>
    </div>
    <el-carousel indicator-position="outside" @arrow-click="handleArrowClick" style="height: 400px;margin-top: 20px;">
      <el-carousel-item v-for="(item, index) in nowMusic" :key="index" style="height: 400px;">
        <div class="carousel-item-wrapper" style="width: 80%;margin-left: 10%;">
          <div class="carousel-item-content" v-if="item[0] != undefined">
            <img :src="item[0].icon" style="height: 175px;width: 175px;cursor: pointer;" @click="toSongRoute(item[0].id)">
            <br>
            <span :id="'light' + index">{{ item[0].name }}</span>
          </div>
          <div class="carousel-item-content" v-if="item[1] != undefined">
            <img :src="item[1].icon" style="height: 175px;width: 175px;cursor: pointer;" @click="toSongRoute(item[1].id)">
            <br>
            <span :id="'light' + index">{{ item[1].name }}</span>
          </div>
          <div class="carousel-item-content" v-if="item[2] != undefined">
            <img :src="item[2].icon" style="height: 175px;width: 175px;cursor: pointer;" @click="toSongRoute(item[2].id)">
            <br>
            <span :id="'light' + index">{{ item[2].name }}</span>
          </div>
          <div class="carousel-item-content" v-if="item[3] != undefined">
            <img :src="item[3].icon" style="height: 175px;width: 175px;cursor: pointer;" @click="toSongRoute(item[3].id)">
            <br>
            <span :id="'light' + index">{{ item[3].name }}</span>
          </div>
          <div class="carousel-item-content" v-if="item[4] != undefined">
            <img :src="item[4].icon" style="height: 175px;width: 175px;cursor: pointer;" @click="toSongRoute(item[4].id)">
            <br>
            <span>{{ item[4].name }}</span>
          </div>
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<style  scoped>
:root {
  --main-color: #42b983;
}

.carousel-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel-item-wrapper {
  display: flex;
}

.carousel-item-content {
  flex: 1;
  width: 250px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: transparent;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: transparent;
}

#imgThing {
  width: 1000px;
  left: 200px;
  margin-top: 50px;
}


.el-carousel__item:nth-child(2n) {
  background-color: transparent;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: transparent;
}

#recommand {
  color: var(--main-color);
}

.MusicClass {
  cursor: pointer;
  font-weight: 200;
  font-size: 15px;
}

.musicClassSpan {
  margin-right: 20px;
}

#musicClass {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
}

.musicClassName {
  overflow: hidden;
  text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  /*width: 40px;*/
  max-width: 200px;
  display: inline-block;
}

.musicPic {
  height: 200px;
  width: 200px;
  display: block;
  margin: 0 auto 10px;
}

.musicPicContainer {
  position: relative;
  overflow: hidden;
  width: 200px;
  height: 200px;
}

.musicPic {
  transition: transform 0.3s;
}

.musicPic:hover {
  transform: scale(1.2);
}

#BottomNav {
  display: flex;
  align-items: center;
  position: fixed;
  bottom: 0;
  border: 0.5px solid gray;
  height: 13%;
  width: 100%;
  background-color: rgb(242, 242, 242);
}

#nowMusicPlayingText {
  position: relative;
  margin-left: 100px;
}

.nowPlayingMusicCover {
  position: relative;
  left: 2.5%;
  height: 70%;
  aspect-ratio: 1 / 1;
  border-radius: 10px;
}

.custom-carousel {
  height: 400px;
}
</style>
<script>
import Music from '../components/music.js';
import store from '@/store';
import { mapActions } from "vuex";
import playAudio1 from '../App.vue';
import User from '../components/User'
import { audioElement, pauseAudio, adjustVolume } from '../components/Audio';
import { reactive, ref } from 'vue';
import { getTagSongList } from '../api/musicClub'
import { getTagSong } from '../api/musicClub'
import { getTagSongtRandom } from '../api/musicClub'
export default {
  mixins: [playAudio1],
  data() {
    return {
      nowPlayingMusic: null,
      nowClassid: 'MusicSet1',
      recommandMusicSet: [],
      MusicSet1: [],
      MusicSet2: [],
      MusicSet3: [],
      MusicSet4: [],
      MusicSet5: [],
      MusicSet6: [],
      Music1: [],
      Music2: [],
      Music3: [],
      Music4: [],
      Music5: [],
      Music6: [],
      nowMusicSet: [],
      isLoaded: false,
      step: 5,
      nowIcon: [],
      page: 0,
      nowMusic: [],
      MusicTag: null,
    }
  },

  created() {
  },
  methods: {
    ...mapActions([
      'ChangeNowPlayMusic',
      'updateLoginUser',
      'updateImageDataUrl',
      'addAttentionUser',
    ]),
    toSongRoute(id) {
      this.$router.push('/music/' + id);
    },
    toListRoute(id) {
      this.$router.push('/user/songList/' + id);
    },
    changeIcon(musicSet) {
      for (let i = 0; i < musicSet.length; i++) {
        musicSet[i].cover_address = 'https://' + musicSet[i].cover_address;
      }
      return musicSet;
    },
    async init() {
      var temp1 = await getTagSongtRandom('False')
      var temp2 = await getTagSongList('国语')
      var temp3 = await getTagSongList('轻音乐')
      var temp4 = await getTagSongList('ACG')
      var temp5 = await getTagSongList('治愈')
      this.MusicSet1 = temp1.data
      this.MusicSet1 = this.changeIcon(this.MusicSet1)
      this.MusicSet2 = temp2.data;
      this.MusicSet2 = this.changeIcon(this.MusicSet2)
      this.MusicSet3 = temp3.data;
      this.MusicSet3 = this.changeIcon(this.MusicSet3)
      this.MusicSet4 = temp4.data;
      this.MusicSet4 = this.changeIcon(this.MusicSet4)
      this.MusicSet5 = temp5.data;
      this.MusicSet5 = this.changeIcon(this.MusicSet5)
      this.nowMusicSet = this.MusicSet1;
      var temp11 = await getTagSongtRandom('True')
      var temp12 = await getTagSong('电子')
      var temp13 = await getTagSong('流行')
      var temp14 = await getTagSong('ACG')
      var temp15 = await getTagSong('摇滚')
      this.Music1 = temp11.data;
      this.Music1 = this.changeIcon(this.Music1)
      this.Music2 = temp12.data;
      this.Music2 = this.changeIcon(this.Music2)
      this.Music3 = temp13.data;
      this.Music3 = this.changeIcon(this.Music3)
      this.Music4 = temp14.data;
      this.Music4 = this.changeIcon(this.Music4)
      this.Music5 = temp15.data;
      this.Music5 = this.changeIcon(this.Music5)
      this.nowMusic = this.Music1;
      this.isLoaded = true;
      this.divide(this.nowMusicSet);
      this.divide1(this.nowMusic);
    },
    playingNextMusic() {
      var temp = store.state.nowPlayingMusicSet.getNextMusic();
      this.playAudio1(temp);
    },
    mouseOverClass(id) {
      var newid = "#" + id;
      var element = document.querySelector(newid);
      element.style.color = this.getColor;
    },
    mouseOutClass(id) {
      var newid = "#" + id;
      if (id === this.nowClassid)
        return
      var element = document.querySelector(newid);
      element.style.color = 'black'
    },
    divide(musicSet) {
      this.nowIcon = [];
      for (let i = 0; i < musicSet.length / 5; i++) {
        var temp = [];
        for (let j = 0; j < 5; j++) {
          if (musicSet[i * 5 + j] != undefined) {
            var h = {
              icon: musicSet[i * 5 + j].cover_address,
              name: musicSet[i * 5 + j].title,
              id: musicSet[i * 5 + j].list_id
            }
            temp.push(h);
          }
        }
        this.nowIcon.push(temp);
      }
    },
    divide1(music) {
      this.nowMusic = [];
      for (let i = 0; i < music.length / 5; i++) {
        var temp = [];
        for (let j = 0; j < 5; j++) {
          if (music[i * 5 + j] != undefined) {
            var h = {
              icon: music[i * 5 + j].cover_address,
              name: music[i * 5 + j].title,
              id: music[i * 5 + j].song_id,
            }
            temp.push(h);
          }
        }
        this.nowMusic.push(temp);
      }
    },
    mouseClickClass(id) {
      var beforeId = "#" + this.nowClassid;
      var newId = "#" + id;
      var beforeEl = document.querySelector(beforeId);
      var nowEl = document.querySelector(newId);
      beforeEl.style.color = 'black';
      nowEl.style.color = this.getColor;
      this.nowClassid = id;
      switch (id) {
        case 'MusicSet1':
          this.nowMusicSet = this.MusicSet2
          break
        case "MusicSet2":
          this.nowMusicSet = this.MusicSet2
          break;
        case "MusicSet3":
          this.nowMusicSet = this.MusicSet3;
          break;
        case "MusicSet4":
          this.nowMusicSet = this.MusicSet4;
          break;
        case "MusicSet5":
          this.nowMusicSet = this.MusicSet5;
          break;
        case "Music1":
          this.nowMusic = this.Music1
          break;
        case "Music2":
          this.nowMusic = this.Music2
          break;
        case "Music3":
          this.nowMusic = this.Music3
          break;
        case "Music4":
          this.nowMusic = this.Music4
          break;
        case "Music5":
          this.nowMusic = this.Music5
          break;
      }
      this.divide(this.nowMusicSet);
      this.divide1(this.nowMusic);
    },
    playaudio(music) {
      this.playAudio1(music);
    },
    pauseAudio() {
      pauseAudio();
    },
    handleArrowClick(direction) {
      if (direction === 'prev') {
        if (this.page == 0)
          this.page = (this.nowMusicSet.length / 5) - 1;
        else
          this.page--;
        for (let i = 0; i < 5; i++) {
          this.nowList.push(this.nowMusicSet[this.page * 5 + i]);
        }
      } else if (direction === 'next') {
        if (this.page == (this.nowMusicSet.length / 5) - 1)
          this.page = 0;
        else
          this.page++;
        for (let i = 0; i < 5; i++) {
          this.nowList.push(this.nowMusicSet[this.page * 5 + i]);
        }
      }
    },
  },
  computed: {
    getColor() {
      return getComputedStyle(document.documentElement).getPropertyValue('--main-color');
    },

  },
  mounted() {
    this.init();
    this.nowMusicSet = this.recommandMusicSet;
  }
}
</script>
