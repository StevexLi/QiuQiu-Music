<template>
    <div v-if="!isLoaded" style="position: fixed; top: 0; min-width: 1200px;width: 100%;height: 100%;">
        <div v-loading="!isLoaded" element-loading-text="正在加载..." style="height: 100%;width: 100%;"></div>
    </div>
    <div class="userLogined" v-if="isLoaded" style="min-width: 1200px;">
        <el-dialog v-model="centerDialogVisible" width="30%" center v-if="isSamePerson">
            <span>
                确定将改歌曲删除
            </span>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="isDelete = false">取消</el-button>
                    <el-button type="primary" @click="deleteSong(removeId)">
                        确定
                    </el-button>
                </span>
            </template>
        </el-dialog>
        <el-dialog v-model="centerDialogVisible" width="30%" center v-if="isSamePerson">
            <span>
                确定将选中歌曲从我喜欢音乐中删除
            </span>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="centerDialogVisible = false">取消</el-button>
                    <el-button type="primary" @click="removeLikeSong(removeId)">
                        确定
                    </el-button>
                </span>
            </template>
        </el-dialog>
        <div id="headContainer">
            <input type="file" id="file-input" style="display: none" @change="handleFileChange" v-if="isChange == true" />
            <label for="file-input" style="cursor: pointer;">
                <img :src='userIcon' id="userIon">
            </label>
            <span id="nameContainer">
                {{ userName }}
            </span>
            <button class="headerBotton" @click="addAttentionUser(nowVisitUser)" v-if="!isSamePerson && !isAttention">
                <span style="left: -5px;color: red;font-weight: 100;font-size: 25px;">
                    +
                </span>
                <span style="margin-left: 10px;font-weight: 100;">
                    关注
                </span>
            </button>
            <button class="headerBotton" @click="removeAttention" v-if="!isSamePerson && isAttention">
                <span style="left: -5px;font-weight: 100;font-size: 15px;">
                    √
                </span>
                <span style="margin-left: 10px;font-weight: 100;">
                    已关注
                </span>
            </button>
            <button class="headerBotton" style="width: 200px;" @click="changeuserInfo"
                v-if="isSamePerson && isChange == false">
                <img src="../../public/icon/changeInfoImg.png">
                <span style="margin-left: 10px;font-weight: 100; vertical-align: center;">
                    编辑个人信息
                </span>
            </button>
            <button class="headerBotton" style="width: 200px;" @click="changeInfo" v-if="isSamePerson && isChange == true">
                <img src="../../public/icon/changeInfoImg.png">
                <span style="margin-left: 10px;font-weight: 100; vertical-align: center;">
                    完成修改
                </span>
            </button>
            <button id="uploadSong" style="width: 200px;" @click="toUploadPage" v-if="isSamePerson">
                <span style="margin-left: 10px;font-weight: 100; vertical-align: center;">
                    上传歌曲
                </span>
            </button>
            <button id="uploadSong1" style="width: 200px;" @click="toUploadPage" v-if="!isSamePerson">
            </button>
            <hr id="lineInHead">
            <div id="UserIntroduction" v-if="!isChange">个人简介 ： {{ this.userIntroduction }}</div>
            <textarea id="UserChangeIntroduction" v-if="isChange == true" v-model="userIntroduction"></textarea>
        </div>
        <div id="nav">
            <span class="myListSpan" id="myList" @mousemove="mouseOverToChangeColor('myList')"
                @mouseout="mouseOutToChangeColor('myList')" @click="mouseClickToChangeColor('myList')">我的歌单</span>
            <span class="myListSpan" id="uploadList" @mousemove="mouseOverToChangeColor('uploadList')"
                @mouseout="mouseOutToChangeColor('uploadList')" @click="mouseClickToChangeColor('uploadList')">上传歌曲</span>
            <span class="myListSpan" id="likeList" @mousemove="mouseOverToChangeColor('likeList')"
                @mouseout="mouseOutToChangeColor('likeList')" @click="mouseClickToChangeColor('likeList')">喜欢歌曲</span>
            <span class="myListSpan" id="attentionUserList" @mousemove="mouseOverToChangeColor('attentionUserList')"
                @mouseout="mouseOutToChangeColor('attentionUserList')"
                @click="mouseClickToChangeColor('attentionUserList')">关注用户</span>
            <span class="myListSpan" id="messageSpan" @mousemove="mouseOverToChangeColor('messageSpan')"
                @mouseout="mouseOutToChangeColor('messageSpan')" @click="mouseClickToChangeColor('messageSpan')">消息</span>
        </div>
        <div>
            <img src="../../public/icon/nothing.png"
                v-if="(nowVisitUser.attentionUser.length == 0 && nowElementSpan == 'attentionUserList') || (nowVisitUser.shareSongList.length == 0 && nowElementSpan == 'myList') || (nowVisitUser.uploadList.length == 0 && nowElementSpan == 'uploadList') || (nowVisitUser.likeList.length == 0 && nowElementSpan == 'likeList')">
            <br>
            <div style="height: 150px;font-size: 20px;color: rgba(0, 0, 0, 0.5);"
                v-if="(nowVisitUser.attentionUser.length == 0 && nowElementSpan == 'attentionUserList') || (nowVisitUser.shareSongList.length == 0 && nowElementSpan == 'myList') || (nowVisitUser.uploadList.length == 0 && nowElementSpan == 'uploadList') || (nowVisitUser.likeList.length == 0 && nowElementSpan == 'likeList') || (messageList.length == 0 && nowElementSpan == 'messageSpan')">
                什么也没有,去
                <router-link to="/" style="color: var(--main-color);">音乐馆</router-link><router-view />发现好音乐
            </div>
        </div>
        <div class="contentSpan" v-if="nowElementSpan == 'attentionUserList' && nowVisitUser.attentionUser.length != 0">
            <div class="itemSpan" v-for="(attentionUserTemp, index) in nowVisitUser.attentionUser" :key="index">
                <img :src="attentionUserTemp.icon" :id="'userPic' + index" class="userPic">
                <br>
                <span>
                    <span :id="'userRouter' + index" style="color: black;text-decoration: none;"
                        @mouseover="mouseOverToChangeColor('userRouter' + index)"
                        @mouseout="mouseOutToChangeColor('userRouter' + index)" @click="reload(attentionUserTemp.id)">{{
                            attentionUserTemp.name }}
                    </span><router-view />
                </span>
            </div>
        </div>
        <div class="contentSpan" v-if="nowElementSpan == 'likeList' && nowVisitUser.likeList.length != 0"
            style="flex-direction: column;display: flex;width: 100%;">
            <div class="itemDiv">
                <div class="itemSpanNum">序号</div>
                <div class="itemSpanOpe">操作</div>
                <div class="itemSpanMusic">标题</div>
                <div class="itemSpanSinger">歌手</div>
            </div>
            <div style="margin-top: -8px;">
                <div class="itemDiv" v-for="(item, index) in nowVisitUser.likeList" :key="index">
                    <div style="height: 100%; width: 100%; background-color: #e1e3e3;flex-direction: row;display: flex;"
                        v-if="index % 2 == 0">
                        <div class="itemSpanNum" style="color: black;cursor: pointer;" :id="'itemNum' + index"
                            @mouseover="mouseOverToChangeColor('itemNum' + index)"
                            @mouseout="mouseOutToChangeColor('itemNum' + index)">{{ index + 1 }}</div>
                        <div class="itemSpanOpe" style="color: black; " :id="'itemDownload' + index">
                            <el-icon style="cursor: pointer;" @click="downloadFile(item.musicPath)">
                                <Download />
                            </el-icon>
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
        <div class="contentSpan" v-if="nowElementSpan == 'uploadList' && nowVisitUser.uploadList.length != 0"
            style="flex-direction: column;display: flex;width: 100%;">
            <div class="itemDiv">
                <div class="itemSpanNum">序号</div>
                <div class="itemSpanOpe">操作</div>
                <div class="itemSpanMusic">标题</div>
                <div class="itemSpanSinger">歌手</div>
            </div>
            <div style="margin-top: -8px;">
                <div class="itemDiv" v-for="(item, index) in nowVisitUser.uploadList" :key="index">
                    <div style="height: 100%; width: 100%; background-color: #e1e3e3;flex-direction: row;display: flex;"
                        v-if="index % 2 == 0">
                        <div class="itemSpanNum" style="color: black;cursor: pointer;" :id="'itemNum' + index"
                            @mouseover="mouseOverToChangeColor('itemNum' + index)"
                            @mouseout="mouseOutToChangeColor('itemNum' + index)">{{ index + 1 }}</div>
                        <div class="itemSpanOpe" style="color: black; " :id="'itemDownload' + index">
                            <el-icon style="cursor: pointer;" @click="downloadFile(item.musicPath)">
                                <Download />
                            </el-icon>
                            <el-icon style="cursor: pointer;" @click="deleteSong(item.id)" v-if="nowVisitUser.id == loginUser.id">
                                <DeleteFilled />
                            </el-icon>
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
                            <el-icon style="cursor: pointer;" @click="deleteSong(item.id)"
                                v-if="nowVisitUser.id == loginUser.id">
                                <DeleteFilled />
                            </el-icon>
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
        <div class="contentSpan" v-if="nowElementSpan == 'myList' && nowVisitUser.shareSongList.length != 0">
            <div class="itemSpan" v-for="(attentionUserTemp, index) in nowVisitUser.shareSongList" :key="index">
                <img :src="attentionUserTemp.cover" :id="'userPic' + index" class="userPic">
                <br>
                <span>
                    <router-link :to="'/user/songList/' + attentionUserTemp.id" :id="'userRouter' + index"
                        style="color: black;text-decoration: none;"
                        @mouseover="mouseOverToChangeColor('userRouter' + index)"
                        @mouseout="mouseOutToChangeColor('userRouter' + index)" v-if="showRouterView">{{
                            attentionUserTemp.title }}
                    </router-link><router-view />
                </span>
            </div>
        </div>
        <!-- <div class="contentSpan" v-if="nowElementSpan == 'messageSpan' && messageList.length != 0"
            style="flex-direction: column;">
            <div class="itemDiv" v-for="(item, index) in messageList" :key="index" style="flex-direction: column;">
                <div style="height: 100%; width: 100%; background-color: #e1e3e3;flex-direction: row;display: flex;"
                    v-if="index % 2 == 0">
                    <span class="itemSpanNum" style="width: 700px;background-color: red;">
                        {{ item.message }}
                    </span>
                    <span class="itemSpanNum" style="width: 500px;background-color: red;">
                        {{ item.created_at }}
                    </span>
                    <br>
                </div>
                <div style="height: 100%; width: 100%;flex-direction: row;display: flex;" v-if="index % 2 == 1">
                    <span class="itemSpanNum" style="width: 700px;background-color: green;">
                        {{ item.message }}
                    </span>
                    <span class="itemSpanNum" style="width: 500px;background-color: green;">
                        {{ item.created_at }}
                    </span>
                    <br>
                </div>
            </div>
        </div> -->
        <div class="contentSpan" v-if="nowElementSpan == 'messageSpan' && messageList.length != 0"
            style="flex-direction: column;display: flex;width: 100%;">
            <div>
                <div class="itemDiv" v-for="(item, index) in messageList" :key="index">
                    <div style="height: 100%; width: 100%; background-color: #e1e3e3;flex-direction: row;display: flex;"
                        v-if="index % 2 == 0">
                        <span class="itemSpanNum" style="width: 700px;">
                            {{ item.message }}
                        </span>
                        <span class="itemSpanNum" style="width: 500px;">
                            {{ item.created_at }}
                        </span>
                    </div>
                    <div style="height: 100%; width: 100%;flex-direction: row;display: flex;" v-if="index % 2 == 1">
                        <span class="itemSpanNum" style="width: 700px;">
                            {{ item.message }}
                        </span>
                        <span class="itemSpanNum" style="width: 500px;">
                            {{ item.created_at }}
                        </span>
                    </div>
                </div>
            </div>
        </div>

    </div>
    <div style="height: 300px;"></div>
    <div class="userLogined" v-if="globalIsLoaded == false">
        123456
        <button @click="testLoaded(true)"></button>
    </div>
