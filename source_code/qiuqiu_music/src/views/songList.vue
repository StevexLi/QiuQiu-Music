<template>
    <div v-if="!isLoaded" style="position: fixed; top: 0; min-width: 1200px;width: 100%;height: 100%;">
        <div v-loading="!isLoaded" element-loading-text="正在加载..." style="height: 100%;width: 100%;"></div>
    </div>
    <div class="songList" v-if="isLoaded">
        <el-dialog v-model="centerDialogVisible" width="30%" center>
            <span>
                添加成功
            </span>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="centerDialogVisible = false">取消</el-button>
                    <el-button type="primary" @click="centerDialogVisible = false">
                        确定
                    </el-button>
                </span>
            </template>
        </el-dialog>
        <el-drawer v-model="table" title="选择添加到的歌单" direction="rtl" size="30%">
            <el-table :data="gridData" @row-click="addMusicToSongList" style="cursor: pointer;">
                <el-table-column property="title" label="歌单名字" width="360px" />
            </el-table>
        </el-drawer>
        <el-dialog v-model="dialogFormVisible" title="投诉">
            <el-form :model="form">
                <el-form-item label="投诉原因" :label-width="formLabelWidth">
                    <el-input v-model="form.name" autocomplete="off" />
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">取消</el-button>
                    <el-button type="primary" @click="confirmComplain">
                        确认
                    </el-button>
                </span>
            </template>
        </el-dialog>
        <div id="headData">\
            <input type="file" id="file-input" style="display: none" @change="handleFileChange" v-if="isChange == true" />
            <label for="file-input" style="cursor: pointer;">
                <img :src="nowSongList.cover" id="coverImg">
            </label>
            <div id="infoDiv">
                <span id="nameContent" v-if="isChange == false">
                    {{ nowSongList.title }}
                </span>
                <input id="nameContentChange" v-if="isChange == true" v-model="nowSongList.title">
                <span id="tagSpan" v-if="isChange == false">
                    标签:
                    <span style="margin-left: 20px;font-size: 18px;">{{ nowSongList.tag[0] }}</span>
                    <span style="margin-left: -4px;font-size: 18px;">{{ nowSongList.tag[1] }}</span>
                    <span style="margin-left: -4px;font-size: 18px;">{{ nowSongList.tag[2] }}</span>
                    <span style="margin-left: -4px;font-size: 18px;">{{ nowSongList.tag[3] }}</span>
                    <span style="margin-left: -4px;font-size: 18px;">{{ nowSongList.tag[4] }}</span>
                    <span style="margin-left: -4px;font-size: 18px;">{{ nowSongList.tag[5] }}</span>
                </span>
                <span id="tagSpan" v-if="isChange == true">
                    标签:
                    <el-select clearable v-model="nowSongList.tag[0]" class="m-2" placeholder="tag0" size="large"
                        style="width: 100px;margin-left: 10px;">
                        <el-option v-for="item in filteredOptions" :key="item.value" :label="item.label"
                            :value="item.value" />
                    </el-select>
                    <el-select clearable v-model="nowSongList.tag[1]" class="m-2" placeholder="tag1" size="large"
                        style="width: 100px;margin-left: 10px;">
                        <el-option v-for="item in filteredOptions" :key="item.value" :label="item.label"
                            :value="item.value" />
                    </el-select>
                    <el-select clearable v-model="nowSongList.tag[2]" class="m-2" placeholder="tag2" size="large"
                        style="width: 100px;margin-left: 10px;">
                        <el-option v-for="item in filteredOptions" :key="item.value" :label="item.label"
                            :value="item.value" />
                    </el-select>
                    <el-select clearable v-model="nowSongList.tag[3]" class="m-2" placeholder="tag3" size="large"
                        style="width: 100px;margin-left: 10px;">
                        <el-option v-for="item in filteredOptions" :key="item.value" :label="item.label"
                            :value="item.value" />
                    </el-select>
                    <el-select clearable v-model="nowSongList.tag[4]" class="m-2" placeholder="tag4" size="large"
                        style="width: 100px;margin-left: 10px;">
                        <el-option v-for="item in filteredOptions" :key="item.value" :label="item.label"
                            :value="item.value" />
                    </el-select>
                </span>
                <div id="buttonDiv">
                    <el-button type="success" round @click="addAllSong">播放全部</el-button>
                    <el-button round @click="this.shoucang()">批量收藏</el-button>
                    <el-button round @click="this.tousu()">投诉</el-button>
                </div>
                <el-button round id="changInfoButton" v-if="store.state.globalLogin==true && store.state.loginUser && nowSongList.creatorID == loginUser.id && isChange == false"
                    @click="isChange = true">编辑信息</el-button>
                <el-button round id="changInfoButton" v-if="store.state.globalLogin==true && store.state.loginUser && nowSongList.creatorID == loginUser.id && isChange == true"
                    @click="changeInfo">修改信息</el-button>
                <div id="songListIntro">
                    简介
                    <br>
                    {{ nowSongList.introduction }}
                </div>
            </div>
        </div>
        <div class="contentSpan" style="flex-direction: column;display: flex;width: 100%;">
            <div class="itemDiv">
                <div class="itemSpanNum">序号</div>
                <div class="itemSpanOpe">操作</div>
                <div class="itemSpanMusic">标题</div>
                <div class="itemSpanSinger">歌手</div>
            </div>
            <div style="margin-top: -8px;">
                <div class="itemDiv" v-for="(item, index) in nowSongList.musicList" :key="index">
                    <div style="height: 100%; width: 100%; background-color: #e1e3e3;flex-direction: row;display: flex;"
                        v-if="index % 2 == 0">
                        <div class="itemSpanNum" style="color: black;cursor: pointer;" :id="'itemNum' + index"
                            @mouseover="mouseOverToChangeColor('itemNum' + index)"
                            @mouseout="mouseOutToChangeColor('itemNum' + index)">{{ index + 1 }}</div>
                        <div class="itemSpanOpe" style="color: black; " :id="'itemDownload' + index">
                            <el-icon style="cursor: pointer;" @click="downloadFile(item.musicPath)">
                                <Download />
                            </el-icon>
                            <el-icon style="cursor: pointer;" @click="deleteSong(item.id)"
                                v-if="store.state.globalLogin==true && nowSongList.creatorID == loginUser.id">
                                <DeleteFilled />
                            </el-icon>
                            <el-icon style="cursor: pointer;" @click="playMusic(item)"><VideoPlay /></el-icon>
                        </div>
                        <div class="itemSpanMusic" style="color: black; cursor: pointer;" :id="'itemName' + index"
                            @mouseover="mouseOverToChangeColor('itemName' + index)"
                            @mouseout="mouseOutToChangeColor('itemName' + index)" @click="toMusicPage(item)">{{ item.name }}
                        </div>
                        <div class="itemSpanSinger" style="color: black;cursor: pointer;" :id="'itemAuthor' + index"
                            @mouseover="mouseOverToChangeColor('itemAuthor' + index)"
                            @mouseout="mouseOutToChangeColor('itemAuthor' + index)">{{ item.author }}</div>
                    </div>
                    <div style="height: 100%; width: 100%;flex-direction: row;display: flex;" v-if="index % 2 == 1">
                        <div class="itemSpanNum" style="color: black;cursor: pointer;" :id="'itemNum' + index"
                            @mouseover="mouseOverToChangeColor('itemNum' + index)"
                            @mouseout="mouseOutToChangeColor('itemNum' + index)">{{ index + 1 }}</div>
                        <div class="itemSpanOpe" style="color: black; " :id="'itemDownload' + index">
                            <el-icon style="cursor: pointer;" @click="downloadFile(item.musicPath)">
                                <Download />
                            </el-icon>
                            <el-icon style="cursor: pointer;" @click="removeSongFromList(item.id)"
                                v-if="store.state.globalLogin==true && nowSongList.creatorID == loginUser.id">
                                <DeleteFilled />
                            </el-icon>
                            <el-icon style="cursor: pointer;" @click="playMusic(item)"><VideoPlay /></el-icon>
                        </div>
                        <div class="itemSpanMusic" style="color: black; cursor: pointer;" :id="'itemName' + index"
                            @mouseover="mouseOverToChangeColor('itemName' + index)"
                            @mouseout="mouseOutToChangeColor('itemName' + index)" @click="toMusicPage(item)">{{ item.name }}
                        </div>
                        <div class="itemSpanSinger" style="color: black;cursor: pointer;" :id="'itemAuthor' + index"
                            @mouseover="mouseOverToChangeColor('itemAuthor' + index)"
                            @mouseout="mouseOutToChangeColor('itemAuthor' + index)">{{ item.author }}</div>
                    </div>
                </div>
            </div>
        </div>
        <div style="height: 300px;"></div>
    </div>
