import store from "@/store";
import { post, get } from "./api";

export async function createSongList(title,introduction,cover,tag){
    var newdata=new FormData();
    newdata.append('user_id',store.state.globalUserID);
    newdata.append('title',title);
    newdata.append('introduction',introduction);
    newdata.append('cover',cover);
    newdata.append('tag1',tag[0]);
    newdata.append('tag2',tag[1]);
    newdata.append('tag3',tag[2]);
    newdata.append('tag4',tag[3]);
    newdata.append('tag5',tag[4]);
    newdata.append('tag6',tag[5]);
    return await post('/api/songlist/create/',newdata);
}

export async function changeShare(songListID){
    if(songListID!=0){
        var newdata=new FormData();
        newdata.append('operator_id',store.state.globalUserID);
        newdata.append('list_id',songListID);
        return await post('/api/songlist/share/',newdata);
    }
}

export async function addSong(songListID,songID){
    var newdata=new FormData();
    newdata.append('list_id',songListID);
    newdata.append('user_id',store.state.globalUserID);
    newdata.append('song_id',songID);
    return await post('/api/songlist/add/',newdata);
}
export async function addSongToList(songListID,songID){
    var newdata=new FormData();
    newdata.append('list_id',songListID);
    newdata.append('user_id',store.state.globalUserID);
    newdata.append('song_id',songID);
    return await post('/api/songlist/add/',newdata);
}

export async function updateSongList(songListID,title,introduction,cover,tag){
    var newdata=new FormData();
    newdata.append('operator_id',store.state.globalUserID);
    newdata.append('list_id',songListID);
    newdata.append('title',title);
    newdata.append('introduction',introduction);
    newdata.append('cover',cover);
    newdata.append('tag1',tag[0]);
    newdata.append('tag2',tag[1]);
    newdata.append('tag3',tag[2]);
    newdata.append('tag4',tag[3]);
    newdata.append('tag5',tag[4]);
    newdata.append('tag6',tag[5]);
    return await post('/api/songlist/update/',newdata);
}

export async function deleteSongList(songListID){
    var newdata=new FormData();
    newdata.append('operator_id',store.state.globalUserID);
    newdata.append('list_id',songListID);
    return await post('/api/songlist/delete/',newdata);
}

export async function getSongList(songListID){
    return await get('/api/songlist/get/?list_id='+songListID);
}

export async function removeSong(songID,songListID){
    var newdata=new FormData();
    newdata.append('song_id',songID);
    newdata.append('operator_id',store.state.globalUserID);
    newdata.append('list_id',songListID);
    return await post('/api/songlist/remove/',newdata);
}