</template>
<style scoped>
:root {
    --main-color: #42b983;
}

#uploadSong {
    position: relative;
    margin-left: 20px;
    top: -143px;
    height: 50px;
    width: 200px;
    border-radius: 10%;
    border-width: 1px;
    border-color: gray;
    cursor: pointer;

}

#uploadSong1 {
    position: relative;
    margin-left: 20px;
    top: -143px;
    height: 50px;
    width: 200px;
    border: 0;
    background-color: transparent;
}

.itemSpanOpe {
    color: #757776;
    display: flex;
    width: 100px;
    height: 50px;
    align-items: center;
    justify-content: center;
    margin-left: 60px;
}

.itemSpanMusic {
    color: #757776;
    display: flex;
    width: 300px;
    height: 50px;
    align-items: center;
    justify-content: center;
    margin-left: 100px;
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

.itemSpanNum {
    color: #757776;
    display: flex;
    width: 100px;
    height: 50px;
    align-items: center;
    justify-content: center;
    margin-left: 30px;
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

.itemDiv {
    display: flex;
    height: 50px;
    width: 1200px;
}

#nav {
    height: 100px;
    width: 80%;
    margin-left: 10%;
    display: flex;
    align-items: center;
    margin-top: 50px;
}

.myListSpan {
    height: 70%;
    width: 100px;
    margin-left: 1%;
    cursor: pointer;
}

#userIon {
    position: relative;
    height: 200px;
    width: 200px;
    border-radius: 50%;
    margin-left: 3%;
    margin-top: 80px;
}

