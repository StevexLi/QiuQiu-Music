<template>
  <div class="audio-player">
    <!-- :src="require(`${list[index].url}`) closeIcon -->
    <audio controls ref="audio-player" v-show="false"></audio>
      <transition name="play_pause" mode="out-in">
      <img alt="" :src="playCoverSource" class="nowPlayingMusicCover_player">
      </transition>
    <div class="audio-mock-player">
<!--      <img :src="app.nowPlayingMusic.coverPath" class="nowPlayingMusicCover">-->
<!--      <img :src="closeIcon" class="closeicon" @click="closeAudioPlay" v-show="false"/>-->
      <!-- 上一首 -->
      <el-icon class="preicon" @click="musicPlay('pre')" color="#ffffff" size="200%">
        <ArrowLeftBold />
      </el-icon>
<!--      <img-->
<!--        @click="musicPlay('pre')"-->
<!--        src="../assets/play_previous.png"-->
<!--        class="preicon"-->
<!--      />-->
      <!-- "暂停" : "播放" -->
      <el-icon class="play-sty"  @click="musicPlay('play')" color="#ffffff" size="300%">
        <transition name="play_pause" mode="out-in">
        <CaretRight v-if="!play"/>
        <VideoPause v-else />
        </transition>
      </el-icon>
<!--      <img-->
<!--        @click="musicPlay('play')"-->
<!--        class="play-sty"-->
<!--        :src="play ? pauseIcon : playIcon"-->
<!--      />-->
      <!-- 下一首 -->
      <el-icon class="preicon" @click="musicPlay('next')" color="#ffffff" size="200%">
        <ArrowRightBold />
      </el-icon>

<!--       <img @click="musicPlay('next')" src="../assets/play_next.png" class="preicon" /> -->

      <div class="right-menu">
        <div class="song_and_singer_name">
            <span class="song_name">{{ list[index].name }}</span>
            <span class="singer_name">- {{ list[index].singer }}</span>
            <span class="duration_upward">/{{ duration }}</span>
            <span class="current_upward">{{ currentTime }}</span>
        </div>
        <div class="bottom">
          <!--  播放进度条 -->
          <el-slider
            class="progress"
            v-model="sliderVal"
            :format-tooltip="formatTooltip"
            :tooltip-class="defaultTooltip"
            :show-tooltip="true"
            :min="sliderMin"
            :max="sliderMax"
            @input="spliderSelect"
            ref="slider1"
          />
<!--                        @change="spliderSelect"-->

<!--          <span class="current">{{ currentTime }}</span>-->
<!--          <span class="duration">/{{ duration }}</span>-->
        </div>
      </div>
        <div class="volume">
            <!-- <img :src="require('../assets/volume.png')" alt=""/> -->
            <!-- 有时候我们在对于一些hover定位元素，当离开时候就没了，这个时候可以使用ctrl+shift+c的快捷键来获取。 -->
            <el-popover
                    placement="top-start"
                    trigger="hover"
                    popper-class="poppervolume-class"
                    width = 50px
                    show-after = "200"
                    hide-after = "400"
            >
                <el-slider
                        class="volume-progress"
                        vertical
                        height="100px"
                        :step="0.1"
                        v-model="sliderValVolume"
                        :format-tooltip="formatTooltipVolume"
                        :min="0"
                        :max="1"
                        @input="spliderSelectVolume"
                />
                <template v-slot:reference>
                    <transition name="play_pause" mode="out-in">
                        <img
                                @click="changeVolumes"
                                :src="volumeIcon"
                                alt=""
                                v-if="sliderValVolume"
                        />
                        <img
                                @click="changeVolumes"
                                :src="mutedIcon"
                                alt=""
                                v-else
                        />
                    </transition>
                </template>
            </el-popover>
        </div>
        <div class="volume">
            <!-- <img :src="require('../assets/volume.png')" alt=""/> -->
            <!-- 有时候我们在对于一些hover定位元素，当离开时候就没了，这个时候可以使用ctrl+shift+c的快捷键来获取。 -->
<!--                <template v-slot:reference>-->
                    <transition name="play_pause" mode="out-in">
                        <img
                                @click="changeLovelist"
                                :src="in_love_listIcon"
                                alt=""
                                v-if="in_lovelist"
                        />
                        <img
                                @click="changeLovelist"
                                :src="not_in_love_listIcon"
                                alt=""
                                v-else
                        />
                    </transition>
<!--                </template>-->
        </div>
        <div class="volume moreicon">
            <!-- <img :src="require('../assets/volume.png')" alt=""/> -->
            <!-- 有时候我们在对于一些hover定位元素，当离开时候就没了，这个时候可以使用ctrl+shift+c的快捷键来获取。 -->
            <!--                <template v-slot:reference>-->
                <el-icon color="white" size="32" @click="toInfoPage"><MoreFilled /></el-icon>
            <!--                </template>-->
        </div>
    </div>
  </div>
