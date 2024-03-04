<template>
    <div v-if="this.isInitialization" style="position: fixed; top: 0; min-width: 1200px;width: 100%;height: 100%;">
        <div v-loading="this.isInitialization" element-loading-text="正在加载..."  style="height: 100%;width: 100%;"></div>
    </div>
    <div v-else>
        <div class="row title1" style="height: 400px;justify-content: center;line-height: 400px;">
            <img :src="this.icon" style="position: relative;border-radius: 50%;width: 200px;height: 200px;margin-top: 100px;margin-left: -60%;"/>
            <span style="box-shadow: 0px 5px 5px -2px #ffffff;position: relative;width: 200px;height: 200px;line-height: 200px;left: 10px;bottom: 85px;font-size: 35px;font-weight: 300;color: black;">{{ this.store.state.loginUser.name }}</span>
        </div>
        <el-row class="row" style="margin-top: 25px;height: 50px;">
            <div class="station"></div>
            <button class="title" @click="createSongList()" style="min-width: 70px;">+创建歌单</button>
        </el-row>
        <el-row style="position: relative;margin-bottom: 25px;min-width: 1200px;height: 30px;">
            <div class="station"></div>
            <div class="lineDiv" style="width: 40%;">歌单</div>
            <div class="lineDiv" style="width: 30%;">曲目数</div>
            <div class="lineDiv" style="width: 10%;">分享状态</div>
            <div class="station"></div>
        </el-row>
        <el-row v-for="(item,index) in songlist" :key = index class="row">
            <div class="station" style="text-align: right;line-height: 75px;">{{ index+1 }}&nbsp&nbsp&nbsp&nbsp</div>
            <div v-if="(index%2==0)" class="lineDiv back" style="width: 75px;"><el-avatar style="margin-top:5px;" shape="square" :fit="conintain" :size="65" :src='item.cover' @click="this.jumpto(item)"></el-avatar></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 75px;"><el-avatar style="margin-top:5px;" shape="square" :fit="conintain" :size="65" :src='item.cover' @click="this.jumpto(item)"></el-avatar></div>
            <div v-if="(index%2==0)" class="lineDiv back" style="width: 23%;"><span class="body" style="margin-left: 3%;" @click="this.jumpto(item)">{{ item.title }}</span></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 23%;"><span class="body" style="margin-left: 3%;" @click="this.jumpto(item)">{{ item.title }}</span></div>
            <div v-if="(index%2==0)" class="lineDiv back" style="width: 12%;">
                <el-button @click="this.playSongList(item)"><el-icon><VideoPlay /></el-icon></el-button>
                <el-button @click="this.delete(item)"><el-icon><Delete /></el-icon></el-button>
            </div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 12%;">
                <el-button @click="this.playSongList(item)"><el-icon><VideoPlay /></el-icon></el-button>
                <el-button @click="this.delete(item)"><el-icon><Delete /></el-icon></el-button>
            </div>
            <div v-if="(index%2==0)" class="lineDiv back" style="width: 30%;">{{ item.total }}首</div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 30%;">{{ item.total }}首</div>
            <div v-if="(index%2==0)" class="lineDiv back" style="width: 10%;"><el-switch v-model="item.shareable" @change="share(item)"/></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 10%;"><el-switch v-model="item.shareable" @change="share(item)"/></div>
            <div class="station"></div>
        </el-row>
        <div class="parent" style="height: 150px;"></div>
    </div>
</template>

<style scoped>
.title1{
    background-image: url('../assets/historybackground.jpg');
    background-size: 100% 100%;
}
.row{
    position: relative;
    min-width: 1200px;
    height: 75px;
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
.back{
    background-color:#e1e3e3;
}
.title{
    font-size: 18px;
    height: 50px;
    width: 120px;
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
import playAudio1 from '../App.vue';
import playAudio2 from '../App.vue';
import playAudio3 from '../App.vue';
import { changeShare, deleteSongList } from '../api/songList';
import { VideoPlay, Delete } from '@element-plus/icons';
import { getLikeList } from '@/api/likeList';
import { getUserAllSongList } from '@/api/User';
import SongList from '@/components/songList';

export default{
    mixins: [playAudio1, playAudio2, playAudio3],
    components: {
        VideoPlay,
        Delete,
    },
    data(){
        return {
            isInitialization: true,
            likelist: null,
            songlist: [],
            uid: null,
            icon: store.state.loginUser.icon,
        }
    },
    methods:{
        playSongList(item){
            console.log(item.musicList);
            this.playAudio3(item.musicList);
        },
        async initialization(){
            this.uid=this.$route.params.uid;
            if(store.state.globalLogin==false){
                this.$router.push('/login');
            }
            else{
                if(store.state.globalUserID!=this.uid){
                    this.$router.push('/mySongList/'+store.state.globalUserID);
                }
                var data=await getLikeList();
                this.songlist.push(new SongList(data.data,true));
                data=await getUserAllSongList();
                for(var i=0;i<data.total;i++){
                    this.songlist.push(new SongList(data.data[i],false))
                }
                this.isInitialization=false;
            }
        },
        createSongList(){
            this.$router.push('/createSongList');
        },
        share(item){
            if(item.songListID!=0){
                changeShare(item.songListID);
            }
            else{
                alert("该歌单不可分享！！");
                item.shareable=false;
            }
        },
        async delete(item){
            if(item.songListID!=0){
                this.isInitialization=true;
                var data=await deleteSongList(item.songListID);
                if(data.code==0){
                    var newArray = this.songlist.filter(i=>i.songListID != item.songListID);
                    this.songlist=newArray;
                }
                this.isInitialization=false;
                if(data.code==0) alert('删除成功');
                else alert("删除失败");
            }
            else{
                alert("该歌单不可删除！！");
            }
        },
        jumpto(item){
            if(item.songListID==0){
                this.$router.push('/user/info/'+this.uid);
            }
            else{
                this.$router.push('/user/songList/'+item.songListID);
            }
        }
    },
    mounted(){
        this.initialization();
    }
}

</script>