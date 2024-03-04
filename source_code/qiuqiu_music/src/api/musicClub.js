import store from "@/store";
import { post, get } from "./api";
export async function getTagSongList(tag){
    var response = await get('/api/search/list_tag/?tag='+tag + '&page_num=' + 1);
    return response
}
export async function getTagSong(tag){
    var response = await get('/api/search/song_tag/?tag='+tag + '&page_num=' + 1);
    return response
}
export async function getTagSongtRandom(type){
    var response = await get('/api/search/random/?num='+10 + '&type=' + type);
    return response
}
