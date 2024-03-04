import { ref } from 'vue';
import { getUserInformation } from "../api/User";
import { getUserLikeList } from "../api/User";
import { getAttentionUser } from "../api/User"
import { getUploadList } from "../api/User"
import { getUserShareList } from "../api/User"
import Music from '../components/music'
export default class User {
  constructor(id) {
    this.id = id;
    this.name = '';
    this.introduction = null;
    this.hasIcon = null;
    this.icon = null;
    this.likeList = []; // 使用 ref 创建响应式数组
    this.recentPlayList = []; // 使用 ref 创建响应式数组
    this.recentPlayMax = 0;
    this.attentionUser = []; // 使用 ref 创建响应式数组
    this.songList = []; // 使用 ref 创建响应式数组
    this.uploadList = [];
    this.shareSongList = [];
    this.isAdmin = false;
  }

  async initializeUserInfo(userId) {
    try {
      const attentionUser = await getAttentionUser(userId);
      const userInformation = await getUserInformation(userId);
      const userLikeList = await getUserLikeList(userId);
      const uploadList = await getUploadList(userId);
      const shareList = await getUserShareList(userId);
      await this.processUserInfo(userInformation, userLikeList,attentionUser,uploadList,shareList);
    } catch (error) {
      console.error("Failed to fetch user information:", error);
    }
  }

  async processUserInfo(userInformation, userLikeList,attentionUser,uploadList,shareList) {
    this.name = userInformation.username;
    this.introduction = userInformation.introduction;
    this.hasIcon = userInformation.has_icon;
    this.icon = 'https://' + userInformation.icon_address;
    this.isAdmin = userInformation.is_admin;
    this.recentPlayMax=userInformation.recent_played_max;
    for (let i = 0; i < userLikeList.length; i++) {
      const musicId = userLikeList[i].song_id;
      const newMusic = new Music(musicId);
      await newMusic.initializeMusicInfo(musicId);
      this.likeList.push(newMusic);
    }
    for(let i = 0;i < attentionUser.length;i++){
      const person = {
        id: attentionUser[i].uid,
        name : attentionUser[i].username,
        introduction : attentionUser[i].introduction,
        has_icon : attentionUser[i].has_icon,
        icon : 'https://' + attentionUser[i].icon_address,
      };
      this.attentionUser.push(person);
    }
    for(let i = 0;i < uploadList.length;i++)
    {
      const music = new Music(uploadList[i].song_id);
      music.initForSongList(uploadList[i]);
      this.uploadList.push(music);
    }
    for(let i = 0;i < shareList.length;i++)
    {
      const temp = {
        id : shareList[i].list_id,
        title : shareList[i].title,
        cover : 'https://' + shareList[i].cover_address,
      }
      this.shareSongList.push((temp));
    }
  }
}