</template>
<style>
:root {
    --main-color: #42b983;
}

.el-button--text {
    margin-right: 15px;
}

.el-select {
    width: 300px;
}

.el-input {
    width: 300px;
}

.dialog-footer button:first-child {
    margin-right: 10px;
}

#nameContentChange {
    position: relative;
    display: flex;
    height: 40px;
    width: 300px;
    margin-bottom: 20px;
    font-size: 40px;
    font-weight: bolder;
    border-width: 100;
    border-radius: 10px;
    border-color: rgb(242, 242, 242);
    background-color: rgb(242, 242, 242);
}

.itemSpanSinger {
    color: #757776;
    display: flex;
    width: 300px;
    height: 50px;
    align-items: center;
    justify-content: center;
    margin-left: 220px;
}

.itemSpanDuration {
    color: #757776;
    display: flex;
    width: 100px;
    height: 50px;
    align-items: center;
    justify-content: center;
    margin-left: 190px;
}

.itemSpanMusic {
    color: #757776;
    display: flex;
    width: 400px;
    height: 50px;
    align-items: center;
    justify-content: center;
    margin-left: 100px;
}

.itemSpanOpe {
    color: #757776;
    display: flex;
    width: 100px;
    height: 50px;
    align-items: center;
    justify-content: center;
    margin-left: 60px;
    font-size: 20px;
}

