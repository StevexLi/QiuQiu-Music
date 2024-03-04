<template>
    <div v-if="!isloaded" style="position: fixed; top: 0; min-width: 1200px;width: 100%;height: 100%;">
        <div v-loading="!isloaded" element-loading-text="正在加载..." style="height: 100%;width: 100%;"></div>
    </div>
    <div class="musicItem" v-if="isloaded" style="min-width: 1200px;">
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
        <div id="headerInfo">
            <input type="file" id="file-input" style="display: none" @change="handleFileChange" v-if="isChange == true" />
            <label for="file-input" style="cursor: pointer;">
                <img :src="nowPlayMusic.coverPath" id="headImg">
            </label>
            <div id="infoDiv">
                <input id="nameContentChange" v-if="isChange == true" v-model="nowPlayMusic.name">
                <div id="nameContent" v-if="isChange == false">{{ nowPlayMusic.name }}</div>
                <div id="singerContent">作者: {{ nowPlayMusic.author }}</div>
                <div id="tagContent" v-if="!isChange">
                    标签:
                    <span style="margin-left: 25px;font-size: 17px;">
                        {{ nowPlayMusic.tag1 }}
                    </span>
                    <span style="margin-left: 0px;font-size: 17px;">
                        {{ nowPlayMusic.tag2 }}
                    </span>
                    <span style="margin-left: 0px;font-size: 17px;">
                        {{ nowPlayMusic.tag3 }}
                    </span>
                    <span style="margin-left: 0px;font-size: 17px;">
                        {{ nowPlayMusic.tag4 }}
                    </span>
                    <span style="margin-left: 0px;font-size: 17px;">
                        {{ nowPlayMusic.tag5 }}
                    </span>
                    <span style="margin-left: 5px;font-size: 17px;">
                        {{ nowPlayMusic.tag6 }}
                    </span>
                </div>
                <div id="tagContent" v-if="isChange">
                    标签:
                    <el-select clearable v-model="nowPlayMusic.tag1" class="m-2" placeholder="tag0" size="large"
                        style="width: 100px;margin-left: 10px;">
                        <el-option v-for="item in filteredOptions" :key="item.value" :label="item.label"
                            :value="item.value" />
                    </el-select>
                    <el-select clearable v-model="nowPlayMusic.tag2" class="m-2" placeholder="tag1" size="large"
                        style="width: 100px;margin-left: 10px;">
                        <el-option v-for="item in filteredOptions" :key="item.value" :label="item.label"
                            :value="item.value" />
                    </el-select>
                    <el-select clearable v-model="nowPlayMusic.tag3" class="m-2" placeholder="tag2" size="large"
                        style="width: 100px;margin-left: 10px;">
                        <el-option v-for="item in filteredOptions" :key="item.value" :label="item.label"
                            :value="item.value" />
                    </el-select>
                    <el-select clearable v-model="nowPlayMusic.tag4" class="m-2" placeholder="tag3" size="large"
                        style="width: 100px;margin-left: 10px;">
                        <el-option v-for="item in filteredOptions" :key="item.value" :label="item.label"
                            :value="item.value" />
                    </el-select>
                    <el-select clearable v-model="nowPlayMusic.tag5" class="m-2" placeholder="tag4" size="large"
                        style="width: 100px;margin-left: 10px;">
                        <el-option v-for="item in filteredOptions" :key="item.value" :label="item.label"
                            :value="item.value" />
                    </el-select>
                </div>
                <div id="buttonContent">
                    <el-button type="success" round @click='clickToPlayAudio(nowPlayMusic)'>播放</el-button>
                    <el-button round @click="toFavorMusic">收藏</el-button>
                    <el-button round @click="downloadFile(nowPlayMusic.musicPath)">下载</el-button>
                    <el-button round @click="dialogFormVisible = true;">投诉</el-button>
                    <el-button round @click="addToMySongList">添加到我的歌单</el-button>
                </div>
                <el-button round id="changInfoButton" v-if="$store.state.loginUser &&  nowPlayMusic.uploaderId == loginUser.id && isChange == false"
                    @click="isChange = true">编辑信息</el-button>
                <el-button round id="changInfoButton" v-if="$store.state.loginUser && nowPlayMusic.uploaderId == loginUser.id && isChange == true"
                    @click="changeInfo">修改信息</el-button>
                <div id="songListIntro">
                    简介
                    <br>
                    {{ nowPlayMusic.introduction }}
                </div>
            </div>
        </div>
        <div id="lyricsDiv" v-if="has_lyric_in_item">
            <span style="text-align: left;">
                歌词
            </span>
            <div id="lyricsContent">
                <span class="music_play_page_middle_placeholder2">
                    <span v-for="(item, index) in $store.state.globalLyricSets2.ms" class="music_play_page_lyric_line2"
                        :key="index" :title="item.c">
                        {{ item.c }}
                    </span>
                </span>
            </div>
            <span class="isShowLyricsSpan" v-if="!isLyricsShow" @click="showAllLyrics">[展开]</span>
            <span class="isShowLyricsSpan" v-if="isLyricsShow" @click="nowShowAllLyrics">[收回]</span>
        </div>
        <div id="lyricsDiv1" v-else>
            <span style="text-align: left;">
                歌词
            </span>
            <div id="lyricsContent1">
                <span class="music_play_page_middle_placeholder2">
                    <span class="music_play_page_lyric_line2">
                        无歌词，请欣赏
                    </span>
                </span>
            </div>
        </div>
        <div id="commentDiv">
            <span style="text-align: center;width: 100%;font-size: 25px;">评论</span>
            <el-input v-model="textarea" maxlength="300" placeholder="说说你的看法吧~" show-word-limit type="textarea"
                id="inputContent" />
            <button id="representComment" @click="sendComment">发表评论</button>
        </div>
        <div id="commentContent">
            <span style="text-align: left;font-size: 15px;">精彩评论</span>
            <hr style="width: 800px">
            <div v-for="(item, index) in comment" :key="index">
                <div id="eachComment">
                    <div style="height: 70px;width: 70px;">
                        <img :src="item.comentUser.img" :id="'userIcon' + index" class="userIcon"
                            @click="clickUserName(item.comentUser.id)">
                    </div>
                    <span :id="'userName' + index" class="userName" @mousemove="mouseOverToChangeColor('userName' + index)"
                        @mouseout="mouseOutToChangeColor('userName' + index, 'black')"
                        @click="clickUserName(item.comentUser.id)">{{ item.comentUser.name }}</span>
                    <span :id="'time' + index" class="time">{{ item.commentTime }}</span>
                    <span :id="'comment' + index" class="commentItem">{{ item.commentContent }}</span>
                    <span v-if="loginUser.id == item.comentUser.id" :id="'deleteSpan' + index" class="deleteSpan"
                        @mousemove="mouseOverToChangeColor('deleteSpan' + index)"
                        @mouseout="mouseOutToChangeColor('deleteSpan' + index, '#999')"
                        @click="removeComment(index)">删除</span>
                </div>
                <hr style="width: 800px;margin-top: 20px;">
            </div>
        </div>
        <div style="height: 300px;">
        </div>
    </div>
