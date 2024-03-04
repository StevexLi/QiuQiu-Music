import { post, get } from "./api";
import store from "@/store";
export async function getMusicInfo(musicId) {
  try {
    const response = await get("/api/song/get_info/?song_id=" + musicId);
    if (response.code !== "0") {
      throw new Error("Failed to fetch user information");
    }
    return response;
  } catch (error) {
    console.error("Failed to fetch user information:", error);
    throw error;
  }
}
export async function favorMusic(uid,musicId) {
  try {
    var newdata = new FormData();
    newdata.append("user_id", uid);
    newdata.append("song_id", musicId);
    var response = await post("/api/songlist/like/add/", newdata);
    if (response.code !== "0") {
      throw new Error("Failed to fetch user information");
    }
    alert("添加成功")
    return response;
  } catch (error) {
    alert("已经收藏过这首歌曲")
    throw error;
  }
}
export async function removeFavorMusic(uid, musicId) {
  try {
    var newdata = new FormData();
    newdata.append("user_id", uid);
    newdata.append("song_id", musicId);
    var response = await post("/api/songlist/like/delete/", newdata);
    if (response.code !== "0") {
      throw new Error("Failed to fetch user information");
    }
    alert("删除成功");
    return response;
  } catch (error) {
    alert("删除失败");
    throw error;
  }
}
export async function updateMusic(musicId, name,coverFile,tag1,tag2,tag3,tag4,tag5) {
  var newdata = new FormData();
  newdata.append("operator_id", store.state.loginUser.id);
  newdata.append("song_id", musicId);
  newdata.append("title", name);
  newdata.append("cover", coverFile);
  newdata.append("tag1", tag1);
  newdata.append("tag2", tag2);
  newdata.append("tag3", tag3);
  newdata.append("tag4", tag4);
  newdata.append("tag5", tag5);
  var response = await post("/api/song/update/", newdata);
}
export async function deleteMusic(songID){
  var newdata=new FormData();
  newdata.append('operator_id',store.state.globalUserID);
  newdata.append('song_id',songID);
  return await post('/api/song/delete/',newdata);
}
export async function addPlayed(songID){
  var newdata=new FormData();
  newdata.append('song_id',songID);
  return await post('/api/song/played/',newdata);
}