<template>
  <nav>
    <span style="font-size: 30px; font-family: 楷体" @click="toAdminPage" class="site_name">丘丘音乐</span>
    <span class="rountSpan" id="router1Span" style="background-color: var(--main-color); color: white"><router-link to="/"
        class="router" id="router1" @mouseover="changeMouseOver('router1')" @mouseout="changeMouseOut('router1')"
        @click="clickRouter('router1')">音乐馆</router-link>
    </span>
    <span class="rountSpan" id="router2Span">
      <router-link :to="'/user/info/' + store.state.loginUser.id" class="router" id="router2"
        @mouseover="changeMouseOver('router2')" @mouseout="changeMouseOut('router2')" v-if="store.state.loginUser">
        个人页面</router-link>
      <router-link :to="'/login'" class="router" id="router2" @mouseover="changeMouseOver('router2')"
        @mouseout="changeMouseOut('router2')" @click="checkGlobalLogin" v-else>
        个人页面</router-link>
    </span>
    <span class="rountSpan" id="router3Span">
      <router-link :to="'/mySongList/' + store.state.loginUser.id" class="router" id="router3"
        @mouseover="changeMouseOver('router3')" @mouseout="changeMouseOut('router3')" v-if="store.state.loginUser">
        我的歌单</router-link>
      <router-link :to="'/login'" class="router" id="router3" @mouseover="changeMouseOver('router3')"
        @mouseout="changeMouseOut('router3')" @click="checkGlobalLogin" v-else>
        我的歌单</router-link>
    </span>
    <span class="rountSpan" id="router4Span">
      <router-link :to="'/history/' + store.state.loginUser.id" class="router" id="router4"
        @mouseover="changeMouseOver('router4')" @mouseout="changeMouseOut('router4')" v-if="store.state.loginUser">
        最近播放</router-link>
      <router-link :to="'/login'" class="router" id="router4" @mouseover="changeMouseOver('router4')"
        @mouseout="changeMouseOut('router4')" @click="checkGlobalLogin" v-else>
        最近播放</router-link>
    </span>
    <span style="
        display: flex;
        border: 2px solid;
        justify-content: center;
        height: 36%;
      ">
      <el-input id="searchInput" style="border: none; outline: none" v-model="this.searchKeywords_in_nav"
        placeholder="搜索歌曲、歌单" maxlength="30" @keydown.enter.native="search_in_nav"></el-input>
      <button id="searchButton" @click="search_in_nav()" @mouseover="overOtherChangeColor('searchButton', 'white')"
        @mouseout="outOtherChangeColor('searchButton')">
        搜索
      </button>
    </span>
    <router-link to="/" id="loginButton" @mouseover="overOtherChangeColor('loginButton', `${this.getColor}`)"
      @mouseout="outOtherChangeColor('loginButton')" @click="globalLogOut" style="cursor: pointer"
      v-if="store.state.loginUser">欢迎{{ store.state.loginUser.name }} - 点击登出</router-link>
    <router-link to="/login" id="loginButton" @mouseover="overOtherChangeColor('loginButton', `${this.getColor}`)"
      @mouseout="outOtherChangeColor('loginButton')" style="cursor: pointer" v-else>登录</router-link>
  </nav>

  <router-view v-slot="{ Component }">
    <component ref="router_view" :is="Component" />
  </router-view>
  <!--  <router-view ref="router_view"/>-->

  <div class="bottom_place_holder" content=""></div>
  <transition name="music_play_page_trans">
    <div class="music_play_page" v-if="show_play_page">
      <div class="music_play_page_left music_play_page_div">
        <span class="music_play_page_back" @click="toInfoPage">
          <el-icon class="backicon" color="#ffffff" size="100%">
            <ArrowLeftBold />
          </el-icon>
          返回
        </span>
        <span class="music_play_page_span" id="music_play_span_song_img">
          <img alt="" :src="this.playCoverSource" class="music_play_page_song_img" @click="toMusicPage" />
        </span>
        <span class="music_play_page_span" id="music_play_span_song_name" @click="toMusicPage">
          {{ song_name }}
        </span>
        <span class="music_play_page_span" id="music_play_span_singer">
          {{ song_singer }}
        </span>
        <!--                <span>element-scroll_height:{{this.scroll_height}}</span><br>-->
        <!--                <span>element-scroll_top:{{this.scroll_top}}</span>-->
      </div>
      <div class="music_play_page_middle music_play_page_div">
        <span class="music_play_page_middle_placeholder"></span>
        <span v-if="has_lyric" class="music_play_page_middle_placeholder" id="music_play_middle_lyric"
          @mouseover="NoScroll" @mouseout="YesScroll">
          <el-scrollbar ref="scr_ref" id="scroll_lyric">
            <span v-for="(item, index) in $store.state.globalLyricSets.ms" class="music_play_page_lyric_line" :key="index"
              @click="setPlayTime(item.t)" :style="{
                background:
                  this.currentIndex === index ? 'rgb(63,157,253)' : '',
                color: this.currentIndex === index ? 'white' : '',
              }">
              {{ item.c }}
            </span>
            <!--                    <span id="div1">{{store.state.globalLyric}}</span>-->
          </el-scrollbar>
        </span>
        <span v-else class="music_play_page_middle_placeholder" id="music_play_middle_lyric">
          <span class="music_play_page_lyric_line" id="default_lrc">{{
            default_lrc
          }}</span>
        </span>
      </div>
      <div class="music_play_page_right music_play_page_div">
        <el-scrollbar>
          播放列表
          <span v-for="(item, index) in $store.state.nowPlayingMusicSet.list" class="music_play_page_right_list" :style="{
            background:
              store.state.nowPlayMusic.id === item.id
                ? 'rgb(63,157,253)'
                : '',
          }" :key="index">
            <span style="
                margin: 0;
                padding-left: 5px;
                height: 100%;
                width: 90%;
                align-items: center;
                display: flex;
              " @click="this.playAudio1(item)">
              <span class="music_play_page_right_list_name" :title="item.name">{{ item.name }}</span>
              <span class="music_play_page_right_list_singer" :title="item.author">- {{ item.author }}</span>
            </span>
            <span class="music_play_page_delete_btn" @click="this.deleteSongInList(item)"><el-icon class="close_icon">
                <Close />
              </el-icon></span>
          </span>
        </el-scrollbar>
      </div>
    </div>
  </transition>
  <!--    new player-->
  <div class="audio-player music_player">
    <transition name="play_pause" mode="out-in" @click="toInfoPage">
      <img alt="" :src="this.playCoverSource" class="nowPlayingMusicCover_player" />
    </transition>
    <div class="audio-mock-player">
      <!-- 上一首 -->
      <el-icon class="preicon" @click="playLastMusic" color="#ffffff" size="200%">
        <ArrowLeftBold />
      </el-icon>
      <!-- "暂停" : "播放" -->
      <el-icon class="play-sty" @click="pauseMusic" color="#ffffff" size="300%">
        <transition name="play_pause" mode="out-in">
          <CaretRight v-if="!play" />
          <VideoPause v-else />
        </transition>
      </el-icon>
      <!-- 下一首 -->
      <el-icon class="preicon" @click="playNextMusic2" color="#ffffff" size="200%">
        <ArrowRightBold />
      </el-icon>

      <div class="right-menu">
        <div class="song_and_singer_name">
          <span class="song_name" :title="song_name" @click="toMusicPage">{{
            song_name
          }}</span>
          <span class="singer_name" :title="song_singer">- {{ song_singer }}</span>
          <span class="duration_upward">/{{ duration }}</span>
          <span class="current_upward">{{ currentTime }}</span>
        </div>
        <div class="bottom">
          <!--  播放进度条 -->
          <el-slider class="progress" v-model="sliderVal" :format-tooltip="formatTooltip" :show-tooltip="true"
            :min="sliderMin" :max="sliderMax" @input="spliderSelect" ref="slider1" />
        </div>
      </div>
      <div class="volume">
        <!-- 有时候我们在对于一些hover定位元素，当离开时候就没了，这个时候可以使用ctrl+shift+c的快捷键来获取。 -->
        <el-popover placement="top-start" trigger="hover" popper-class="poppervolume-class" width="50px" :show-after="0"
          :hide-after="400">
          <el-slider class="volume-progress" vertical height="100px" :step="0.1" v-model="sliderValVolume"
            :show-tooltip="true" :format-tooltip="formatTooltipVolume" :min="0" :max="1" @input="spliderSelectVolume" />
          <template v-slot:reference>
            <transition name="play_pause" mode="out-in">
              <img @click="changeVolumes" :src="volumeIcon" alt="" :width="32" :height="32" v-if="sliderValVolume" />
              <img @click="changeVolumes" :src="mutedIcon" alt="" :width="32" :height="32" v-else />
            </transition>
          </template>
        </el-popover>
      </div>
      <div class="volume">
        <!-- 有时候我们在对于一些hover定位元素，当离开时候就没了，这个时候可以使用ctrl+shift+c的快捷键来获取。 -->
        <transition name="play_pause" mode="out-in">
          <img @click="changeLovelist" :src="in_love_listIcon" alt="" v-if="in_lovelist" :width="32" :height="32" />
          <img @click="changeLovelist" :src="not_in_love_listIcon" alt="" :width="32" :height="32" v-else />
        </transition>
      </div>
      <div class="volume">
        <!-- 有时候我们在对于一些hover定位元素，当离开时候就没了，这个时候可以使用ctrl+shift+c的快捷键来获取。 -->
        <!--                <transition name="play_pause" mode="out-in">-->
        <img @click="changePlaySequence" :src="sequence_play" alt="" v-if="play_sequence === 0" :width="28"
          :height="28" />
        <img @click="changePlaySequence" :src="single_song" alt="" v-if="play_sequence === 1" :width="28" :height="28" />
        <img @click="changePlaySequence" :src="random_play" alt="" v-if="play_sequence === 2" :width="28" :height="28" />
        <!--                </transition>-->
      </div>
      <div class="volume moreicon">
        <!-- 有时候我们在对于一些hover定位元素，当离开时候就没了，这个时候可以使用ctrl+shift+c的快捷键来获取。 -->
        <el-icon color="white" size="32" @click="toInfoPage">
          <MoreFilled />
        </el-icon>
      </div>
    </div>
  </div>