</template>
<style scoped>
:root {
    --main-color: #42b983;
}

.music_play_page_middle_placeholder2 {
    display: block;
    /*background: green;*/
    height: 10%;
    /*transition: 0.5s;*/
    /*scroll-behavior: smooth;*/
}

.music_play_page_lyric_line2 {
    display: block;
    /*border: 1px solid red;*/
    font-size: 22px;
    line-height: 30px;
    height: 30px;
    margin: 0;
    padding: 0;
    /*margin-top: 1%;*/
    /*margin-bottom: 1%;*/
    /*margin: auto;*/
    width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    -o-text-overflow: ellipsis;
    white-space: nowrap;
    /*width: 40px;*/
    max-width: 1200px;
    transition: 0.2s;
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
.music_play_page_lyric_line2:hover {
    cursor: pointer;
    color: #42b983;
    transition: 0.2s;
}

.deleteSpan {
    position: relative;
    display: flex;
    cursor: pointer;
    color: #999;
    font-size: 15px;
    margin-top: 15px;
    left: 80px;
    top: -50px;
    width: 30px;
}

.commentItem {
    position: relative;
    display: flex;
    height: 100px;
    width: 730px;
    top: -50px;
    left: 80px;
    margin-top: 15px;
    text-align: left;
    word-break: break-all;
}

.time {
    position: relative;
    display: flex;
    width: 500px;
    left: 80px;
    top: -60px;
    margin-top: 15px;
    color: #999;
    font-weight: 100;
}

.userName {
    position: relative;
    display: flex;
    width: 70px;
    left: 80px;
    top: -60px;
    color: #999;
    font-weight: 200;
    cursor: pointer;
}

.userIcon {
    position: relative;
    width: 70px;
    height: 70px;

    border-radius: 50%;

    cursor: pointer;
}

#eachComment {
    position: relative;
    display: flex;
    flex-direction: column;
    height: 150px;
    border: 0;
}