.itemSpanNum {
    color: #757776;
    display: flex;
    font-size: 20px;
    width: 100px;
    height: 50px;
    align-items: center;
    justify-content: center;
    margin-left: 30px;
}

.contentSpan {
    font-size: 20px;
    position: relative;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 10px;
    height: auto;
    width: 80%;
    left: 10%;
}

.itemDiv {
    display: flex;
    height: 50px;
    margin-top: 0px;
    width: 1200px;
}

#changInfoButton {
    position: relative;
    display: flex;
    top: 20px;
}

#contentDiv {
    position: relative;
    display: flex;
    top: 500px;
    width: 1100px;
    left: 200px;
    height: 800px;
}

#musicItem {
    width: 1100px;
}

#content {
    background-color: red;
    position: relative;
    top: 1200px;
}

.durationSpan {
    margin-left: 260px;
    font-size: 15px;
    color: rgba(93, 91, 91, 0.85);
}

.singerSpan {
    margin-left: 260px;
    font-size: 15px;
    color: rgba(93, 91, 91, 0.85);
}

.musicSpan {
    position: relative;
    margin-left: 100px;
    font-size: 15px;
    color: rgba(93, 91, 91, 0.85);
}

#musicContent {
    text-align: left;
    position: relative;
    height: 200px;
    width: 1100px;
    top: 380px;
    left: 200px;
}

#playButton {
    cursor: pointer;
    height: 40px;
    width: 130px;
    background-color: var(--main-color);
    border: 0;
    color: white;
    font-weight: 500;
}

#buttonDiv {
    position: relative;
    display: flex;
    height: 65px;
    width: 600px;
    left: 0px;
    text-align: left;
    top: 40px;
    font-size: 18px;
}

#playNumSpan {
    position: relative;
    display: flex;
    height: 20px;
    width: 600px;
    left: 0px;
    text-align: left;
    top: 20px;
    font-size: 18px;
}

#tagSpan {
    position: relative;
    display: flex;
    height: 20px;
    width: 600px;
    left: 0px;
    text-align: left;
    font-size: 18px;
}

#nameContent {
    position: relative;
    display: flex;
    height: 70px;
    width: 600px;
    left: 0px;
    font-size: 35px;
    text-align: left;
    font-weight: 400;

}

#infoDiv {
    position: relative;
    margin-left: 100px;
    top: 75px;
    height: 200px;
    width: 600px;
}

#headData {
    position: relative;
    left: 100px;
    display: flex;
    height: 400px;
    width: 1200px;
}
#songListIntro{
    height:100px;
    width: 400px;
    position: relative;
    display: flex;
    left: 500px;
    top: -150px;
    border-width: 3px;
    word-break: break-all;
}

