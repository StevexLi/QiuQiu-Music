<template>
    <div v-if="this.isInitialization" style="position: fixed; top: 0; min-width: 1200px;width: 100%;height: 100%;">
        <div v-loading="this.isInitialization" element-loading-text="正在加载..."  style="height: 100%;width: 100%;"></div>
    </div>
    <div v-else style="width: 100%;min-width: 1200px;">
        <el-row style="position: relative;margin-bottom: 35px;min-width: 1200px;height: 30px;">
            <div class="station"></div>
            <div class="lineDiv" style="width: 10%;">投诉人</div>
            <div class="lineDiv" style="width: 8%;">投诉类型</div>
            <div class="lineDiv" style="width: 12%;text-align: center;">投诉对象</div>
            <div class="lineDiv" style="width: 45%;">投诉内容</div>
            <div class="lineDiv" style="width: 5%;">处理</div>
            <div class="station"></div>
        </el-row>
        <el-row v-if="this.count==0" class="parent" style="margin-top: 25px;height: 30px;">
            <div class="station" style="height: 30px;"></div>
            <div class="lineDiv" style="width: 330px;font-size: 18px;">您已经处理完所有投诉啦，休息一下吧！</div>
            <img src="../assets/manage.png" />
        </el-row>
        <el-row v-for="(item,index) in this.listOfComplain" :key = index class="row">
            <div class="station"></div>
            <div v-if="(index%2==0)" class="lineDiv back" style="width: 10%;"><span class="body" @click="this.jumptoUser(item)">{{ item.complainerName }}</span></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 10%;"><span class="body" @click="this.jumptoUser(item)">{{ item.complainerName }}</span></div>
            <div v-if="(index%2==0)" class="lineDiv back" style="width: 8%;">{{ item.typeName }}</div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 8%;">{{ item.typeName }}</div>
            <div v-if="(index%2==0)" class="lineDiv back" style="width: 12%;">
                <el-avatar shape="square" :fit="conintain" :size="85" :src='item.cover' style="margin-top: 3px;" @click="this.jump(item)"></el-avatar>
            </div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 12%;">
                <el-avatar shape="square" :fit="conintain" :size="85" :src='item.cover' style="margin-top: 3px;" @click="this.jump(item)"></el-avatar>
            </div>
            <div v-if="(index%2==0)" class="lineDiv back" style="width: 45%;">
                <el-input type="textarea" disabled="false" v-model="item.content" :autosize="{ minRows: 4, maxRows: 4 }" class="body2"></el-input>
            </div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 45%;">
                <el-input type="textarea" disabled="false" v-model="item.content" :autosize="{ minRows: 4, maxRows: 4 }" class="body2"></el-input>
            </div>
            <div v-if="(index%2==0)" class="lineDiv back" style="width: 5%;">
                <el-button @click="this.execute(item)"><el-icon><Edit /></el-icon></el-button>
            </div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 5%;">
                <el-button @click="this.execute(item)"><el-icon><Edit /></el-icon></el-button>
            </div>
            <div class="station"></div>
        </el-row>
        <div class="parent" style="height: 150px;"></div>
    </div>
    <el-dialog v-model="this.dialogFormVisible" title="投诉处理">
        <el-form>
            <el-form-item label="处理意见">
                <el-input type="textarea" maxlength="128" show-word-limit="true" :autosize="{ minRows: 6, maxRows: 6 }" v-model="this.message" autocomplete="off"/>
            </el-form-item>
        </el-form>
            <el-button type="primary" @click="this.submit(true)" style="margin-right: 10px;">处理</el-button>
            <el-button type="error" @click="this.submit(false)" style="margin-right: 10px;">驳回</el-button>
    </el-dialog>
</template>

<style scoped>
.row{
    position: relative;
    min-width: 1200px;
    height: 93px;
}
.station{
    position: relative;
    width: 10%;
}
.lineDiv{
    position: relative;
    height: 93px;
    text-align: center;
    line-height: 93px;
}
.back{
    background-color:#e1e3e3;
}
.body{
    font-size: 14px;
}
.body:hover{
    color: #42b983;
}
</style>

<script>
import store from '@/store';
import { Edit } from '@element-plus/icons';
import { getComplain, executeComplain } from '@/api/complain'
import { ElMessage } from 'element-plus';

export default{
    components:{
        Edit,
    },
    data(){
        return {
            isInitialization: true,
            count: 0,
            listOfComplain: [],
            nowitem: null,
            message: '',
            dialogFormVisible: false,
        }
    },
    methods:{
        jump(item){
            if(item.type){
                this.$router.push('/music/'+item.objID);
            }
            else{
                this.$router.push('/songlist/'+item.objID);
            }
        },
        jumptoUser(item){
            this.$router.push('/user/info/'+item.comlainerID);
        },
        execute(item){
            this.dialogFormVisible=true;
            this.message='请输入处理意见';
            this.nowitem=item;
        },
        async submit(result){
            if(this.message===''||this.message=='请输入处理意见'){
                ElMessage({
                    message: '请输入处理意见',
                    type: 'warning',
                });
            }
            else{
                this.isInitialization=true;
                if(result==false) var data=await executeComplain('False',this.nowitem.id,this.message);
                else var data=await executeComplain('True',this.nowitem.id,this.message);
                if(data.code==0){
                    ElMessage({
                        message: '处理成功',
                        type: 'success',
                    });
                }
                else{
                    ElMessage({
                        message: '处理失败\n'+data.msg,
                        type: 'error',
                    });
                }
                this.dialogFormVisible=false;
                this.initialization();
            }
        },
        async initialization(){
            this.isInitialization=true;
            if(store.state.globalLogin==true&&store.state.loginUser.isAdmin==true){
                var data=await getComplain();
                var list=[];
                for(var i=0;i<data.data.length;i++){
                    var ob={
                        id : data.data[i].id,
                        comlainerID: data.data[i].complainer_id,
                        complainerName: data.data[i].complainer_name,
                        type: data.data[i].type,
                        typeName: null,
                            content: data.data[i].content,
                        objID: data.data[i].obj_id,
                        cover: "https://"+data.data[i].obj_cover_address,                        
                        uploaderID: data.data[i].obj_uploader_id,
                    };
                    if(ob.type==true) ob.typeName='歌曲';
                    else ob.typeName='歌单';
                    list.push(ob);
                }
                this.count=data.data.length;
                this.listOfComplain=list;
                this.isInitialization=false;
            }
            else{
                this.isInitialization=false;
                this.$router.push('/');
            }
        }
    },
    mounted(){
        this.initialization();
    }
}


</script>