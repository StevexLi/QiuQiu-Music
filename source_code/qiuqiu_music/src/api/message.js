import store from "@/store";
import { post, get } from "./api";

export async function createNotification(message){
    var newdata=new FormData();
    newdata.append('user_id',store.state.globalUserID);
    newdata.append('message',message);
    return await post('/api/notification/create/',newdata);
}
export async function getNotification(){
    return await get('/api/notification/get/?user_id='+store.state.globalUserID);
}