</template>

<script>
import { ArrowLeftBold, ArrowRightBold, CaretRight, VideoPause, MoreFilled} from '@element-plus/icons-vue'

export default {
  name: 'MusicPlayer',
  components: { VideoPause, ArrowRightBold, CaretRight, ArrowLeftBold, MoreFilled},
    expose:{
      musicPlay(flag) {
      }
    },
  props: {
    // 显示隐藏
    isShowAudioPlayer: {
      default: true
    },
    // 播放列表
    list: {
      default: function () {
        return [
          // 数据格式
          {
            id: 1,
            name: 'Always You',
            url: '../assets/1.mp3',
            cover: 'ChenYou',
            singer: 'milet',
            is_loved: true,
            playCoverPath: '../../public/img/pic1.jpg',
          },
          {
            id: 2,
            name: '起风了',
            url: '../assets/2.mp3',
            cover: 'ChenYou',
            singer: '林俊杰',
            is_loved: false,
            playCoverPath: '../../public/img/pic2.jpg',
          },
          {
              id: 3,
              name: '蒼穹のファンファーレ',
              url: '../assets/3.flac',
              cover: 'ChenYou',
              singer: 'FictionJunction feat.藍井エイル & ASCA & ReoNa',
              is_loved: false,
              playCoverPath: '../../public/img/pic3.jpg',
          }
        ]
      }
    }
    //  播放索引
    // index
  },
  data () {
    return {
      playIcon: require('../assets/play.png'),
      pauseIcon: require('../assets/pause.png'),
      volumeIcon: require('../assets/volume.png'),
      mutedIcon: require('../assets/muted.png'),
      closeIcon: require('../assets/close.png'),
      in_love_listIcon: require('../assets/is_in_lovelist.png'),
      not_in_love_listIcon: require('../assets/not_in_lovelist.png'),
      playCoverSource: undefined,
      box: undefined,
      index: 0, // 当前播放的音乐素质索引
      play: false, // 播放状态，true为正在播放
      sliderVal: 0, // 这个对接当前时长。
      copySliderVal: 0,
      sliderMin: 0,
      sliderMax: 0, // 这个对接总时长。
      sliderValVolume: 0.5, // 音量
      copySliderValVolume: 0.5,
      duration: undefined, // 音乐总时长
      currentTime: undefined, // 当前播放时长
      in_lovelist: false, //当前播放歌曲是否在当前用户的喜爱列表
    }
  },
  mounted () {
    this.init()
  },
  methods: {
    init () {
      this.box = this.$refs['audio-player']
        let musicurl;
      musicurl = this.list[this.index].url.split('../assets/')[1]
      this.box.src = require('../assets/'+musicurl)
      // this.box.src = require(`${this.list[this.index].url}`)
      //console.log(this.box, '音频播放器DOM')
      const that = this
      this.in_lovelist = this.list[this.index].is_loved//todo:request in_love_info
      // this.playCoverSource = this.list[this.index].playCoverPath //todo:request playcover_source
      //   this.playCoverSource = require("../../public/img/pic1.jpg")
        let imgurl;
      imgurl = this.list[this.index].playCoverPath.split('../../public/img/')[1]
        this.playCoverSource = require('../../public/img/' + imgurl)//todo:从后端获取图片也是如此吗
      // this.playCoverSource = require(`${this.list[this.index].playCoverPath}`)
      //  this.duration  =  this.formatTime(this.box.duration)
      // 绑定三个触发方法
      // 当时长有变化时触发，由"NaN"变为实际时长也算
      this.box.ondurationchange = function () {
        //console.log('时长发生了变化')
        //console.log(that.box.duration)
        // that.
        // that.duration  =  that.formatTime(that.box.duration)
        that.sliderMax = Math.floor(that.box.duration)
        that.updateTime()
      }
      // 当前数据可用是触发
      // this.box.oncanplay = function () {
      //   //console.log('已经可以播放了')
      // }
      // 播放位置发送改变时触发。
      this.box.ontimeupdate = function () {
        //这种用法在doSomething处使用this的话，指向的是匿名函数//3000表示睡眠3s后执行doSomething
        // setTimeout(function(){
            //doSomething(这里写时间到之后需要去做的事情)
            //console.log('播放位置发送了变动')
          that.updateTime()
        // }, 100);

      }
      // 音频播放完毕
      this.box.onended = function () {
        //console.log('播放完毕，谢谢收听')
        that.musicPlay('next') //播放完毕自动播放下一首
      }
      // 音频播放完毕
      this.box.onerror = function () {
        //console.log('加载出错！')
      }
    },
    spliderSelect () {
        // 滑块松动后触发。更新当前时长，
        // 时长发生变动会init里的方法进行更新数据
        this.copySliderVal = this.sliderVal
        this.box.currentTime = this.copySliderVal
        // }
    },
    changeVolumes () {
      // 静音切换
      if (this.sliderValVolume > 0) {
        this.sliderValVolume = 0
      } else {
        this.sliderValVolume = this.copySliderValVolume
      }
        this.box.volume = this.sliderValVolume
    },
    changeLovelist() {
        if (this.in_lovelist) {
            this.in_lovelist = !this.in_lovelist
        } else {
            this.in_lovelist = !this.in_lovelist
        }
        this.list[this.index].is_loved = this.in_lovelist
        //todo:contact 后端
    },
    // 播放
    musicPlay (flag) {
      switch (flag) {
        case 'pre':
          if (this.list[this.index - 1]) {
            this.box.src = this.list[this.index - 1].url
            this.index -= 1
          } else {
            this.box.src = this.list[this.list.length - 1].url
            this.index = this.list.length - 1
          }
          this.init()
          if (this.play) {
            this.box.play()
          } else {
            this.box.pause()
          }
          break
        case 'play':
          this.play = !this.play
          if (this.play) {
            this.box.play()
          } else {
            this.box.pause()
          }
          break
        case 'next':
          if (this.list[this.index + 1]) {
            this.box.src = this.list[this.index + 1].url
            this.index += 1
          } else {
            this.box.src = this.list[0].url
            this.index = 0
          }
          this.init()
          if (this.play) {
            this.box.play()
          } else {
            this.box.pause()
          }
          break
      }
    },
    formatTooltip (val) {
      // 格式化毫秒数，由于组件提示为纯数字，所以这里需要将数字转化为我们所需要的格式，string类型的。'03:45',
      const time = this.formatTime(val)
      return `${time.min}:${time.sec}⚪`
    },
    // 音量显示100%
    formatTooltipVolume (val) {
      return val * 100 + '%'
    },
    spliderSelectVolume () {
      this.box.volume = this.sliderValVolume
      // 备份音量
      this.copySliderValVolume = this.sliderValVolume
    },
    updateTime () {

      const total = this.formatTime(this.box.duration)
      const current = this.formatTime(this.box.currentTime)
      this.duration = `${total.min}:${total.sec}`
      this.currentTime = `${current.min}:${current.sec}`
      // 值为xx.xxxxx 需要取整
      this.sliderVal = Math.floor(this.box.currentTime)
    },
    formatTime (time) {
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
      toInfoPage () {
        //todo:跳转到播放界面
      }
    // closeAudioPlay () {
    //   // eslint-disable-next-line vue/no-mutating-props
    //   this.isShowAudioPlayer = false
    // }
  }
}
</script>

<!--<style lang="less">-->
<!--.defaultTooltip-class{-->
<!--  min-width: 200px;-->
<!--  width: 500px;-->
<!--}-->
<!--.tooltip-width {-->
<!--  width: 200px;-->
<!--  max-width: 500px;-->
<!--}-->
<!--</style>-->

<style  lang='scss'>
.defaultTooltip {
  min-width: 200px;
  width: 500px;
}
.poppervolume-class {
  min-width: 10px !important;
  padding: 12px 5px !important;
}
.audio-player {
  background: rgba(34, 34, 34, 0.85);
  display: flex;
  align-items: center;
  position: fixed;
  bottom: 0;
  height: 9%;
  width: 100%;
  box-shadow: 0px 0px 20px 5px rgba(34, 34, 34, 0.85);
  .audio-mock-player {
    //border: black 1px solid;
    position: relative;
    width: 90%;
    left: 3%;
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
        //.volume {
        //  position: relative;
        //  img {
        //    width: 100px;
        //    height: 100px;
        //  }
        //  .volume-progress {
        //    position: absolute;
        //    top: -730px;
        //    left: -120px;
        //  }
        //  transition: 0.2s;
        //}
        //.volume:hover {
        //  cursor: pointer;
        //  scale: 1.25;
        //  transition: 0.2s;
        //}
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
        transition: 0.1s;
      }
      .song_name:hover{
        cursor: pointer;
        border-bottom: white 1.5px solid;
        transition: 0.1s;
      }
      .singer_name {
        font-size: 16px;
        //margin-top: 10px;
        margin-right: 10px;
        transition: 0.1s;
      }
      .singer_name:hover{
        border-bottom: white 1.5px solid;
        transition: 0.1s;
      }
      .current_upward {
        margin-top: 11px;
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
      .duration_upward{
        margin-top: 11px;
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
  .nowPlayingMusicCover_player {
    //display: block;
    height: 80%;
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
    //border: black 1px solid;
    margin-right: 10px;
    img {
      width: 32px;
      height: 32px;
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
