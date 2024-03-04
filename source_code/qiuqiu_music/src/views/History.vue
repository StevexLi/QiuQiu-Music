<template>
    <div v-if="this.isInitialization" style="position: fixed; top: 0; min-width: 1200px;width: 100%;height: 100%;">
        <div v-loading="this.isInitialization" element-loading-text="正在加载..."  style="height: 100%;width: 100%;"></div>
    </div>
    <div v-else style="width: 100%;min-width: 1200px;">
        <div class="parent title1" style="height: 400px;justify-content: center;line-height: 400px;">
            <img :src="this.icon" style="position: relative;border-radius: 50%;width: 200px;height: 200px;margin-top: 100px;margin-left: -60%;"/>
            <span style="box-shadow: 0px 5px 5px -2px #ffffff;position: relative;width: 200px;height: 200px;line-height: 200px;left: 10px;bottom: 85px;font-size: 35px;font-weight: 300;color: black;">{{ this.store.state.loginUser.name }}</span>
        </div>
        <el-row class="parent" style="margin-top: 25px;height: 30px;line-height: 30px;">
            <div class="station"></div>
            <div style="width: 120ppx;font-size: 18px;text-align: right;">最大历史播放数量&nbsp:&nbsp</div>
            <span v-if="this.change"  @click="this.startChange()" style="width: 6%;font-size: 18px;text-align: left;">{{ this.$store.state.loginUser.recentPlayMax }}</span>
            <el-input v-else v-model="this.recentPlayMax" style="width: 10%;font-size: 18px;"></el-input>
            <button v-if="this.change" @click="this.startChange()" style="width: 5%;font-size: 18px;">修改</button>
            <button v-else @click="this.submit()" style="width: 5%;font-size: 18px;">提交</button>
        </el-row>
        <el-row class="parent" style="margin-bottom: 25px;height: 30px;">
            <div class="station"></div>
            <div class="lineDiv" style="width: 50%;">歌曲</div>
            <div class="lineDiv" style="width: 20%;">创作歌手</div>
            <div class="lineDiv" style="width: 10%;">上传用户</div>
            <div class="station"></div>
        </el-row>
        <el-row v-if="this.count==0" class="parent" style="margin-top: 25px;height: 30px;">
            <div class="station" style="height: 30px;"></div>
            <div class="lineDiv" style="width: 250px;font-size: 18px;">这个人很懒，什么都没有听过</div>
            <img src="../assets/history.jpg"/>
        </el-row>
        <el-row class="parent" v-for="(item,index) in listOfSong" :key = index>
            <div class="station" style="text-align: right;line-height: 75px;">{{ index+1 }}&nbsp&nbsp&nbsp&nbsp</div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 5%;"><el-avatar style="margin-top: 5px;"  shape="square" :fit="conintain" :size="65" :src='item.coverPath' @click="jumpToSong(item.id)"></el-avatar></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 5%;"><el-avatar style="margin-top: 5px;" shape="square" :fit="conintain" :size="65" :src='item.coverPath' @click="jumpToSong(item.id)"></el-avatar></div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 25%;"><span class="body btn" style="margin-left: 3%;" @click="jumpToSong(item.id)">{{ item.name }}</span></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 25%;"><span class="body btn" style="margin-left: 3%;" @click="jumpToSong(item.id)">{{ item.name }}</span></div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 20%;">
                <el-button class="elbtn" @click="this.playSong(item)"><el-icon><VideoPlay /></el-icon></el-button>
                <el-button class="like elbtn" v-if="this.likelist[index]==1" @click="this.favorSong(index,false)"></el-button>
                <el-button class="notlike elbtn" v-else @click="this.favorSong(index,true)"></el-button>
                <el-button class="elbtn" @click="this.showTable(item)"><el-icon><Plus /></el-icon></el-button>
                <el-button class="elbtn" @click="this.downLoad(item)"><el-icon><Download /></el-icon></el-button>
            </div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 20%;">
                <el-button class="elbtn" @click="this.playSong(item)"><el-icon><VideoPlay /></el-icon></el-button>
                <el-button class="like elbtn" v-if="this.likelist[index]==1" @click="this.favorSong(index,false)"></el-button>
                <el-button class="notlike elbtn" v-else @click="this.favorSong(index,true)"></el-button>
                <el-button class="elbtn" @click="this.showTable(item)"><el-icon><Plus /></el-icon></el-button>
                <el-button class="elbtn" @click="this.downLoad(item)"><el-icon><Download /></el-icon></el-button>
            </div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 20%;">{{ item.author }}</div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 20%;">{{ item.author }}</div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 10%;"><span class="body btn"  @click="this.jumpToUser(item.uploaderId)">{{ this.uploaderName[index] }}</span></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 10%;"><span class="body btn"  @click="this.jumpToUser(item.uploaderId)">{{ this.uploaderName[index] }}</span></div>
            <div class="station"></div>
        </el-row>
        <div class="parent" style="height: 150px;"></div>
    </div>
    <el-drawer v-model="table" title="选择添加到的歌单" direction="rtl" size="30%">
        <el-table :data="this.gripData" @row-click="addMusicToSong" style="cursor: pointer;">
            <el-table-column property="title" label="歌单名字" width="360px" />
        </el-table>
    </el-drawer>