#coverImg {
    position: relative;
    height: 250px;
    width: 250px;
    left: 40px;
    top: 50px;
}
</style>
<script>
import { getUserAllSongList1 } from '../api/User'
import store from '@/store';
import { getSongList } from '../api/songList'
import SongList from '../components/songList'
import download from 'downloadjs';
import { mapState } from 'vuex';
import { updateSongList } from '../api/songList';
import { DeleteFilled } from '@element-plus/icons';
import { Download } from '@element-plus/icons';
import { removeSong } from '../api/songList'
import { addSong } from '../api/songList'
import { setComplain } from '../api/complain';
import playAudio1 from '../App.vue';
import playAudio2 from '../App.vue';
import playAudio3 from '../App.vue';
import { VideoPlay } from '@element-plus/icons';
export default ({
    mixins: [playAudio1, playAudio2, playAudio3],
    name: "App",
    components: {
        DeleteFilled,
        Download,
        VideoPlay
    },
    data() {
        return {
            centerDialogVisible : false,
            table: false,
            gridData: [],
            dialogFormVisible: false,
            formLabelWidth: '250px',
            form: {
                name: '',
            },
            nowSongList: null,
            isLoaded: false,
            isChange: false,
            options: [
                {
                    value: '国语',
                    label: '国语',
                },
                {
                    value: '外语',
                    label: '外语',
                },
                {
                    value: '小清新',
                    label: '小清新',
                },
                {
                    value: '伤感',
                    label: '伤感',
                },
            ],
            fileTemp: null,
            id: 0,
        }
    },
    methods: {
        playMusic(music){
            this.playAudio1(music);
        },
        async deleteSong(id){
            await removeSong(id,this.nowSongList.songListID);
            this.init();
        },
        addAllSong(){
            this.playAudio3(this.nowSongList.musicList);
        },
        shoucang(){
            if(store.state.globalLogin==false){
                this.$router.push('/login');
            }
            else{
                this.table=true;
            }
        },
        tousu(){
            if(store.state.globalLogin==false){
                this.$router.push('/login');
            }
            else{
                this.dialogFormVisible=true;
            }
        },
        async addMusicToSongList(row){
            this.centerDialogVisible = true;
            for(let i = 0;i < this.nowSongList.musicList.length;i++)
            {
                await addSong(row.list_id, this.nowSongList.musicList[i].id);
            }

        },
        async removeSongFromList(id) {
            this.isLoaded = false;
            await removeSong(id, this.id);
            this.id = this.$route.params.songListId;
            var data = await getSongList(this.id);
            var info = data.info;
            this.nowSongList = new SongList(info, false);
            this.isLoaded = true;
        },
        async confirmComplain() {
            if (this.form.name.length > 256) {
                alert("投诉内容过长，限制为256个字");
                return;
            }
            alert("投诉成功");
            await setComplain(this.nowSongList.songListID, 'False', this.form.name);
        },
        async changeInfo() {
            this.isChange = false;
            await updateSongList(this.id, this.nowSongList.title, this.nowSongList.introduction, this.fileTemp, this.nowSongList.tag);
        },
        handleFileChange(event) {
            this.fileTemp = document.getElementById('file-input').files[0];
            const file = event.target.files[0];
            const reader = new FileReader();
            reader.onload = (e) => {
                this.nowSongList.cover = e.target.result;
            };
            reader.readAsDataURL(file);
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
        favorAllSongList() {

        },
        toMusicPage(music) {
            this.$router.push('/music/' + music.id);
        },
        async init() {
            this.id = this.$route.params.songListId;
            var data = await getSongList(this.id);
            var info = data.info;
            this.nowSongList = new SongList(info, false);
            this.isLoaded = true;
            this.gridData = await getUserAllSongList1();
        },
        mouseOverToChangeColor(id) {
            var ele = document.getElementById(id);
            ele.style.color = this.getColor;
        },
        mouseOutToChangeColor(id) {
            if (id != this.nowElementSpan) {
                var ele = document.getElementById(id);
                ele.style.color = 'black';
            }
        },
        mouseClickToChangeColor(id) {
            var ele = document.getElementById(this.nowElementSpan);
            ele.style.color = 'black';
            this.nowElementSpan = id;
            ele = document.getElementById(this.nowElementSpan);
            ele.style.color = this.getColor;
            this.judgeContentEmpty()
        },
    },
    mounted() {
        this.init();
    },
    computed: {
        ...mapState(['loginUser', 'globalIsLoaded']),
        getColor() {
            return getComputedStyle(document.documentElement).getPropertyValue('--main-color');
        },
        filteredOptions() {
            // 过滤选项，排除已选择的值
            return this.options.filter(option => !this.nowSongList.tag.includes(option.value));
        }
    },
})
</script>

