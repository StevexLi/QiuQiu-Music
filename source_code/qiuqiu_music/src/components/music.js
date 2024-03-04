import { checkSong } from '@/api/likeList';
import { getMusicInfo } from '../api/music';
import { ref } from 'vue';
export default class Music {
  constructor(id) {
    this.id = id;
    this.name = null;
    this.author = null;
    this.coverPath = null;
    this.musicPath = null;
    this.duration = "00:00";
    this.lyrics = null;
    this.lyricPath = null;
    this.tag1 = null;
    this.tag2 = null;
    this.tag3 = null;
    this.tag4 = null;
    this.tag5 = null;
    this.tag6 = null;
    this.isInLovelist = false;
    this.hasLyrics = false;
    this.uploaderId = null;
    this.played = 0;
    this.lyricCode = 'GBK';
  }
  initForSongList(musicInformation){
    this.id = musicInformation.song_id;
    this.name = musicInformation.title;
    this.introduction = musicInformation.introduction;
    this.coverPath = 'https://' + musicInformation.cover_address;
    this.hasLyrics = musicInformation.has_lyric;
    if (this.hasLyrics) {
      this.lyrics = 'https://' + musicInformation.lyric_address;
      this.lyricPath = 'https://' + musicInformation.lyric_address;
      this.lyricCode = musicInformation.lyric_code;
    }
    this.author = musicInformation.singer;
    this.uploaderId = musicInformation.uploader_id;
    this.tag1 = musicInformation.tag1;
    this.tag2 = musicInformation.tag2;
    this.tag3 = musicInformation.tag3;
    this.tag4 = musicInformation.tag4;
    this.tag5 = musicInformation.tag5;
    this.tag6 = musicInformation.tag6;
    this.musicPath = 'https://' + musicInformation.song_address;
    this.played = musicInformation.played;
  }
  async initializeMusicInfo(musicID) {
    try {
      const musicInformation = await getMusicInfo(musicID);
      this.processMusicInfo(musicInformation);
      this.isInLovelist = await checkSong(musicID);
    } catch (error) {
      console.error("Failed to fetch user information:", error);
    }
  }
  processMusicInfo(musicInformation) {
    this.name = musicInformation.info.title;
    this.introduction = musicInformation.info.introduction;
    this.coverPath = 'https://' + musicInformation.info.cover_address;
    this.hasLyrics = musicInformation.info.has_lyric;
    if (this.hasLyrics) {
      this.lyrics = 'https://' + musicInformation.info.lyric_address;
      this.lyricPath = 'https://' + musicInformation.info.lyric_address;
      this.lyricCode = musicInformation.info.lyric_code;
    }
    this.author = musicInformation.info.singer;
    this.uploaderId = musicInformation.info.uploader_id;
    this.tag1 = musicInformation.info.tag1;
    this.tag2 = musicInformation.info.tag2;
    this.tag3 = musicInformation.info.tag3;
    this.tag4 = musicInformation.info.tag4;
    this.tag5 = musicInformation.info.tag5;
    this.tag6 = musicInformation.info.tag6;
    this.musicPath = 'https://' + musicInformation.info.song_address;
    this.played = musicInformation.info.played;
  }
}
