<template>
    <div v-if="this.isInitialization" style="position: fixed; top: 0; min-width: 1200px;width: 100%;height: 100%;">
        <div v-loading="this.isInitialization" element-loading-text="正在上传歌曲..."  style="height: 100%;width: 100%;"></div>
    </div>
    <el-container v-else style="min-width: 1200px;height: 100%;width: 100%;">
        <button class="back" @click="this.jump()" style="width: 150px;height: 40px;font-size: 18px;margin-left: 10%;margin-top: 25px;">返回个人页面</button>
        <el-header class="formHeader">
            上传歌曲 &nbsp&nbsp&nbsp~&nbsp&nbsp&nbsp Ye dala &nbsp&nbsp&nbsp~
        </el-header>
        <el-main>
            <el-form :model="songData" status-icon :rules="rules" ref="songData" label-width="100px" class="form">
                <el-row class="parent">
                    <el-form-item label="歌曲名称" maxlength="25" prop="title" class="formLabel">
                        <el-input v-model="songData.title" class="formInput"></el-input>
                    </el-form-item>
                </el-row>
                <el-row class="parent">
                    <el-form-item label="创作歌手" maxlength="15" class="formLabel">
                        <el-input maxlength="32" v-model="songData.singerName" class="formInput"></el-input>
                    </el-form-item>
                </el-row>
                <el-row class="parent">
                    <el-form-item label="标签" prop="tag0" class="formLabel">
                        <el-select style="width: 200px;" v-model="songData.tag[0]" placeholder="歌曲标签" @change="checkTag()"> 
                            <el-option v-for="item in tag.optiontag" :key="item.value" :value="item.value">{{ item.label }}</el-option>
                        </el-select>
                    </el-form-item>
                </el-row>
                <el-row v-if="tag.istag[0]" class="parent">
                    <el-form-item prop="tag1" class="formLabel">
                        <el-select style="width: 200px;" v-model="songData.tag[1]" placeholder="歌曲标签" @change="checkTag()"> 
                            <el-option v-for="item in tag.optiontag" :key="item.value" :value="item.value">{{ item.label }}</el-option>
                        </el-select>
                    </el-form-item>
                </el-row>
                <el-row v-if="tag.istag[1]" class="parent">
                    <el-form-item prop="tag2" class="formLabel">
                        <el-select style="width: 200px;" v-model="songData.tag[2]" placeholder="歌曲标签" @change="checkTag()"> 
                            <el-option v-for="item in tag.optiontag" :key="item.value" :value="item.value">{{ item.label }}</el-option>
                        </el-select>
                    </el-form-item>
                </el-row>
                <el-row v-if="tag.istag[2]" class="parent">
                    <el-form-item prop="tag3" class="formLabel">
                        <el-select style="width: 200px;" v-model="songData.tag[3]" placeholder="歌曲标签" @change="checkTag()"> 
                            <el-option v-for="item in tag.optiontag" :key="item.value" :value="item.value">{{ item.label }}</el-option>
                        </el-select>
                    </el-form-item>
                </el-row>
                <el-row v-if="tag.istag[3]" class="parent">
                    <el-form-item prop="tag4" class="formLabel">
                        <el-select style="width: 200px;" v-model="songData.tag[4]" placeholder="歌曲标签" @change="checkTag()"> 
                            <el-option v-for="item in tag.optiontag" :key="item.value" :value="item.value">{{ item.label }}</el-option>
                        </el-select>
                    </el-form-item>
                </el-row>
                <el-row v-if="tag.istag[4]" class="parent">
                    <el-form-item prop="tag5" class="formLabel">
                        <el-select style="width: 200px;" v-model="songData.tag[5]" placeholder="歌曲标签" @change="checkTag()"> 
                            <el-option v-for="item in tag.optiontag" :key="item.value" :value="item.value">{{ item.label }}</el-option>
                        </el-select>
                    </el-form-item>
                </el-row>
                <el-row class="parent">
                    <el-form-item label="上传歌曲" ref="file" prop="song" class="formLabel">
                        <el-input type="file" v-model="songData.songAddress" style="width: 70%;" id="song"></el-input>
                    </el-form-item>
                </el-row>
                <el-row class="parent">
                    <el-form-item label="上传歌词" prop="lyric" class="formLabel">
                        <el-input type="file" v-model="songData.lyricAddress" style="width: 70%;" id="lyric"></el-input>
                    </el-form-item>
                </el-row>
                <el-row class="parent">
                    <el-form-item label="上传封面" prop="cover" class="formLabel">
                        <el-input type="file" v-model="songData.coverAddress" style="width: 70%;" id="cover"></el-input>
                    </el-form-item>
                </el-row>
                <el-row class="parent">
                    <el-form-item label="歌曲介绍"  class="formLabel">
                        <el-input type="textarea" maxlength="1024" show-word-limit=true :autosize="{ minRows: 2, maxRows: 7 }" v-model="songData.introduction" class="formInput"></el-input>
                    </el-form-item>
                </el-row>
                <el-row class="parent">
                    <el-form-item class="formLabel">
                        <el-button type="success" class="formInput" @click="submitForm('songData')" style="left: 10%;width: 60%;">上传歌曲</el-button>
                    </el-form-item>
                </el-row>
            </el-form>
        </el-main>
    </el-container>
    <div class="parent" style="height: 150px;"></div>
