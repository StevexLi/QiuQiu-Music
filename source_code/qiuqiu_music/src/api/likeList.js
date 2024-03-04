import store from "@/store";
import { post, get } from "./api";

export async function addSong(songID){
    if(store.state.globalLogin==true){
        var newdata=new FormData();
        newdata.append('user_id',store.state.globalUserID);
        newdata.append('song_id',songID);
        return await post('/api/songlist/like/add/',newdata);
    }
}

export async function deleteSong(songID){
    if(store.state.globalLogin==true){
        var newdata=new FormData();
        newdata.append('user_id',store.state.globalUserID);
        newdata.append('song_id',songID);
        return await post('/api/songlist/like/delete/',newdata);
    }
    
}

export async function getLikeList(){
    return await get('/api/songlist/like/get/?user_id='+store.state.globalUserID);
}

export async function checkSong(songID){
    if(store.state.globalLogin==true) 
        return await get('/api/songlist/like/check/?user_id='+store.state.globalUserID+'&song_id='+songID);
    else
        return false;
}