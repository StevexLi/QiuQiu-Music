import store from "@/store";
import { post, get } from "./api";

export async function getComplain(){
    return await get('/api/complain/get/');
}

export async function setComplain(id,type,content){
    var newdata=new FormData();
    newdata.append('user_id',store.state.globalUserID);
    newdata.append('obj_id',id);
    newdata.append('type',type);
    newdata.append('content',content);
    return await post('/api/complain/create/',newdata);
}

export async function executeComplain(result,complainID,message){
    var newdata=new FormData();
    newdata.append('result',result);
    newdata.append('complain_id',complainID);
    newdata.append('extra_msg',message);
    return await post('/api/complain/execute/',newdata);
}