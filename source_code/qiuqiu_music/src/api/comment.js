import store from "@/store";
import { post, get } from "./api";
export async function getComment(musicId) {
  try {
    const response = await get("/api/comment/get_info/?song_id=" + musicId);
    const data = response.data;
    if (response.code !== "0") {
      throw new Error("Failed to fetch comment information");
    }
    return data;
  } catch (error) {
    console.error("Failed to fetch comment information:", error);
    throw error;
  }
}
export async function addComment(userId, musicId, content1) {

  var newdata = new FormData();
  newdata.append("user_id", userId);
  newdata.append("song_id", musicId);
  newdata.append("content", content1);
  var response = await post("/api/comment/add/", newdata);
  //console.log(response);
  
}
export async function removeComment(userId, commentId) {
  var newdata = new FormData();
  newdata.append("operator_id", userId);
  newdata.append("comment_id", commentId);
  var response = await post("/api/comment/delete/", newdata);
  //console.log(response);
}