</template>

<style scoped>
.title1{
    background-image: url('../assets/historybackground.jpg');
    background-size: 100% 100%;
}
.like{
    background-image: url("../assets/red_heart.png");
    background-size: 100% 100%;
    transition: 0.2s;
}
.like:hover{
    transition: 0.2s;
    scale: 1.25;
}
.notlike{
    background-image: url("../assets/black_heart.png");
    background-size: 100% 100%;
    transition: 0.2s;
}
.notlike:hover{
    transition: 0.2s;
    scale: 1.25;
}
.elbtn{
    position: relative;
    width: 40px;
    height: 40px;
}
.parent{
    width: 100%;
    min-width: 1200px;
}
.station{
    position: relative;
    width: 10%;
}
.lineDiv{
    position: relative;
    height: 75px;
    text-align: left;
    line-height: 75px;
}
.back1{
    background-color: #e1e3e3;
}
.title{
    font-size: 18px;
}
.body{
    font-size: 14px;
}
span:hover{
    color: #42b983;
}
</style>

<script>
import store from '@/store';
import { VideoPlay, Download, Plus } from '@element-plus/icons';
import playAudio1 from '../App.vue';
import playAudio2 from '../App.vue';
import playAudio3 from '../App.vue';
import download from 'downloadjs';
import { getHistory } from '@/api/history';
import Music from '@/components/music';
import { ElMessage } from 'element-plus';
import { updateUserInfo } from '@/api/User';
import { addSong, deleteSong, getLikeList } from '@/api/likeList';
import { getUserAllSongList1 } from '@/api/User';
import { addSongToList } from '@/api/songList';

