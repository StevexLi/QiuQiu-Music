import store from "@/store";
import { post, get } from "./api";

export async function upLoadSong(title,singer,introduction,local_file,lyric,cover,tag){
    var newdata=new FormData();
    newdata.append('title',title);
    newdata.append('singer',singer);
    newdata.append('introduction',introduction);
    newdata.append('local_file',local_file);
    newdata.append('uploader_id',store.state.globalUserID);
    newdata.append('lyric',lyric);
    newdata.append('cover',cover);
    newdata.append('tag1',tag[0]);
    newdata.append('tag2',tag[1]);
    newdata.append('tag3',tag[2]);
    newdata.append('tag4',tag[3]);
    newdata.append('tag5',tag[4]);
    newdata.append('tag6',tag[5]);
    return await post('/api/song/upload/',newdata);
}
