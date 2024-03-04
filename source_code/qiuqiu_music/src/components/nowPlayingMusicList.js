export default class NowPlayMusicList {
  constructor() {
    this.list = [];
    this.index = 0;
  }
  isEmptyMusicSet() {
    return this.list.length === 0;
  }
  addMusic(Music) {
    let item;
    let can_add_music = true;
    for (item in this.list) {
      if (this.list[item].id === Music.id){
        can_add_music=false;
        this.index = item;
      }
    }
    // if (!this.list.includes(Music))
    //     this.list.push(Music);
    if (can_add_music) {
      this.list.push(Music);
      this.index = this.list.indexOf(Music);
    }
    return this.list[this.index];
  }
  removeMusic(Music) {
    var index = this.list.indexOf(Music);
    this.list.splice(index, 1);
  }
  async removeMusicAll() {
    let listlength = this.list.length;
    this.list.splice(0, listlength);
    return 0;
  }
  getNextMusic() {
    this.index++;
    if (this.index >= this.list.length) this.index = 0;
    return this.list[this.index];
  }

  getRandomMusic() {
    this.index = Math.floor(Math.random()*this.list.length);
    if (this.index >= this.list.length) this.index = 0;
    return this.list[this.index];
  }
  getLastMusic() {
    this.index--;
    if(this.index <= -1) this.index = this.list.length - 1;
    return this.list[this.index];
  }
  changeLoveStatus(Music, in_lovelist) {
    if (!this.list.includes(Music))
      return;
    this.list[this.list.indexOf(Music)].isInLovelist = in_lovelist;
  }
  indexOfMusic(Music) {
    let item;
    for (item in this.list) {
      if (this.list[item].id === Music.id) {
        return item;
      }
    }
    return -1;
  }
}
