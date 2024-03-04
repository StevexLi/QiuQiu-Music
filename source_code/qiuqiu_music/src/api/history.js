import store from "@/store";
import { post, get } from "./api";

export async function getHistory(){
    return await get('/api/history/get/?user_id='+store.state.globalUserID);
}

export async function addHistory(musicID){
    var newdata=new FormData();
    if(store.state.globalLogin==true){
        newdata.append('user_id',store.state.globalUserID);
        newdata.append('song_id',musicID);
        return await post('/api/history/add/',newdata);
    }
}