#headerInfo {
    position: relative;
    height: 325px;
    width: 100%;
}

#changInfoButton {
    position: relative;
    display: flex;
    margin-top: 10px;
    width: 150px;
}

#headImg {
    position: relative;
    display: flex;
    left: 150px;
    top: 50px;
    height: 250px;
    width: 250px;
}

#infoDiv {
    position: relative;
    display: flex;
    flex-direction: column;
    height: 200px;
    width: 800px;
    top: -170px;
    left: 480px;

}

#nameContent {
    position: relative;
    display: flex;
    height: 50px;
    width: 100%;
    font-size: 30px;
    font-weight: 50;

}

#singerContent {
    position: relative;
    display: flex;
    height: 50px;
    width: 100%;
    margin-top: 10px;
}

#tagContent {
    position: relative;
    display: flex;
    height: 50px;
    width: 100%;
    margin-top: 10px;
}

#buttonContent {
    position: relative;
    display: flex;
    height: 100px;
    width: 100%;
    margin-top: 30px;
}

#lyricsDiv {
    position: relative;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    height: 350px;
    width: 800px;
    left: 150px;
    margin-top: 40px;
}

#lyricsContent {
    position: relative;
    display: flex;
    width: 100%;
    overflow: hidden;
    font-size: 15px;
    height: 300px;
    text-align: left;
    margin-top: 23px;
}

#lyricsDiv1 {
    position: relative;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    height: 100px;
    width: 800px;
    left: 150px;
    margin-top: 40px;
}

#lyricsContent1 {
    position: relative;
    display: flex;
    width: 100%;
    overflow: hidden;
    font-size: 15px;
    height: 50px;
    text-align: left;
    margin-top: 23px;
}

#commentDiv {
    position: relative;
    display: flex;
    flex-direction: column;
    height: 300px;
    width: 800px;
    left: 150px;
    margin-top: 50px;
}

#inputContent {
    margin-top: 30px;
    height: 120px;
}

.isShowLyricsSpan {
    color: var(--main-color);
    font-size: 15px;
    text-align: left;
    cursor: pointer;
}

#representComment {
    position: relative;
    height: 50px;
    width: 100px;
    margin-top: 50px;
    font-size: 18px;
    left: 700px;
    background-color: var(--main-color);
    color: white;
    border: 0;
    border-radius: 3px;
    cursor: pointer;
}