</template>
<style>
:root {
  --main-color: #42b983;
}

#app {
  height: 100%;
  margin: 0;
  padding: 0;
  text-align: center;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: black;
}

template {
  height: 20%;
}

nav {
  height: 100px;
  width: 100%;
  min-width: 1200px;
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}

span {
  margin-right: 4%;
  font-size: 20px;
}

.router {
  color: black;
  text-decoration: none;
  transition: 0.5s;
}

.router:hover {
  scale: 1.25;
  color: #42b983;
  transition: 0.2s;
}

#router1 {
  color: white;
  transition: 0.5s;
}

#router1 :hover {
  color: white;
  scale: 1.25;
  transition: 0.2s;
}

.timeSpan {
  text-align: left;
  margin-left: 5%;
  color: rgb(164, 161, 161);
  font-size: 7px;
}

#musicList {
  position: fixed;
  top: 0;
  right: 0%;
  height: 100%;
  width: 30%;
}

#searchButton {
  cursor: pointer;
  width: 50px;
  margin-right: 0px;
  border: none;
  background-color: var(--main-color);
  font-size: 15px;
  font-weight: 200;
}

.site_name:hover {
  cursor: pointer;
}

.rountSpan {
  cursor: pointer;
  width: 8%;
  display: flex;
  height: 100%;
  align-items: center;
  justify-content: center;
}

.changeStatusButton {
  cursor: pointer;
  border: 0;
  margin-right: 30px;
}

#changeStatusSpan {
  margin-left: 0%;
  margin-top: -35px;
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

.slider-demo-block {
  margin-left: 92.5%;
  background-color: white;
  height: 100px;
  width: 50px;
  border-radius: 10px;
  align-items: center;
}

.slider-demo-block .el-slider {
  height: 30px;
  margin-top: 0;
  margin-left: 0px;
  align-items: center;
}

.bottom_place_holder {
  height: 9%;
  background-color: grey;
}

/*music_player*/

.poppervolume-class {
  min-width: 10px !important;
  padding: 12px 5px !important;
}

.music_player {
  position: fixed;
  /*border: black 1px solid;*/
  width: 100%;
  height: 9%;
  bottom: 0;
  z-index: 999;
}