#nameContainer {
    position: relative;
    display: inline-block;
    height: 60px;
    line-height: 60px;
    color: white;
    width: 200px;
    margin-left: 4%;
    top: -36%;
    font-size: 30px;
    font-weight: bolder;
    overflow: hidden;
    background: rgba(0, 0, 0, 0.5);
}

#headContainer {
    display: inline-block;
    position: relative;
    width: 100%;
    height: 400px;
    background-image: url('../assets/userbackground.jpg');
    background-size: 100% 100%;
}

#lineInHead {
    width: 100px;
    position: relative;
    margin-top: -8.5%;
    margin-left: 28%;
    width: 68%;
}

.headerBotton {
    position: relative;
    margin-left: 20%;
    top: -140px;
    height: 50px;
    width: 200px;
    border-radius: 10%;
    border-width: 1px;
    border-color: gray;
    cursor: pointer;
}

#UserIntroduction {
    height: 100px;
    width: 600px;
    position: relative;
    left: 28%;
    text-align: left;
    margin-top: 10px;
    font-weight: 100;
    color: white;
    background: rgba(0, 0, 0, 0.5);
}

#UserChangeIntroduction {
    border: 0;
    border-radius: 5px;
    background-color: rgba(221, 215, 215, 0.98);
    padding: 10px;
    resize: none;
    height: 80px;
    width: 600px;
    position: relative;
    left: 0%;
    text-align: left;
    margin-top: 10px;
    font-weight: 100;
    color: gray;
    vertical-align: top;
}