</template>

<style scoped>
.back:hover{
  color:  #42b983;
}
.parent{
  justify-content: center;
}
.formHeader{
  position: relative;
  top: 35px;
}
.form{
  position: relative;
  width: 100%;
}
.formLabel{
  position: relative;
  width: 600px;
}
.formInput{
    position: relative;
    width: 90%;
}
.formButton{
  position: relative;
}

</style>

<script>
import store from '@/store';
import { upLoadSong } from "../api/song";
import { ElMessage } from 'element-plus';

export default{
    data(){
        var checkTitle=(rule, value, callback)=>{
            if (value=== '') {
                callback(new Error('请输入歌曲名称'));
            }
            else{
                if(this.code!=0){
                    this.code=0;
                    callback(new Error(this.message));
                }
                callback()
            }
        };
        var checkTags=(rule,value,callback)=>{
            var i,j,k;
            for(i=5;i>0;i--){
                if(this.songData.tag[i]==='') continue;
                else{
                    for(j=0;j<i;j++){
                        if(this.songData.tag[i]==this.songData.tag[j]) callback(new Error('不能选择重复Tag'));
                    }
                }
            }
            if(this.songData.tag[0]==='') callback(new Error('请至少选择一个标签'));
            callback();
        };
        var checkSong=(rule,value,callback)=>{
            var song=this.songData.songAddress.substring(this.songData.songAddress.lastIndexOf('.'));
            if(song=='.mp3'||song=='.flac'||song=='.wma'||song=='.wav'||song=='.ape'||song=='.ogg'||song=='.acc'){
                callback();
            }
            else if(this.songData.songAddress===''){
                callback(new Error('本文件不能为空'));
            }
            else{
                callback(new Error('该文件类型不支持'));
            }
        };
        var checkLyric=(rule,value,callback)=>{
            var lyric=this.songData.lyricAddress.substring(this.songData.lyricAddress.lastIndexOf('.'));
            if(lyric=='.lrc'||lyric==''){
                callback();
            }
            else{
                callback(new Error('该文件类型不支持'));
            }
        };
        var checkCover=(rule,value,callback)=>{
            var cover=this.songData.coverAddress.substring(this.songData.coverAddress.lastIndexOf('.'));
            if(cover=='.png'||cover=='.jpg'||cover=='.jpeg'||cover=='.bmp'||cover==''){
                callback();
            }
            else{
                callback(new Error('该文件类型不支持'));
            }
        };
        return {
            songData: {
                title: '',
                singerName: '',
                introduction: '',
                songAddress: '',
                lyricAddress: '',
                coverAddress: '',
                tag: new Array('','','','','',''),
            },
            tag:{
                istag: new Array(false,false,false,false,false,false),
                optiontag:[
                    {value: '', label: '歌曲标签', },
                    {value: '国语', label: '国语'},//语言
                    {value: '日语', label: '日语'},
                    {value: '英语', label: '英语'},
                    {value: '韩语', label: '韩语'},
                    {value: '法语', label: '法语'},
                    {value: '俄语', label: '俄语'},
                    {value: '流行', label: '流行'},//流派
                    {value: '摇滚', label: '摇滚'},
                    {value: '电子', label: '电子'},
                    {value: '爵士', label: '爵士'},
                    {value: '民谣', label: '民谣'},
                    {value: '古典', label: '古典'},
                    {value: '重金属', label: '重金属'},
                    {value: '嘻哈', label: '嘻哈'},
                    {value: '蓝调', label: '蓝调'},
                    {value: '轻音乐', label: '轻音乐'},
                    {value: 'ACG', label: 'ACG'},//主题
                    {value: '经典', label: '经典'},
                    {value: '古风', label: '古风'},
                    {value: '情歌', label: '情歌'},
                    {value: '佛教音乐', label: '佛教音乐'},
                    {value: '网络歌曲', label: '网络歌曲'},
                    {value: '伤感', label: '伤感'},//心情
                    {value: '安静', label: '安静'},
                    {value: '治愈', label: '治愈'},
                    {value: '励志', label: '励志'},
                    {value: '校园', label: '校园'},//场景
                    {value: '咖啡馆', label: '咖啡馆'},
                    {value: '工作', label: '工作'},
                    {value: '婚礼', label: '婚礼'},
                    {value: '约会', label: '约会'},
                    {value: '开车', label: '开车'},
                    {value: '运动', label: '运动'},
                    {value: '夜店', label: '夜店'},
                    {value: '睡前', label: '睡前'},
                    {value: '派对', label: '派对'},
                    {value: '学习', label: '学习'},
                ]
            },
            rules:{
                title: [{validator: checkTitle, trigger: 'blur'}],
                tag0: [{validator: checkTags, trigger: 'change'}],
                tag1: [{validator: checkTags, trigger: 'change'}],
                tag2: [{validator: checkTags, trigger: 'change'}],
                tag3: [{validator: checkTags, trigger: 'change'}],
                tag4: [{validator: checkTags, trigger: 'change'}],
                tag5: [{validator: checkTags, trigger: 'change'}],
                song: [{validator: checkSong, trigger: 'change'}],
                lyric: [{validator: checkLyric, trigger: 'change'}],
                cover: [{validator: checkCover, trigger: 'change'}],
            },
            code: 0,
            message: null,
            isInitialization: false,
        }
    },
    methods: {
        jump(){
            this.$router.push('/user/info/'+store.state.globalUserID);
        },
        submitForm(formName){
            this.$refs[formName].validate(async (valid)=>{
                if(valid){
                    this.isInitialization=true;
                    var file1=document.getElementById('song').files[0];
                    var file2=document.getElementById('lyric').files[0];
                    var file3=document.getElementById('cover').files[0];
                    var data=await upLoadSong(this.songData.title,this.songData.singerName,this.songData.introduction,file1,file2,file3,this.songData.tag);
                    this.code=data['code'];
                    this.message=data['msg'];
                    if(this.code!=0){
                        this.isInitialization=false;
                        ElMessage({
                            message: data.msg,
                            type: error,
                        });
                        this.code=0;
                    }
                    else{
                        this.isInitialization=false;ElMessage({
                            message: '上传歌曲成功！',
                            type: 'success',
                        });
                        this.isInitialization=false;
                        this.songData.title='';
                        this.songData.singerName='';
                        this.songData.introduction='';
                        this.songData.songAddress='';
                        this.songData.lyricAddress='';
                        this.songData.coverAddress='';
                        this.songData.tag=new Array('','','','','','');
                    }
                }
            });
        },
        checkTag(){
            var count=new Array(1,1,1,1,1,1);
            var i,j,k;
            for(i=0;i<6;i++){
                if(this.songData.tag[i]==='') count[i]=0;
            }
            j=0;
            k=0;
            for(i=0;i<6;i++){
                if(count[i]==0){
                    for(j=i+1;j<6;j++){
                        if(count[j]==1){
                            k=j;
                            break;
                        }
                    }
                    if(k>i){
                        for(j=i;k<6;j++,k++){
                            this.songData.tag[j]=this.songData.tag[k];
                            count[j]=count[k];
                        }
                        for(;j<6;j++){
                            count[j]=0;
                        }
                    }
                }
                if(count[i]==0) this.tag.istag[i]=false;
                else this.tag.istag[i]=true;
            }
        },
    },
    mounted(){
        if(store.state.globalLogin==false){
            this.$router.push('/')
        }
    }
}

</script>