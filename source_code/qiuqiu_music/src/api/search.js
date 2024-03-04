import store from "@/store";
import { post, get } from "./api";

export async function searchSong(keywords,pageNum){
    return await get('/api/search/song_name/?keywords='+keywords+'&page_num='+pageNum);
}

export async function searchSongList(keywords,pageNum){
    return await get('/api/search/list_name/?keywords='+keywords+'&page_num='+pageNum);
}
export async function getTagSongList(tag,pageNum){
    var response = await get('/api/search/list_tag/?tag='+tag + '&page_num=' + pageNum);
    return response
}
export async function getTagSong(tag,pageNum){
    var response = await get('/api/search/song_tag/?tag='+tag + '&page_num=' + pageNum);
    return response
}