#nameChangeContainer {
    position: relative;
    display: inline-block;
    height: 60px;
    width: 300px;
    left: 8%;
    top: -50%;
    font-size: 40px;
    font-weight: bolder;
    border-width: 100;
    border-radius: 10px;
    border-color: rgb(242, 242, 242);
    background-color: rgb(242, 242, 242);
}

.itemSpan {
    height: 200px;
    width: 200px;
}

.contentSpan {
    position: relative;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 10px;
    min-height: 800px;
    width: 80%;
    left: 10%;
}

.userPic {
    height: 150px;
    width: 150px;
    border-radius: 50%;
}

.dialog-footer button:first-child {
    margin-right: 10px;
}
</style>
<script>
import store from "@/store";
import User from "@/components/User";
import { KinesisContainer, KinesisElement } from "vue-kinesis";
import { ref } from 'vue';
import { mapState } from 'vuex';
import { postAttentionUser } from '../api/User'
import { removeAttentionUser } from '../api/User'
import { changeUsernfo } from '../api/User'
import { removeFavorMusic } from '../api/music'
import download from 'downloadjs';
import { Download } from '@element-plus/icons';
import { DeleteFilled } from '@element-plus/icons';
import { VideoPlay } from '@element-plus/icons';
import {getNotification} from '../api/message'
import {deleteMusic } from '../api/music'
export default {
    name: "App",
    components: {
        KinesisContainer,
        KinesisElement,
        Download,
        DeleteFilled,
        VideoPlay
    },
    data() {
        return {
            isDelete : false,
            userIcon: null,
            userName: null,
            userIntroduction: null,
            nowVisitUser: null,
            isChange: false,
            nowElementSpan: 'myList',
            isAttention: false,
            attentionUser: ref([]),
            isNowContentEmpty: false,
            centerDialogVisible: ref(false),
            removeId: '',
            isLoaded: false,
            intervalId: null,
            fileTemp: null,
            showRouterView: true,
            messageList: [
                {
                    message: '您关注的用户CodingKirby分享了新的歌曲哦！快去围观一下吧！',
                    created_at: '2023-05-25T18:45:31.049'
                },
                {
                    message: '您关注的用户CodingKirby分享了新的歌曲哦！快去围观一下吧！',
                    created_at: '2023-05-25T18:45:31.049'
                }
            ],
            deleteId : null,
        }
    },
    watch: {
        'store.state.loginUser'(newValue, oldValue) {
            this.nowVisitUser = newValue;
        },
        $route(to, from) {

        },
    },
    created() {
    },
    methods: {
        playMusic(music)
        {
            this.playAudio1(music.id);
        },
        deleteSong(id){
            this.isDelete = true;
            this.deleteId = id;
        },
        
        toUploadPage() {
            this.$router.push('/upLoadSong');
        },
        async reload(id) {
            this.isLoaded = false;
            this.$router.push('/user/info/' + id);
        },
        changeuserInfo() {
            clearInterval(this.intervalId);
            this.isChange = true;
        },
        toMusicPage(music) {
            this.$router.push('/music/' + music.id)
        },
        toRemoveLikeSong(music) {
            this.centerDialogVisible = true;
            this.removeId = music.id;
        },
        async temp(uid) {
            clearInterval(this.intervalId);
            var newUser = new User(uid);
            await newUser.initializeUserInfo(uid);
            var response = await getNotification();
            this.messageList = response.data;
            for(let i = 0;i < this.messageList.length;i++)
            {
                const date = new Date(this.messageList[i].created_at);
                const year = date.getFullYear();
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const day = String(date.getDate()).padStart(2, '0');
                const hours = String(date.getHours()).padStart(2, '0');
                const minutes = String(date.getMinutes()).padStart(2, '0');
                const seconds = String(date.getSeconds()).padStart(2, '0');
                const formattedDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
                const myVariable = formattedDateTime;
                this.messageList[i].created_at = myVariable
            }
            this.nowVisitUser = newUser;
            var newUser1 = new User(store.state.loginUser.id);
            await newUser1.initializeUserInfo(store.state.loginUser.id);
            store.commit('updateLoginUser', newUser1);
            var newArray = store.state.loginUser.attentionUser.filter(item => item.id == this.nowVisitUser.id);
            if (newArray.length == 0)
                this.isAttention = false;
            else
                this.isAttention = true;

            this.isNowContentEmpty = (this.nowVisitUser.songList.length == 0);
            this.userIcon = this.nowVisitUser.icon
            this.userName = this.nowVisitUser.name
            this.userIntroduction = this.nowVisitUser.introduction
            this.intervalId = setInterval(async () => {
                var newUser = new User(this.nowVisitUser.id);
                await newUser.initializeUserInfo(this.nowVisitUser.id);
                this.nowVisitUser = newUser;
            }, 5000);
            this.isLoaded = true;
            var element = document.getElementById(this.nowElementSpan);
            element.style.color = this.getColor;
        },
        async init() {
            var uid = this.$route.params.uid;
            var response = await getNotification();
            this.messageList = response.data;
            for(let i = 0;i < this.messageList.length;i++)
            {
                const date = new Date(this.messageList[i].created_at);
                const year = date.getFullYear();
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const day = String(date.getDate()).padStart(2, '0');
                const hours = String(date.getHours()).padStart(2, '0');
                const minutes = String(date.getMinutes()).padStart(2, '0');
                const seconds = String(date.getSeconds()).padStart(2, '0');
                const formattedDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
                const myVariable = formattedDateTime;
                this.messageList[i].created_at = myVariable
            }
            var newUser = new User(uid);
            await newUser.initializeUserInfo(uid);
            this.nowVisitUser = newUser;
            var newUser1 = new User(store.state.loginUser.id);
            await newUser1.initializeUserInfo(store.state.loginUser.id);
            store.commit('updateLoginUser', newUser1);
            var newArray = store.state.loginUser.attentionUser.filter(item => item.id == this.nowVisitUser.id);
            if (newArray.length == 0)
                this.isAttention = false;
            else
                this.isAttention = true;

            this.isNowContentEmpty = (this.nowVisitUser.songList.length == 0);
            this.userIcon = this.nowVisitUser.icon
            this.userName = this.nowVisitUser.name
            this.userIntroduction = this.nowVisitUser.introduction
            this.intervalId = setInterval(async () => {
                var newUser = new User(this.nowVisitUser.id);
                await newUser.initializeUserInfo(this.nowVisitUser.id);
                this.nowVisitUser = newUser;
            }, 3000);
            this.isLoaded = true;
            var element = document.getElementById(this.nowElementSpan);
            element.style.color = this.getColor;
        },
        testLoaded(value) {
            store.commit('updateIsLoaded', true);
        },
        async changeInfo() {
            this.isChange = false;
            this.nowVisitUser.icon = this.userIcon;
            this.nowVisitUser.name = this.userName;
            this.nowVisitUser.introduction = this.userIntroduction;
            store.commit('updateLoginUser', this.nowVisitUser);
            await changeUsernfo(store.state.loginUser.id, store.state.loginUser.name, store.state.loginUser.introduction, this.fileTemp);
            this.intervalId = setInterval(async () => {
                var newUser = new User(this.nowVisitUser.id);
                await newUser.initializeUserInfo(this.nowVisitUser.id);
                this.nowVisitUser = newUser;
            }, 5000);
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
        async removeLikeSong(id) {
            this.centerDialogVisible = false;
            await removeFavorMusic(store.state.loginUser.id, id);
        },
        removeAttention() {
            removeAttentionUser(store.state.loginUser.id, this.nowVisitUser.id);
            var newArray = store.state.loginUser.attentionUser.filter(item => item.id != this.nowVisitUser);
            store.state.loginUser.attentionUser = newArray;
            store.commit('updateLoginUser', store.state.loginUser);
            this.isAttention = false;
        },
        indexofUser(user) {
            var newArray = store.state.loginUser.attentionUser.filter(item => item.id == user.id)
            if (newArray.length == 0)
                return false;
            return true;
        },
        addAttentionUser(user) {
            this.isAttention = true;
            if ((this.indexofUser(user)) == true)
                return;
            postAttentionUser(store.state.loginUser.id, user.id);
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
        handleFileChange(event) {
            this.fileTemp = document.getElementById('file-input').files[0];
            const file = event.target.files[0];
            const reader = new FileReader();
            reader.onload = (e) => {
                this.userIcon = e.target.result;
            };
            reader.readAsDataURL(file);
        },
        getImgUrl: function (t) {
            return require('@/assets/img/' + t);
        },
        judgeContentEmpty() {
            if (this.nowElementSpan == 'myList') {
                if (this.nowVisitUser.songList.length == 0)
                    this.isNowContentEmpty = true;
                else this.isNowContentEmpty = false;
            }
            else if (this.nowElementSpan == 'uploadList') {
                if (this.nowVisitUser.uploadList.length == 0)
                    this.isNowContentEmpty = true;
                else this.isNowContentEmpty = false;

            }
            else if (this.nowElementSpan == 'likeList') {
                if (this.nowVisitUser.likeList.length == 0)
                    this.isNowContentEmpty = true;
                else this.isNowContentEmpty = false;
            }
            else if (this.nowElementSpan == 'attentionUserList') {
                if (this.nowVisitUser.attentionUser.length == 0)
                    this.isNowContentEmpty = true;
                else this.isNowContentEmpty = false;
            }
        },

    },
    computed: {
        ...mapState(['loginUser', 'globalIsLoaded']),
        isSamePerson() {
            return this.nowVisitUser.id == store.state.loginUser.id;
        },
        getColor() {
            return getComputedStyle(document.documentElement).getPropertyValue('--main-color');
        },

    },
    mounted() {
        if(store.state.globalLogin==false){
            this.$router.push('/login');
        }
        else{
            this.init();
        }
    }
};
</script>
