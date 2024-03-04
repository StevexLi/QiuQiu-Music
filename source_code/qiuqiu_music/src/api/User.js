import { post, get } from "./api";
import store from "@/store";
export async function sendVerCode(address) {
  var newdata = new FormData();
  newdata.append("");
  return await post("", "123", newdata);
}
export async function register(userName,password,repassword,address,verCode){
  var newdata = new FormData();
  newdata.append("username", userName);
  newdata.append("password_1", password);
  newdata.append("password_2", repassword);
  return await post("/api/user/register/", newdata);
}
export async function applyForLikeList(userid) {
  var newdata = new FormData();
  newdata.append("user_id", userid);
  return await post("/api/songlist/like/create/", newdata);
}
export async function login(username, password) {
  var newdata = new FormData();
  newdata.append("username", username);
  newdata.append("password", password);
  return await post("/api/user/login/", newdata);
}
export async function getUserLikeList(userId) {
  try {
    const response = await get("/api/songlist/like/get/?user_id=" + userId);
    const data = response.data;
    if (response.code !== "0") {
      throw new Error("Failed to fetch user information");
    }
    const dataContent = data.content;
    return dataContent;
  } catch (error) {
    console.error("Failed to fetch user information:", error);
    throw error;
  }
}

export async function getUserInformation(userId) {
  try {
    var response = await get("/api/user/get_info/?user_id=" + userId);
    const data = response.data;
    if (response.code !== "0") {
      throw new Error("Failed to fetch user information");
    }
    return data;
  } catch (error) {
    console.error("Failed to fetch user information:", error);
    throw error;
  }
}
export async function getAttentionUser(userId) {
  try {
    var response = await get("/api/describe/get/?user_id=" + userId);
    const data = response.data;
    if (response.code !== "0") {
      throw new Error("Failed to fetch user information");
    }
    return data;
  } catch (error) {
    console.error("Failed to fetch user information:", error);
    throw error;
  }
}
export async function postAttentionUser(userId,describer_id) {
  try {
    var newdata = new FormData();
    newdata.append("user_id", userId);
    newdata.append("describer_id", describer_id);
    var response = await post("/api/describe/add/", newdata);
    if (response.code != "0") {
      throw new Error("Failed to fetch user information");
    }
    return response;
  } catch (error) {
    console.error("Failed to fetch user information:", error);
    throw error;
  }
}
export async function removeAttentionUser(userId,describer_id) {
  try {
    var newdata = new FormData();
    newdata.append("user_id", userId);
    newdata.append("describer_id", describer_id);
    var response = await post("/api/describe/remove/", newdata);
    if (response.code !== "0") {
      throw new Error("Failed to fetch user information");
    }
    return response;
  } catch (error) {
    console.error("Failed to fetch user information:", error);
    throw error;
  }
}
export async function getUserAllSongList(){
  return await get('/api/user/get_list_a/?operator_id='+store.state.globalUserID);
}
export async function getUserAllSongList1() {
  try {
    var response = await get(
      "/api/user/get_list_a/?operator_id=" + store.state.loginUser.id
    );
    var data = response.data;
    return data;
  } catch {
    console.log("can't get songList");
  }
}
export async function getUploadList(userId) {
  try {
    var response = await get("/api/user/get_song/?user_id=" + userId);
    var data = response.data;
    return data;
  } catch {
    console.log("can't get uploadList");
  }
}
export async function getUserShareList(userId) {
  try {
    var response = await get("/api/user/get_list_s/?user_id=" + userId);
    var data = response.data;
    return data;
  } catch {
    console.log("can't get uploadList");
  }
}
export async function changeUsernfo(userId,username, userIntroduction, icon) {
  console.log(userIntroduction);
  var newdata = new FormData();
  newdata.append("user_id", userId);
  newdata.append("username", username);
  newdata.append("introduction", userIntroduction);
  newdata.append("icon",icon);
  var response = await post("/api/user/change_info/", newdata);
}
export async function updateUserInfo(userId,username, userIntroduction, icon,maxPlayed){
  var newdata = new FormData();
  newdata.append("user_id", userId);
  newdata.append("username", username);
  newdata.append("introduction", userIntroduction);
  newdata.append("icon",icon);
  newdata.append("recent_played_max",maxPlayed);
  return await post("/api/user/change_info/", newdata);
}