import store from "@/store";
import Music from './music';


export default class SongList{
    constructor(data,isLikeList) {
        this.creatorID=data.creator_id;
        this.total=data.total;
        this.cover="https://"+data.cover_address;
        this.musicList=[];
        for(var i=0;i<this.total;i++){
            var music=new Music(data.content.song_id)
            music.initForSongList(data.content[i]);
            this.musicList.push(music);
        }
        if(isLikeList==false){
            this.songListID=data.list_id;
            this.title=data.title;
            this.introduction=data.introduction;
            this.tag=new Array(data.tag1,data.tag2,data.tag3,data.tag4,data.tag5,data.tag6);
            this.shareable=data.sharable;
        }
        else{
            this.songListID=0;
            this.title='我喜欢';
            this.introduction=null;
            this.tag=new Array(null,null,null,null,null,null);
            this.shareable=false;
        }
    }
}

export function openSongList(songList){
    store.state.currentSongList=songList;
    this.router.push(path+'/:'+songList.songListID);
}