#commentContent {
    position: relative;
    display: flex;
    flex-direction: column;
    width: 800px;
    left: 150px;
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
</style>
<script>
import { mapState } from 'vuex';
import { ref } from 'vue'
import Music from '../components/music'
import playAudio1 from '../App.vue';
import playAudio2 from '../App.vue';
import playAudio3 from '../App.vue';
import download from 'downloadjs';
import { favorMusic } from '../api/music';
import store from '@/store';
import { getUserAllSongList1 } from '../api/User'
import { addSong } from '../api/songList'
import { updateMusic } from '../api/music'
import { getComment } from '../api/comment'
import { addComment } from '../api/comment'
import { removeComment } from '../api/comment';
import { setComplain } from '../api/complain';
import { get2, get3 } from "@/api/api";
export default ({
    mixins: [playAudio1, playAudio2],
    name: "App",
    data() {
        return {
            dialogFormVisible: false,
            formLabelWidth: '250px',
            form: {
                name: '',
            },
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
            isChange: false,
            centerDialogVisible: false,
            textarea: ref(''),
            isLyricsShow: false,
            nowPlayMusic: null,
            isloaded: false,
            isShowDialog: true,
            table: false,
            dialog: false,
            loading: false,
            gridData: [],
            fileTemp: null,
            comment: [],
            has_lyric_in_item: false,
            nowMusicID: '',
        }
    },
    created() {
    },
    methods: {
        async confirmComplain() {
            if (this.form.name.length > 256) {
                alert("投诉内容过长，限制为256个字");
                return;
            }
            alert("投诉成功");
            await setComplain(this.nowPlayMusic.id, 'True', this.form.name);
        },
        async removeComment(index) {
            this.isloaded = false;
            var musicId = this.$route.params.musicId;
            await removeComment(store.state.loginUser.id, this.comment[index].id);
            var temp = await getComment(musicId);
            this.comment = [];
            for (let i = 0; i < temp.length; i++) {
                var commentUser = {
                    id: temp[i].user.uid,
                    img: "https://" + temp[i].user.icon_address,
                    name: temp[i].user.username,
                }
                const date = new Date(temp[i].created_at);
                const year = date.getFullYear();
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const day = String(date.getDate()).padStart(2, '0');
                const hours = String(date.getHours()).padStart(2, '0');
                const minutes = String(date.getMinutes()).padStart(2, '0');
                const seconds = String(date.getSeconds()).padStart(2, '0');
                const formattedDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
                const myVariable = formattedDateTime;
                var newComment = {
                    commentContent: temp[i].content,
                    comentUser: commentUser,
                    commentTime: myVariable,
                    id: temp[i].comment_id,
                }
                this.comment.push(newComment);
            }
            this.isloaded = true;
        },
        clickUserName(uid) {
            this.$router.push('/user/info/' + uid);
            this.isloaded = false;
            this.init();
        },
        mouseOutToChangeColor(id, color) {
            var ele = document.getElementById(id);
            ele.style.color = color;
        },
        mouseOverToChangeColor(id) {
            var ele = document.getElementById(id);
            ele.style.color = this.getColor;
        },
        async changeInfo() {
            this.isChange = false;
            var id = this.nowPlayMusic.id
            var name = this.nowPlayMusic.name
            var tag1 = this.nowPlayMusic.tag1
            var tag2 = this.nowPlayMusic.tag2
            var tag3 = this.nowPlayMusic.tag3
            var tag4 = this.nowPlayMusic.tag4
            var tag5 = this.nowPlayMusic.tag5
            await updateMusic(id, name, this.fileTemp, tag1, tag2, tag3, tag4, tag5);
        },
        handleFileChange(event) {
            this.fileTemp = document.getElementById('file-input').files[0];
            const file = event.target.files[0];
            const reader = new FileReader();
            reader.onload = (e) => {
                this.nowPlayMusic.coverPath = e.target.result;
            };
            reader.readAsDataURL(file);
        },
        addMusicToSongList(row) {
            this.centerDialogVisible = true;
            addSong(row.list_id, this.nowPlayMusic.id);
        },
        cancelForm() {
            this.loading = false
            this.dialog = false
        },
        addToMySongList() {
            this.table = true
        },
        toFavorMusic() {
            if (store.state.globalLogin == false) {
                this.$router.push('/login');
            }
            else
                favorMusic(store.state.loginUser.id, this.nowPlayMusic.id)
        },
        downloadFile(url) {
            if (store.state.loginUser == null)
                this.$router.push('/login');
            const urlParts = url.split('/');
            // const filename = urlParts[urlParts.length - 1];
            const filename = this.nowPlayMusic.name + ' - ' + this.nowPlayMusic.author;
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
        clickToPlayAudio(music) {
            this.playAudio1(music);
        },
        async init() {
            this.isloaded = false;
            var musicId = this.$route.params.musicId;
            this.nowPlayMusic = new Music(musicId);
            this.nowMusicID = musicId;
            this.isLyricsShow = false;
            await this.nowPlayMusic.initializeMusicInfo(musicId);
            this.has_lyric_in_item = this.nowPlayMusic.hasLyrics;
            if (this.nowPlayMusic.hasLyrics) {
                var temp1 = this.nowPlayMusic.lyricPath;
                var temp3 = this.nowPlayMusic.lyricCode;
                let temp2 = await get3(temp1, temp3);
            }
            this.gridData = await getUserAllSongList1();
            var temp = await getComment(musicId);
            for (let i = 0; i < temp.length; i++) {
                var commentUser = {
                    id: temp[i].user.uid,
                    img: "https://" + temp[i].user.icon_address,
                    name: temp[i].user.username,
                }
                const date = new Date(temp[i].created_at);
                const year = date.getFullYear();
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const day = String(date.getDate()).padStart(2, '0');
                const hours = String(date.getHours()).padStart(2, '0');
                const minutes = String(date.getMinutes()).padStart(2, '0');
                const seconds = String(date.getSeconds()).padStart(2, '0');
                const formattedDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
                const myVariable = formattedDateTime;
                var newComment = {
                    commentContent: temp[i].content,
                    comentUser: commentUser,
                    commentTime: myVariable,
                    id: temp[i].comment_id,
                }
                this.comment.push(newComment);
            }
            this.isloaded = true;
        },
        async sendComment() {
            this.isloaded = false;
            var musicId = this.$route.params.musicId;
            await addComment(store.state.loginUser.id, this.nowPlayMusic.id, this.textarea);
            var temp = await getComment(musicId);
            this.comment = [];
            for (let i = 0; i < temp.length; i++) {
                var commentUser = {
                    id: temp[i].user.uid,
                    img: "https://" + temp[i].user.icon_address,
                    name: temp[i].user.username,
                }
                const date = new Date(temp[i].created_at);
                const year = date.getFullYear();
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const day = String(date.getDate()).padStart(2, '0');
                const hours = String(date.getHours()).padStart(2, '0');
                const minutes = String(date.getMinutes()).padStart(2, '0');
                const seconds = String(date.getSeconds()).padStart(2, '0');
                const formattedDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
                const myVariable = formattedDateTime;
                var newComment = {
                    commentContent: temp[i].content,
                    comentUser: commentUser,
                    commentTime: myVariable,
                    id: temp[i].comment_id,
                }
                this.comment.push(newComment);
            }
            this.isloaded = true;
            this.textarea = ''
        },
        showAllLyrics() {
            this.isLyricsShow = true;
            var ele1 = document.getElementById('lyricsContent');
            var ele2 = document.getElementById('lyricsDiv');
            ele1.style.overflow = 'visible';
            ele2.style.overflow = 'visible';
            ele1.style.height = 'auto';
            ele2.style.height = 'auto';
            ele1.style.maxWidth = '1200px';
            ele2.style.maxWidth = '1250px';
        },
        nowShowAllLyrics() {
            this.isLyricsShow = false;
            var ele1 = document.getElementById('lyricsContent');
            var ele2 = document.getElementById('lyricsDiv');
            ele1.style.height = '300px';
            ele2.style.height = '350px';
            ele1.style.overflow = 'hidden';
            ele2.style.overflow = 'hidden';
            // ele1.style.overflowX = 'visible';
            // ele2.style.overflowX = 'visible';
            // ele1.style.overflowY = 'hidden';
            // ele2.style.overflowY = 'hidden';
        }
    },
    mounted() {
        this.init();
        setInterval(() => {
            var musicId = this.$route.params.musicId;
            if (this.nowMusicID != musicId)
                this.init();
        }, 50)
    },
    computed: {
        ...mapState(['loginUser', 'globalIsLoaded']),
        getColor() {
            return getComputedStyle(document.documentElement).getPropertyValue('--main-color');
        },
        filteredOptions() {
            // 创建一个数组，用于保存已选择的值
            const selectedValues = [
                this.nowPlayMusic.tag1,
                this.nowPlayMusic.tag2,
                this.nowPlayMusic.tag3,
                this.nowPlayMusic.tag4,
                this.nowPlayMusic.tag5,
                this.nowPlayMusic.tag6
            ];

            // 过滤选项，排除已选择的值
            return this.options.filter(option => !selectedValues.includes(option.value));
        }
    },
})
</script>