export default{
    mixins: [playAudio1, playAudio2, playAudio3],
    components:{
        VideoPlay,
        Download,
        Plus,
    },
    data(){
        return {
            id: null,
            table: false,
            gripData: [],
            recentPlayMax: this.$store.state.loginUser.recentPlayMax,
            playMax: this.$store.state.loginUser.recentPlayMax,
            change: true,
            uid: null,
            listOfSong: [],
            uploaderName: [],
            isInitialization: true,
            count: 0,
            likelist: [],
            icon: store.state.loginUser.icon,
        }
    },
    methods:{
        showTable(item){
            this.id=item.id;
            if(store.state.globalLogin==false){
                this.$router.push('/login');
            }
            else{
                this.table=true;
            }
        },
        async addMusicToSong(row){
            var data=await addSongToList(row.list_id,this.id);
            if(data.code==0){
                ElMessage({
                    message: '添加成功',
                    type: 'success',
                })
            }
            else{
                ElMessage({
                    message: '添加失败\n'+data.msg,
                    type: 'error',
                })
            }
        },
        async favorSong(index,type){
            if(store.state.globalLogin==false){
                this.$router.push('/login');
            }
            else{
                if(this.likelist[index]==0&&type==true){
                    this.likelist[index]=1;
                    await addSong(this.listOfSong[index].id);
                }
                else if(this.likelist[index]==1&&type==false){
                    this.likelist[index]=0;
                    await deleteSong(this.listOfSong[index].id);
                }
            }
        },
        async addSongToList(item){
            if(store.state.globalLogin==true){

            }
        },
        playSong(item){
            this.playAudio1(item);
        },
        checkLikeList(data){
            var newlist=[];
            var i,j;
            for(i=0;i<this.count;i++){
                newlist.push(0);
            }
            if(store.state.globalLogin==true){
                for(i=0;i<this.count;i++){
                    for(j=0;j<data.length;j++){
                        if(this.listOfSong[i].id==data[j].song_id){
                            newlist[i]=1;
                            break;
                        }
                    }
                }
            }
            this.likelist=[];
            this.likelist=newlist;
        },
        downLoad(item){
            this.downloadFile(item.musicPath);
        },
        downloadFile(url) {
            if (store.state.loginUser == null)
                this.$router.push('/login');
            const urlParts = url.split('/');
            const filename = urlParts[urlParts.length - 1];
            fetch(url).then(res => {
                return res.blob()
            }).then(blob => {
                download(blob, filename)
            }).catch(err => {
                console.log(err)
                return false
            }).finally(res => {
                return true
            })
        },
        startChange(){
            this.change=false;
        },
        async submit(){
            if(this.recentPlayMax>50){
                ElMessage({
                    message: '最大历史播放数量不能超过50首',
                    type: 'warning',
                });
            }
            else{
                var data=await updateUserInfo(store.state.globalUserID,'','','',this.recentPlayMax);
                if(data.code==0){
                    store.commit('updateRecentPlay',this.recentPlayMax);
                    ElMessage({
                        message: '修改成功',
                        type: 'success',
                    });
                }
                else{
                    ElMessage({
                        message: '修改失败',
                        type: 'error',
                    });
                }
            }
            this.recentPlayMax=this.$store.state.loginUser.recentPlayMax;
            this.change=true;
        },
        async update(){
            var list1=[];
            var list2=[];
            var data=await getHistory();
            var x=data.data.length;
            for(var i=0;i<x;i++){
                var newMusic=new Music(data.data[i].song_id);
                newMusic.initForSongList(data.data[i]);
                list1.push(newMusic);
                list2.push(data.data[i].uploader_name);
            }
            this.checkLikeList();
            this.listOfSong=list1;
            this.uploaderName=list2;
            this.count=x;
        },
        async initialization(){
            this.uid=this.$route.params.uid;
            if(store.state.globalLogin==false){
                this.$router.push('/login');
            }
            else{
                this.isInitialization=true;
                if(store.state.globalUserID!=this.uid){
                    this.$router.push('/history/'+store.state.globalUserID);
                    
                }
                this.listOfSong=[];
                this.uploaderName=[];
                var data=await getHistory();
                this.count=data.data.length;
                for(var i=0;i<this.count;i++){
                    var newMusic=new Music(data.data[i].song_id);
                    newMusic.initForSongList(data.data[i]);
                    this.listOfSong.push(newMusic);
                    this.uploaderName.push(data.data[i].uploader_name);
                }
                this.update();
                this.isInitialization=false;
            }
        },
        jumpToUser(uid){
            this.$router.push('/user/info/'+uid);
        },
        jumpToSong(musicID){
            this.$router.push('/music/'+musicID);
        },
    },
    mounted(){
        setInterval(async () => {
            var data=await getLikeList();
            this.checkLikeList(data.data.content);
            this.gripData = await getUserAllSongList1();
        }, 5000);
        this.initialization();
    }
}
</script>