.music_play_page {
  position: fixed;
  /*border: black 1px solid;*/
  width: 100%;
  height: 91%;
  top: 0;
  padding-left: 2%;
  z-index: 900;
  background: rgba(0, 0, 0, 0.7);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  /*border-radius: 25px;*/
  /*box-shadow:inset 0 0 6px rgba(255, 255, 255, 0.2);*/
  color: lightgrey;
  font-size: 22px;
  min-width: 1200px;
}

.music_play_page_div {
  /*margin-top: 5px;*/
  height: 98%;
  width: 26%;
  float: left;
  display: inline-block;
  /*border: 1px solid white;*/
  /*background-color: green;*/
}

.music_play_page_left {
  background-color: rgba(0, 0, 0, 0);
}

.music_play_page_middle {
  width: 44%;
  overflow-y: auto;
  overflow-x: hidden;
  align-items: center;
  /*display: flex;*/
}

.music_play_page_right {
  overflow: auto;
  background-color: rgba(0, 0, 0, 0);
  border-left: 2px lightgrey dashed;
  /*box-shadow: -3px 0 3px -2px rgb(255,255,255);*/
}

.music_play_page_back {
  display: block;
  /*border: 1px solid red;*/
  margin-top: 5%;
  font-size: 24px;
  width: 30%;
  transition: 0.2s;
}

.music_play_page_back:hover {
  cursor: pointer;
  color: white;
  transition: 0.2s;
}

.music_play_page_span {
  display: block;
  /*border: 1px solid red;*/
  font-size: 24px;
  /*width: 30%;*/
  transition: 0.2s;
}

.music_play_page_span:hover {
  cursor: pointer;
  color: white;
  transition: 0.2s;
}

#music_play_span_song_img {
  margin-top: 35%;
}

.music_play_page_song_img {
  height: 60%;
  width: 60%;
  border-radius: 20px;
  transition: 0.5s;
}

.music_play_page_song_img:hover {
  cursor: pointer;
  box-shadow: 0 0 80px 30px white;
  transition: 0.2s;
}

#music_play_span_song_name {
  margin-top: 10%;
  font-size: 32px;
  color: white;
  overflow: hidden;
  text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  /*width: 40px;*/
  max-width: 100%;
  display: block;
  transition: 0.5s;
}

#music_play_span_song_name:hover {
  scale: 1.15;
  transition: 0.2s;
}

#music_play_span_singer {
  margin-top: 1%;
  overflow: hidden;
  text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  /*width: 40px;*/
  max-width: 100%;
  display: block;
  transition: 0.5s;
}

#music_play_span_singer:hover {
  scale: 1.15;
  transition: 0.2s;
}

.music_play_page_middle_placeholder {
  display: block;
  /*background: green;*/
  height: 10%;
  /*transition: 0.5s;*/
  /*scroll-behavior: smooth;*/
}

#music_play_middle_lyric {
  height: 80%;
  border: 1px solid rgba(0, 0, 0, 0);
  transition: 0.5s;
}

#scroll_lyric {
  /*scroll-behavior: smooth;*/
  /*transition: 0.5s;*/
}

.music_play_page_lyric_line {
  display: block;
  /*border: 1px solid red;*/
  font-size: 22px;
  line-height: 40px;
  height: 40px;
  margin: 0;
  padding: 0;
  /*margin-top: 1%;*/
  /*margin-bottom: 1%;*/
  /*margin: auto;*/
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  /*width: 40px;*/
  max-width: 100%;
  transition: 0.2s;
}

.music_play_page_lyric_line:hover {
  cursor: pointer;
  color: white;
  transition: 0.2s;
}

#default_lrc {
  font-size: 36px;
  margin-top: 40%;
  transition: 0.5s;
}

#default_lrc:hover {
  scale: 1.25;
  transition: 0.2s;
}

.music_play_page_right_list {
  display: flex;
  align-items: center;
  /*justify-content: center;*/
  height: 50px;
  margin: 10px;
  /*padding-left: 5px;*/
  text-align: left;
  border-radius: 4px;
  background: rgba(125, 125, 125, 0.5);
  color: lightgrey;
  transition: 0.5s;
  overflow: hidden;
}

.music_play_page_right_list:hover {
  cursor: pointer;
  background: rgba(255, 255, 255, 0.5);
  transition: 0.2s;
}

.music_play_page_right_list_name {
  color: white;
  margin-right: 4px;
  overflow: hidden;
  text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  /*width: 40px;*/
  max-width: 70%;
  display: inline-block;
}

.music_play_page_right_list_singer {
  font-size: 14px;
  margin-left: 0;
  padding-left: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  -o-text-overflow: ellipsis;
  white-space: nowrap;
  /*width: 40px;*/
  max-width: 35%;
  display: inline-block;
}

.music_play_page_delete_btn {
  position: relative;
  right: -1%;
  /*float: right;*/
}

.backicon {
  width: 32px;
  height: 32px;
  border-radius: 26px;
  transition: 0.5s;
}

.backicon:hover {
  cursor: pointer;
  transform: rotate(-90deg);
  scale: 1.25;
  transition: 0.2s;
}

.close_icon {
  z-index: 999;
  border-radius: 50%;
  transition: 0.5s;
}

.close_icon:hover {
  cursor: pointer;
  transform: rotate(-90deg);
  scale: 1.25;
  background: red;
  transition: 0.2s;
}

.play_pause-enter-active,
.play_pause-leave-active {
  transition: opacity 0.15s ease;
}

.play_pause-enter-from,
.play_pause-leave-to {
  opacity: 0;
}

.music_play_page_trans-enter-active,
.music_play_page_trans-leave-active {
  transition: opacity 0.3s ease;
}

.music_play_page_trans-enter-from,
.music_play_page_trans-leave-to {
  opacity: 0;
}

