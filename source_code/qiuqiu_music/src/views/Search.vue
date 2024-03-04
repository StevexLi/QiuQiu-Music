<template>
    <div v-if="this.isInitialization" style="position: fixed; top: 0; min-width: 1200px;width: 100%;height: 100%;">
        <div v-loading="this.isInitialization" element-loading-text="正在加载..." style="height: 100%;width: 100%;"></div>
    </div>
    <div v-else style="width: 100%;min-width: 1200px;height: 100%;">
        <div class="parent title1" style="height: 400px;justify-content: center;line-height: 400px;">
            <el-input v-model="this.searchKeywords" placeholder="搜索歌曲、歌单" @keydown.enter.native="search" style="width: 55%;height: 40px;text-align: right;margin-top: -100px;" maxlength="30"></el-input>
            <el-button @click="search()" style="width: 40px;height: 40px;margin-top: -100px;"><el-icon><Search/></el-icon></el-button>
        </div>
        <el-row class="parent" style="margin-top: 25px;height: 30px;">
            <div class="station"></div>
            <span v-if="!this.isSong" class="title btn" @click="this.changeType(true)">歌曲</span>
            <span v-else class="title btn" style="color: #42b983;" >歌曲</span>
            <span v-if="this.isSong" class="title btn" @click="this.changeType(false)">歌单</span>
            <span v-else class="title btn" style="color: #42b983;">歌单</span>
        </el-row>
        <el-row v-if="isSong" class="parent" style="margin-bottom: 25px;height: 30px;">
            <div class="station"></div>
            <div class="lineDiv" style="width: 50%;">歌曲</div>
            <div class="lineDiv" style="width: 10%;">播放量</div>
            <div class="lineDiv" style="width: 10%;">创作歌手</div>
            <div class="lineDiv" style="width: 10%;">上传用户</div>
            <div class="station"></div>
        </el-row>
        <el-row v-else class="parent" style="margin-bottom: 25px;height: 30px;">
            <div class="station" style="height: 30px;"></div>
            <div class="lineDiv" style="width: 40%;">歌单</div>
            <div class="lineDiv" style="width: 30%;">曲目数</div>
            <div class="lineDiv" style="width: 10%;">分享用户</div>
            <div class="station" style="height: 30px;"></div>
        </el-row>
        <el-row v-if="isSong" class="parent" v-for="(item,index) in listOfSong" :key = index>
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
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 10%;">{{ item.played }}次</div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 10%;">{{ item.played }}次</div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 10%;">{{ item.author }}</div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 10%;">{{ item.author }}</div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 10%;"><span class="body btn"  @click="this.jumpToUser(item.uploaderId)">{{ this.uploaderName[index] }}</span></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 10%;"><span class="body btn"  @click="this.jumpToUser(item.uploaderId)">{{ this.uploaderName[index] }}</span></div>
            <div class="station"></div>
        </el-row>
        <el-row v-else class="parent" v-for="(item,index) in listOfSongList">
            <div class="station" style="text-align: right;line-height: 75px;">{{ index+1 }}&nbsp&nbsp&nbsp&nbsp</div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 5%;"><el-avatar style="margin-top: 5px;" shape="square" :fit="conintain" :size="65" :src='item.cover' @click="jumpToSongList(item.songListID)"></el-avatar></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 5%;"><el-avatar style="margin-top: 5px;" shape="square" :fit="conintain" :size="65" :src='item.cover' @click="jumpToSongList(item.songListID)"></el-avatar></div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 30%;"><span class="body btn" style="margin-left: 3%;" @click="jumpToSongList(item.songListID)">{{ item.title }}</span></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 30%;"><span class="body btn" style="margin-left: 3%;" @click="jumpToSongList(item.songListID)">{{ item.title }}</span></div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 5%;">
                <el-button class="elbtn"  @click="this.playSongList(item)"><el-icon><VideoPlay /></el-icon></el-button>
            </div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 5%;">
                <el-button class="elbtn"  @click="this.playSongList(item)"><el-icon><VideoPlay /></el-icon></el-button>
            </div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 30%;">{{ item.total }}首</div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 30%;">{{ item.total }}首</div>
            <div v-if="(index%2==0)" class="lineDiv back1" style="width: 10%;"><span class="body btn"  @click="this.jumpToUser(item.creatorID)">{{ this.uploaderName[index] }}</span></div>
            <div v-if="(index%2==1)" class="lineDiv" style="width: 10%;"><span class="body btn"  @click="this.jumpToUser(item.creatorID)">{{ this.uploaderName[index] }}</span></div>
            <div class="station"></div>
        </el-row>
        <el-row v-if="this.nowpage==1&&this.count==0" class="parent" style="margin-top: 25px;height: 30px;">
            <div class="station" style="height: 30px;"></div>
            <div class="lineDiv" style="width: 315px;font-size: 18px;text-align: left;">这个关键词似乎没什么用，试试别的吧</div>
            <img src="../assets/search.jpg" />
        </el-row>
        <el-row v-if="this.totalPage>1" class="parent" style="height: 40px;margin-top: 40px;justify-content: center;">
            <span style="width: 20%;"></span>
            <span v-for="(item,index) in this.pageNumber" :key=index style="width: 40px;height: 40px;margin-right: 40px;">
                <button v-if="(nowpage-index==1)" style="width: 40px;height: 40px;background-color: #42b983;" @click="this.changePageNum(item)">{{ item }}</button>
                <button v-else style="width: 40px;height: 40px;" @click="this.changePageNum(item)">{{ item }}</button>
            </span>
            <span style="width: 20%;"></span>
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
.title1{
    background-image: url('../assets/searchbackground.png');
    background-size: 100% 100%;
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
.btn:hover{
    color: #42b983;
}
</style>

<script>
import store from '@/store';
import { VideoPlay, Search, Download, Plus} from '@element-plus/icons-vue';
import playAudio1 from '../App.vue';
import playAudio2 from '../App.vue';
import playAudio3 from '../App.vue';
import download from 'downloadjs';
import { searchSong, searchSongList } from '@/api/search';
import Music from '@/components/music';
import SongList from '@/components/songList';
import { ElMessage } from 'element-plus';
import { addSong, deleteSong, getLikeList } from '@/api/likeList';
import { getUserAllSongList1 } from '@/api/User';
import { addSongToList } from '@/api/songList';

export default{
    mixins: [playAudio1, playAudio2, playAudio3],
    components:{
        VideoPlay,
        Search,
        Download,
        Plus,
    },
    data(){
        return {
            id: null,
            table: false,
            gripData: [],
            nowpage: 1,
            isInitialization: true,
            keywords: null,
            totalPage: 0,
            count: 0,
            listOfSong: [],
            listOfSongList: [],
            isSong: true,
            uploaderName: [],
            likelist: [],
            pageNumber: [],
            searchKeywords: '',
        };
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
        async search(){
            if(this.searchKeywords===''){
                ElMessage({
                    message: '请输入搜索内容',
                    type: 'warning',
                });
            }
            else{
                this.isInitialization=true;
                this.listOfSong=[];
                this.listOfSongList=[];
                this.uploaderName=[];
                this.pageNumber=[];
                this.keywords=this.searchKeywords;
                this.$router.push('/search/'+this.searchKeywords);
                await this.changePageNum(1);
                this.searchKeywords='';
                this.isInitialization=false;
            }
        },
        async search1(search_words){
            this.isInitialization=true;
            this.listOfSong=[];
            this.listOfSongList=[];
            this.uploaderName=[];
            this.pageNumber=[];
            this.keywords=search_words;
            this.$router.push('/search/'+search_words);
            await this.changePageNum(1);
            this.searchKeywords='';
            this.isInitialization=false;
        },
        playSong(item){
            this.playAudio1(item);
        },
        async playSongList(item){
            this.playAudio3(item.musicList);
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
        changeType(type){
            this.isSong=type;
            this.changePageNum(1);
        },
        async changePageNum(pageNum){
            this.nowpage=pageNum;
            this.isInitialization=true;
            var data;
            this.uploaderName=[];
            this.pageNumber=[];
            if(this.isSong==true){
                this.listOfSong=[];
                this.uploaderName=[];
                data=await searchSong(this.keywords,pageNum);
                this.totalPage=data.total_page;
                this.count=data.current_entry_num;
                for(var i=0;i<this.count;i++){
                    var newMusic=new Music(data.data[i].song_id);
                    newMusic.initForSongList(data.data[i]);
                    this.listOfSong.push(newMusic);
                    this.uploaderName.push(data.data[i].uploader_name);
                }
            }
            else{
                this.listOfSongList=[];
                this.uploaderName=[];
                data=await searchSongList(this.keywords,pageNum);
                this.totalPage=data.total_page;
                this.count=data.current_entry_num;
                for(var i=0;i<this.count;i++){
                    var newSongList=new SongList(data.data[i],false);
                    this.listOfSongList.push(newSongList);
                    this.uploaderName.push(data.data[i].creator_name);
                }
            }
            for(var i=1;i<=this.totalPage;i++){
                this.pageNumber.push(i);
            }
            this.isInitialization=false;
        },
        async initialization(){
            this.isInitialization=true;
            this.keywords=this.$route.params.keywords;
            var data=await searchSong(this.keywords,1);
            this.totalPage=data.total_page;
            this.count=data.current_entry_num;
            for(var i=0;i<this.count;i++){
                var newMusic=new Music(data.data[i].song_id);
                newMusic.initForSongList(data.data[i]);
                this.listOfSong.push(newMusic);
                this.uploaderName.push(data.data[i].uploader_name);
            }
            for(var i=1;i<=this.totalPage;i++){
                this.pageNumber.push(i);
            }
            this.isInitialization=false;
        },
        jumpToUser(uid){
            this.$router.push('/user/info/'+uid);
        },
        jumpToSong(musicID){
            this.$router.push('/music/'+musicID);
        },
        jumpToSongList(songListID){
            this.$router.push('/user/songList/'+songListID);
        },
    },
    mounted(){
        setInterval(async()=>{
            var data=await getLikeList();
            this.checkLikeList(data.data.content);
            this.gripData = await getUserAllSongList1();
        },5000)
        this.initialization();
    }
}

</script>