.audio-player {
  background: rgba(34, 34, 34, 0.85);
  display: flex;
  align-items: center;
  position: fixed;
  /*bottom: 0;*/
  /*height: 9%;*/
  /*width: 100%;*/
  box-shadow: 0 0 20px 5px rgba(34, 34, 34, 0.85);
  min-width: 1200px;

  .audio-mock-player {
    //border: black 1px solid;
    position: relative;
    width: 92%;
    left: 0.5%;
    padding: 15px;
    //background: rgba(34, 34, 34, 0.8);
    //border: 1px solid rgba(34, 34, 34, 1);
    border-radius: 8px;
    display: flex;
    align-items: center;

    .play-sty {
      margin: 0 6px;
      //padding-left: 2px;
      width: 52px;
      height: 52px;
      border-radius: 26px;
      background-color: #3f9dfd;
      transition: 0.2s;
    }

    .play-sty:hover {
      cursor: pointer;
      box-shadow: 0px 0px 20px 5px white;
      transition: 0.2s;
    }

    .preicon {
      width: 32px;
      height: 32px;
      border-radius: 26px;
      transition: 0.2s;
    }

    .preicon:hover {
      cursor: pointer;
      box-shadow: inset 0px 0px 20px 2px white;
      transition: 0.2s;
    }

    .closeicon {
      position: absolute;
      right: -10px;
      top: -10px;
      width: 20px;
      height: 20px;
    }

    .right-menu {
      margin-left: 20px;
      margin-right: 20px;
      flex: 1;
      padding-right: 0;

      .bottom {
        display: flex;
        align-items: center;

        .progress {
          flex: 1;
        }

        .current {
          font-family: PingFangSC-Regular;
          font-size: 12px;
          color: #ffffff;
          text-align: left;
          font-weight: 400;
          margin-left: 12px;
          margin-right: 5px;
        }

        .duration {
          opacity: 0.6;
          font-family: PingFangSC-Regular;
          font-size: 12px;
          color: #ffffff;
          text-align: left;
          font-weight: 400;
          margin-right: 16px;
          margin-left: 0;
        }
      }

      .song_and_singer_name {
        height: 20px;
        font-family: PingFangSC-Regular;
        font-size: 25px;
        color: #ffffff;
        text-align: left;
        font-weight: 400;
        margin-bottom: 10px;
        //border: black 1px solid;
        //display: flex;
      }

      .song_name {
        font-size: 25px;
        margin-right: 10px;
        overflow: hidden;
        transition: 0.1s;
        overflow: hidden;
        text-overflow: ellipsis;
        -o-text-overflow: ellipsis;
        white-space: nowrap;
        /*width: 40px;*/
        max-width: 60%;
        display: inline-block;
      }

      .song_name:hover {
        cursor: pointer;
        border-bottom: white 1.5px solid;
        transition: 0.1s;
      }

      .singer_name {
        font-size: 16px;
        //margin-top: 10px;
        margin-right: 0;
        margin-bottom: 2px;
        overflow: hidden;
        transition: 0.1s;
        overflow: hidden;
        text-overflow: ellipsis;
        -o-text-overflow: ellipsis;
        white-space: nowrap;
        /*width: 40px;*/
        max-width: 27%;
        display: inline-block;
      }

      .singer_name:hover {
        border-bottom: white 1.5px solid;
        transition: 0.1s;
      }

      .current_upward {
        margin-top: 10px;
        font-family: PingFangSC-Regular;
        font-size: 14px;
        color: #ffffff;
        text-align: right;
        font-weight: 400;
        //margin-left: 12px;
        margin-right: 5px;
        //justify-content: space-between;
        float: right;
      }

      .duration_upward {
        margin-top: 10px;
        opacity: 0.6;
        font-family: PingFangSC-Regular;
        margin-right: 0;
        font-size: 14px;
        color: #ffffff;
        text-align: right;
        font-weight: 400;
        //margin-right: 16px;
        margin-left: 0;
        //position: relative;
        //right: -55%;
        //justify-content: space-between;
        float: right;
      }
    }
  }

  .play_pause-enter-active,
  .play_pause-leave-active {
    transition: opacity 0.15s ease;
  }

  .play_pause-enter-from,
  .play_pause-leave-to {
    opacity: 0;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease;
  }

  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }

  .nowPlayingMusicCover_player {
    /*display: block;*/
    height: 52px;
    width: 52px;
    margin-left: 2.5%;
    border-radius: 10px;
    transition: 0.2s;
  }

  .nowPlayingMusicCover_player:hover {
    cursor: pointer;
    scale: 1.25;
    transition: 0.2s;
  }

  .volume {
    position: relative;
    /*border: black 1px solid;*/
    margin-right: 8px;

    img {
      width: 16px;
      height: 16px;
    }

    .volume-progress {
      position: absolute;
      top: -730px;
      left: -120px;
    }

    transition: 0.2s;
  }

  .volume:hover {
    cursor: pointer;
    scale: 1.25;
    transition: 0.2s;
  }
}
</style>

<script>
import { AxiosHeaders } from "axios"
import store from './store';
import { mapState } from 'vuex'
import { audioElement, pauseAudio, playAudio } from './components/Audio';
import { ref } from 'vue';
import { ArrowLeftBold, ArrowRightBold, CaretRight, MoreFilled, VideoPause } from "@element-plus/icons-vue";
import Music from "@/components/music";
import { Close, Delete } from "@element-plus/icons";
import { post, get, get2 } from "@/api/api";
import { addHistory } from "@/api/history";
import { addSong, deleteSong } from "@/api/likeList";
import { ElMessage } from 'element-plus';
import { addPlayed } from "./api/music";
import { checkSong } from "@/api/likeList";

export default {
  name: 'navView',
  components: {
    Close,
    ArrowRightBold, ArrowLeftBold, MoreFilled, CaretRight, VideoPause,
  },
  data() {
    return {
      playIcon: require('./assets/play.png'),
      pauseIcon: require('./assets/pause.png'),
      volumeIcon: require('./assets/volume.png'),
      mutedIcon: require('./assets/muted.png'),
      closeIcon: require('./assets/close.png'),
      in_love_listIcon: require('./assets/is_in_lovelist.png'),
      not_in_love_listIcon: require('./assets/not_in_lovelist.png'),
      playCoverSource: require('./assets/avatar10015.png'),
      playCoverSource_empty: require('./assets/avatar10015.png'),
      single_song: require('./assets/single_song.png'),
      sequence_play: require('./assets/sequence_play.png'),
      random_play: require('./assets/random_play.png'),
      lyricFilePath: null,
      box: null,
      play: false, // 播放状态，true为正在播放
      play_sequence: 0, // 0顺序播放，1单曲循环，2随机播放
      sliderVal: 0, // 这个对接当前时长。
      copySliderVal: 0,
      sliderMin: 0,
      sliderMax: 0, // 这个对接总时长。
      sliderValVolume: 0.5, // 音量
      copySliderValVolume: 0.5,
      duration: "--:--", // 音乐总时长
      currentTime: "--:--", // 当前播放时长
      in_lovelist: true, //当前播放歌曲是否在当前用户的喜爱列表
      song_name: "Olah! 欢迎来到丘丘音乐",
      song_singer: "飞翔的丘丘人",
      last_interval_playtime: 0,
      loginUser1: store.state.loginUser,
      show_play_page: false,
      now_playing_list: store.state.nowPlayingMusicSet,
      nowPlayingMusic: null,
      has_lyric: false,
      default_lrc: "丘丘音乐，听我想听",
      lrc: "",
      oLRC: {
        ti: "", //歌曲名
        ar: "", //演唱者
        al: "", //专辑名
        by: "", //歌词制作人
        offset: 0, //时间补偿值，单位毫秒，用于调整歌词整体位置
        ms: [] //歌词数组{t:时间,c:歌词}
      },
      scroll_height: 0,
      scroll_top: 0,
      currentIndex: 0,
      scroll_able: true,
      searchKeywords_in_nav: '',
    };
  },
  mounted() {
    setInterval(() => {
      // if (this.$route.path==='/'){
      //     var routerid = "#" + 'router1';
      //     var elementRouter = document.querySelector(routerid);
      //     elementRouter.style.color = 'white';
      //     var spanid = "#" + 'router1' + "Span";
      //     var elementSpan = document.querySelector(spanid);
      //     elementSpan.style.backgroundColor = this.getColor;
      // }
      // else {
      //     var routerid = "#" + 'router1';
      //     var elementRouter = document.querySelector(routerid);
      //     elementRouter.style.color = 'black';
      //     var spanid = "#" + 'router1' + "Span";
      //     var elementSpan = document.querySelector(spanid);
      //     elementSpan.style.backgroundColor = 'white';
      // }
      if (store.state.nowPlayMusic) {
        if (this.box == null) {
          this.box = audioElement;
        }
        this.has_lyric = store.state.nowPlayMusic.hasLyrics;
        var aftertime = this.box.currentTime;
        this.in_lovelist = store.state.nowPlayMusic.isInLovelist; //todo request in_lovelist
        // this.playCoverSource = this.list[this.index].playCoverPath //todo:request playcover_source
        //   this.playCoverSource = require("../../public/img/pic1.jpg")
        this.playCoverSource = store.state.nowPlayMusic.coverPath;
        this.lyricFilePath = store.state.nowPlayMusic.lyricPath;
        this.createLrcObj(store.state.globalLyric);
        if (this.$refs.scr_ref && this.play) {
          this.scroll_top = this.$refs.scr_ref.wrapRef.scrollTop;
          this.scroll_height = this.$refs.scr_ref.wrapRef.scrollHeight;
          this.setupScroll();
        }
        // let imgurl;
        // imgurl = this.list[this.index].playCoverPath.split('../../public/img/')[1]
        // this.playCoverSource = require('../../public/img/' + imgurl)//todo:从后端获取图片也是如此吗
        const total1 = this.formatTime(this.box.duration)
        const current1 = this.formatTime(this.box.currentTime)
        this.duration = `${total1.min}:${total1.sec}`
        this.currentTime = `${current1.min}:${current1.sec}`
        // //console.log('duration in mounted',this.duration)
        this.song_name = store.state.nowPlayMusic.name;
        this.song_singer = store.state.nowPlayMusic.author;
        // //console.log('song_name in mounted',this.song_name);
        this.sliderVal = Math.floor(this.box.currentTime);
        this.sliderMax = Math.floor(this.box.duration);
        // //console.log('sliderMax in mounted',this.sliderMax);
        this.play = this.last_interval_playtime !== aftertime;
        this.last_interval_playtime = aftertime;
        // //console.log("globalLyric",store.state.globalLyric);
        // //console.log("not empty");
        if (this.box.currentTime <= 0.01 && this.play === false) {
          this.playMusic();
        }
        if (this.box.duration - this.box.currentTime < 0.01) {
          this.playNextMusic();
        }
      }
      else {
        // //console.log("empty music set!")
      }
    }, 50)
  },
  created() {
    this.isHover = false;
    // this.nowPlayingMusic = store.state.nowPlayMusic;
    this.nowPlayingMusic = null;
    this.isPause = false;
    this.isListShow = ref(false);
    this.box = audioElement;
    ////console.log('created')
  },
  methods: {
    checkGlobalLogin() {
      if (!store.state.globalLogin) {
        ElMessage({
          message: '请先登录',
          type: 'warning',
        });
      }
    },
    toAdminPage() {
      if (store.state.globalLogin && store.state.loginUser.isAdmin === true) {
        this.$router.push('/manage');
      }
      else {
        this.$router.push('/');
        this.clickRouter('router1');
      }
    },
    globalLogOut() {
      this.setDefaultPlayer();
      store.commit('GLOBALLOGOUT', 0);
    },
    async search_in_nav() {
      if (this.searchKeywords_in_nav === '') {
        ElMessage({
          message: '请输入搜索内容',
          type: 'warning',
        });
      }
      else if (this.$route.name === 'search') {
        // this.search1(this.searchKeywords_in_nav);
        ////console.log("in search");
        ////console.log("this.ref",this.$refs['router_view'].search1(''));
        await this.$refs['router_view'].search1(this.searchKeywords_in_nav);
        this.searchKeywords_in_nav = '';
      }
      else {
        this.$router.push('/search/' + this.searchKeywords_in_nav);
        this.searchKeywords_in_nav = '';
      }
    },
    changePlaySequence() {
      if (this.play_sequence < 2)
        this.play_sequence += 1;
      else
        this.play_sequence = 0;
      ////console.log("now sequence",this.play_sequence);
    },
    NoScroll() {
      this.scroll_able = false;
    },
    YesScroll() {
      this.scroll_able = true;
    },
    setPlayTime(to_time) {
      this.box.currentTime = to_time;
      this.playMusic();
    },
    setupScroll() {
      const container = document.querySelector('#music_play_middle_lyric');
      const containerHeight = container.clientHeight
      let index = this.monitorAudio();
      this.currentIndex = index;
      this.scroll_top = this.$refs.scr_ref.wrapRef.scrollTop;
      this.scroll_height = this.$refs.scr_ref.wrapRef.scrollHeight;
      let scroll_to = index * 40 + 40 - containerHeight / 2;
      //console.log("scr_to",scroll_to);
      if (this.scroll_able)
        this.$refs.scr_ref.setScrollTop(scroll_to);
    },
    monitorAudio() {
      // 使用内置api currentTime 获取当前播放的时间
      const currentAudioTime = this.box.currentTime
      // 如果当前播放时间小于某一项的时间,就返回他前面一项的数据
      if (store.state.globalLyricSets.ms[0] && currentAudioTime <= store.state.globalLyricSets.ms[0].t)
        return -666;

      const index =
        store.state.globalLyricSets.ms.findIndex(item => {
          return item.t > currentAudioTime
        }) - 1
      // 若索引小于0表示歌曲播放结束了
      return index < 0 ? store.state.globalLyricSets.ms.length - 1 : index;
    },
    async playAudio2(id) {
      let local_test_music = new Music(id);
      await local_test_music.initializeMusicInfo(id);
      // //console.log("in play3",local_test_music.musicPath);
      await this.playAudio1(local_test_music);
    },
    async getLRC(temp_music) {
      var temp1 = temp_music.lyricPath;
      var temp3 = temp_music.lyricCode;
      //console.log("in getLRC",temp_music.lyricPath);
      //console.log("in getLRC2",temp1);
      let temp2 = await get2(temp1, temp3);
      //console.log("judge lrc");
      //console.log(temp2);
      this.lrc = store.state.globalLyric;
      // //console.log("in get lrc2:",this.lrc);
      this.createLrcObj(store.state.globalLyric);
    },
    createLrcObj(lrc) {
      this.oLRC = {
        ti: "", //歌曲名
        ar: "", //演唱者
        al: "", //专辑名
        by: "", //歌词制作人
        offset: 0, //时间补偿值，单位毫秒，用于调整歌词整体位置
        kana: "",
        ms: [] //歌词数组{t:时间,c:歌词}
      }
      // //console.log("in create lrc:",this.oLRC);
      if (lrc.length === 0) return;
      var lrcs = lrc.split('\n');//用回车拆分成数组
      for (var i in lrcs) {//遍历歌词数组
        lrcs[i] = lrcs[i].replace(/(^\s*)|(\s*$)/g, ""); //去除前后空格
        var t = lrcs[i].substring(lrcs[i].indexOf("[") + 1, lrcs[i].indexOf("]"));//取[]间的内容
        var s = t.split(":");//分离:前后文字
        if (isNaN(parseInt(s[0]))) { //不是数值
          for (var i in this.oLRC) {
            if (i != "ms" && i == s[0].toLowerCase()) {
              this.oLRC[i] = s[1];
            }
          }
        } else { //是数值
          var arr = lrcs[i].match(/\[(\d+:.+?)\]/g);//提取时间字段，可能有多个
          var start = 0;
          for (var k in arr) {
            start += arr[k].length; //计算歌词位置
          }
          var content = lrcs[i].substring(start);//获取歌词内容
          for (var k in arr) {
            var t = arr[k].substring(1, arr[k].length - 1);//取[]间的内容
            var s = t.split(":");//分离:前后文字
            if (content !== '')
              this.oLRC.ms.push({//对象{t:时间,c:歌词}加入ms数组
                t: (parseFloat(s[0]) * 60 + parseFloat(s[1])).toFixed(3),
                c: content
              });
          }
        }
      }
      this.oLRC.ms.sort(function (a, b) {//按时间顺序排序
        return a.t - b.t;
      });

      // for(var i in this.oLRC){ //查看解析结果
      //     //console.log(i,":",this.oLRC[i]);
      // }
      if (this.oLRC.ti === store.state.globalLyricSets.ti && this.oLRC.ar === store.state.globalLyricSets.ar && this.oLRC.al === store.state.globalLyricSets.al) {
        return;
      }
      store.commit('CHANGENOWPLAYINGLYRICSETS', this.oLRC);
    },

    deleteSongInList(music_to_delete) {
      store.state.nowPlayingMusicSet.removeMusic(music_to_delete);
    },
    setDefaultPlayer() {
      this.play = false;
      store.commit('CHANGENOWPLAYINGMUSIC', null);
      // store.state.nowPlayMusic = null;
      this.box.src = null;
      this.playCoverSource = this.playCoverSource_empty;
      this.has_lyric = false;
      store.commit('CHANGENOWPLAYINGLYRIC', "丘丘音乐，听我想听");
      this.duration = "--:--"; // 音乐总时长
      this.currentTime = "--:--"; // 当前播放时长
      this.scroll_height = 0;
      this.scroll_top = 0;
      this.scroll_able = true;
      this.currentIndex = 0;
      this.in_lovelist = true; //当前播放歌曲是否在当前用户的喜爱列表
      this.song_name = "Olah! 欢迎来到丘丘音乐";
      this.song_singer = "飞翔的丘丘人";
    },
    playMusic() {
      if (store.state.nowPlayingMusicSet.isEmptyMusicSet()) {
        this.setDefaultPlayer();
        return;
      }
      this.play = true;
      this.box.play();
    },
    pauseMusic() {
      if (store.state.nowPlayingMusicSet.isEmptyMusicSet()) {
        this.setDefaultPlayer();
        return;
      }
      this.play = !this.play;
      if (this.play) {
        playAudio();
      } else {
        pauseAudio();
      }
    },
    playNextMusic() { //播放器进行到结尾播放下一首
      let temp;
      //console.log("play sequence",this.play_sequence);
      if (store.state.nowPlayingMusicSet.isEmptyMusicSet()) {
        this.setDefaultPlayer();
        return;
      }
      if (this.play_sequence === 0) { //顺序播放
        //console.log('我在这里执行playNextMusic!!!!!');
        temp = store.state.nowPlayingMusicSet.getNextMusic();
        //console.log('IN PLAY NEXT MUSIC:',temp);
        this.playAudio1(temp);
      }
      else if (this.play_sequence === 1) { //单曲循环
        if (store.state.nowPlayingMusicSet.indexOfMusic(store.state.nowPlayMusic) >= 0)
          this.playAudio1(store.state.nowPlayMusic);
        else
          this.setDefaultPlayer();
      }
      else { //随机播放
        temp = store.state.nowPlayingMusicSet.getRandomMusic();
        this.playAudio1(temp);
      }
    },
    playNextMusic2() { //播放按钮
      let temp;
      //console.log("play sequence2",this.play_sequence);
      if (store.state.nowPlayingMusicSet.isEmptyMusicSet()) {
        this.setDefaultPlayer();
        return;
      }
      if (this.play_sequence === 2) { //随机播放则随机播放
        temp = store.state.nowPlayingMusicSet.getRandomMusic();
        this.playAudio1(temp);
      }
      else { // 顺序播放和单曲循环则顺序播放
        temp = store.state.nowPlayingMusicSet.getNextMusic();
        this.playAudio1(temp);
      }
    },
    playLastMusic() {
      if (store.state.nowPlayingMusicSet.isEmptyMusicSet()) {
        this.setDefaultPlayer();
        return;
      }
      var temp = store.state.nowPlayingMusicSet.getLastMusic();
      this.playAudio1(temp);
    },
    async playAudio3(to_play_list) {
      //console.log("PLAY AUDIO3",to_play_list);
      let temp1;
      // console.log("PLAY AUDIO3:LENGTH",to_play_list.length);
      if (to_play_list.length > 0) {
        // console.log("PLAY AUDIO3:0",to_play_list[0]);
        temp1 = await store.state.nowPlayingMusicSet.removeMusicAll();
        // await this.playAudio1(to_play_list[0]);
        // console.log("PLAY AUDIO3:1",to_play_list[0]);
      }
      else {
        // this.setDefaultPlayer();
        return;
      }
      for (var item in to_play_list) {
        let temp2 = await store.state.nowPlayingMusicSet.addMusic(to_play_list[item]);
        // console.log("PLAY AUDIO3:x",temp2);
      }
      await this.playAudio1(to_play_list[0]);
    },
    async playAudio1(music) {
      let temp2 = await store.state.nowPlayingMusicSet.addMusic(music);
      store.commit('CHANGENOWPLAYINGMUSIC', temp2);
      // this.nowPlayingMusic = store.state.nowPlayMusic;
      // this.nowPlayingMusic = temp2;
      this.song_name = temp2.name;
      this.song_singer = temp2.author;
      this.has_lyric = temp2.hasLyrics;
      this.box.src = temp2.musicPath;
      this.has_lyric = temp2.hasLyrics;
      this.in_lovelist = temp2.isInLovelist;
      this.playCoverSource = temp2.coverPath;
      this.lyricFilePath = temp2.lyricPath;
      const total1 = this.formatTime(this.box.duration)
      const current1 = this.formatTime(this.box.currentTime)
      this.duration = `${total1.min}:${total1.sec}`
      this.currentTime = `${current1.min}:${current1.sec}`
      // console.log('duration in p1',this.duration)
      this.song_name = temp2.name;
      this.song_singer = temp2.author;
      // console.log('song_name in p1',this.song_name);
      this.sliderVal = Math.floor(this.box.currentTime);
      this.sliderMax = Math.floor(this.box.duration);
      // console.log('sliderMax in p1',this.sliderMax);
      if (this.has_lyric) {
        await this.getLRC(temp2);
      }
      let temp4 = await checkSong(temp2.id)
      var m;
      if (temp4.result == 'False')
        m = false;
      else
        m = true;
      this.in_lovelist = m;
      //console.log('TEMP4',temp4);
      store.state.nowPlayingMusicSet.changeLoveStatus(store.state.nowPlayMusic, m);
      await addPlayed(temp2.id);
      await addHistory(temp2.id);
      //console.log("in addHistory:",temp2.id);
      this.playMusic();
      this.init();
    },
    changeMouseOver(id) {
      // var newid = "#" + id;
      // var element = document.querySelector(newid);
      // if (element.href != window.location) {
      //     element.style.color = this.getColor;
      // }
    },
    changeMouseOut(id) {
      // var newid = "#" + id;
      // var element = document.querySelector(newid);
      // if (element.href != window.location) {
      //     element.style.color = 'black';
      // }
    },
    clickRouter(id) {
      var routerid = "#" + id;
      var elementRouter = document.querySelector(routerid);
      var spanid = "#" + id + "Span";
      var elementSpan = document.querySelector(spanid);
      var list = document.getElementsByClassName('router');
      for (var i = 0; i < list.length; i++)
        list[i].style.color = 'black';
      list = document.getElementsByClassName('rountSpan');
      for (var i = 0; i < list.length; i++)
        list[i].style.backgroundColor = 'white';
      elementRouter.style.color = 'white';
      elementSpan.style.backgroundColor = this.getColor;
      if (id == 'router2' && store.state.loginUser != null) {
        store.commit('updateVisitUser', store.state.loginUser);
        //console.log(store.state.loginUser)
      }
      if (id != 'router1' && !store.state.globalLogin) {
        ElMessage({
          message: '请先登录',
          type: 'warning',
        });
      }
    },
    overOtherChangeColor(id, color) {
      var routerid = "#" + id;
      var element = document.querySelector(routerid);
      element.style.color = color;
    },
    outOtherChangeColor(id) {
      var routerid = "#" + id;
      var element = document.querySelector(routerid);
      element.style.color = 'black';
    },
    init() {
      if (this.box == null) {
        this.box = audioElement;
      }
      if (!store.state.nowPlayMusic) {
        return;
      }
      this.box.src = store.state.nowPlayMusic.musicPath;
      // this.box.src = require(`${this.list[this.index].url}`)
      //console.log(this.box, '音频播放器DOM')
      const that = this
      // this.in_lovelist = this.list[this.index].is_loved//todo:request in_love_info
      this.has_lyric = store.state.nowPlayMusic.hasLyrics;
      this.in_lovelist = store.state.nowPlayMusic.isInLovelist;//todo request in_lovelist
      // this.playCoverSource = this.list[this.index].playCoverPath //todo:request playcover_source
      //   this.playCoverSource = require("../../public/img/pic1.jpg")
      this.playCoverSource = store.state.nowPlayMusic.coverPath;
      this.lyricFilePath = store.state.nowPlayMusic.lyricPath;
      // let imgurl;
      // imgurl = this.list[this.index].playCoverPath.split('../../public/img/')[1]
      // this.playCoverSource = require('../../public/img/' + imgurl)//todo:从后端获取图片也是如此吗
      const total1 = this.formatTime(this.box.duration)
      const current1 = this.formatTime(this.box.currentTime)
      this.duration = `${total1.min}:${total1.sec}`
      this.currentTime = `${current1.min}:${current1.sec}`
      //console.log('duration in this.init()',this.duration)
      // this.playCoverSource = require(`${this.list[this.index].playCoverPath}`)
      this.song_name = store.state.nowPlayMusic.name;
      this.song_singer = store.state.nowPlayMusic.author;
      //console.log('song_name in this.init():',this.song_name);
      this.sliderVal = Math.floor(this.box.currentTime);
      this.sliderMax = Math.floor(this.box.duration);
      //console.log('sliderMax in this.init():',this.sliderMax);
      this.playMusic();
      // 下面的是实时监听函数，就是{}里面this的含义变了，所以用一个常量that代替this
      this.box.ondurationchange = function () {
        //console.log('时长发生了变化')
        //console.log(that.box.duration)
        that.sliderMax = Math.floor(that.box.duration)
        that.updateTime()
      }
      // 当前数据可用时触发
      this.box.oncanplay = function () {
        //console.log('已经可以播放了')
      }
      // 播放位置发送改变时触发。
      this.box.ontimeupdate = function () {
        //这种用法在doSomething处使用this的话，指向的是匿名函数//3000表示睡眠3s后执行doSomething
        // setTimeout(function(){
        //doSomething(这里写时间到之后需要去做的事情)
        //console.log('播放位置发送了变动')
        that.updateTime();
        // }, 100);
      }
      // 音频播放完毕
      this.box.onended = function () {
        //console.log('播放完毕，谢谢收听')
        that.playNextMusic() //播放完毕自动播放下一首
      }
      // 音频播放错误
      this.box.onerror = function () {
        //console.log('加载出错！')
      }
    },
    spliderSelect() {
      // 滑块松动后触发。更新当前时长，
      // 时长发生变动会init里的方法进行更新数据
      this.copySliderVal = this.sliderVal
      this.box.currentTime = this.copySliderVal
      // }
    },
    changeVolumes() {
      // 静音切换
      if (this.sliderValVolume > 0) {
        this.sliderValVolume = 0
      } else {
        this.sliderValVolume = this.copySliderValVolume
      }
      this.box.volume = this.sliderValVolume
    },
    async changeLovelist() {
      if (this.in_lovelist) {
        this.in_lovelist = !this.in_lovelist;
        store.state.nowPlayingMusicSet.changeLoveStatus(store.state.nowPlayMusic, this.in_lovelist);
        await deleteSong(store.state.nowPlayMusic.id);
      } else {
        this.in_lovelist = !this.in_lovelist;
        store.state.nowPlayingMusicSet.changeLoveStatus(store.state.nowPlayMusic, this.in_lovelist);
        await addSong(store.state.nowPlayMusic.id);
      }
      // store.state.nowPlayingMusicSet.changeLoveStatus(store.state.nowPlayMusic, this.in_lovelist);
    },
    formatTooltip(val) {
      // 格式化毫秒数，由于组件提示为纯数字，所以这里需要将数字转化为我们所需要的格式，string类型的。'03:45',
      const time = this.formatTime(val)
      return `${time.min}:${time.sec}⚪`
    },
    // 音量显示100%
    formatTooltipVolume(val) {
      return val * 100 + '%'
    },
    spliderSelectVolume() {
      this.box.volume = this.sliderValVolume
      // 备份音量
      this.copySliderValVolume = this.sliderValVolume
    },
    updateTime() {
      const total = this.formatTime(this.box.duration)
      const current = this.formatTime(this.box.currentTime)
      this.duration = `${total.min}:${total.sec}`
      this.currentTime = `${current.min}:${current.sec}`
      // //console.log('duration in updateTime():',this.duration)
      // //console.log('currentTime in updateTime()',this.currentTime)
      // 值为xx.xxxxx 需要取整
      this.sliderVal = Math.floor(this.box.currentTime)
      // //console.log('song_name in updateTime():',this.song_name)
    },
    formatTime(time) {
      // 格式化毫秒，返回String型分秒对象
      if (!time) return { min: '00', sec: '00' }
      return {
        min: Math.floor(time / 60)
          .toString()
          .padStart(2, '0'),
        sec: Math.floor(time % 60)
          .toString()
          .padStart(2, '0')
      }
    },
    toInfoPage() {
      //console.log("in toinfo",store.state.nowPlayingMusicSet);
      this.show_play_page = !this.show_play_page;
      this.scroll_able = true;
    },
    toMusicPage() {
      // if (this.$route.path === '/music/'+store.state.nowPlayMusic.id)
      //console.log(this.$route.path);
      if (store.state.nowPlayMusic) {
        if (this.$route.path === '/music/' + store.state.nowPlayMusic.id) {
          this.toInfoPage();
          return;
        }
        this.$router.push('/');
        // setTimeout(this.toMusicPageAdd(),1000);
        setTimeout(this.toMusicPageAdd(), 1000);
      }
      else
        this.toInfoPage();
    },
    toMusicPageAdd() {
      this.$router.push('/music/' + store.state.nowPlayMusic.id);
      this.show_play_page = false;
      this.scroll_able = true;
    }
    // closeAudioPlay () {
    //   // eslint-disable-next-line vue/no-mutating-props
    //   this.isShowAudioPlayer = false
    // }
  },
  computed: {
    store() {
      return store
    },
    Delete() {
      return Delete
    },
    getColor() {
      return getComputedStyle(document.documentElement).getPropertyValue('--main-color');
    },
    // ...mapState({
    //   nowPlayingMusic: state => state.nowPlayMusic,
    // }),
    nowLoginUser() {
      return store.state.loginUser;
    },
    userRouter() {
      return '/user/Logined/' + nowLoginUser();
    }
  },
}
</script>
