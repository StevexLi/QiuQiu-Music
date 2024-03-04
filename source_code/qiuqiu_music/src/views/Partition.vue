<template>
    <div v-if="this.isInitialization" style="position: fixed; top: 0; min-width: 1200px;width: 100%;height: 100%;">
        <div v-loading="this.isInitialization" element-loading-text="正在加载..."  style="height: 100%;width: 100%;"></div>
    </div>
    <div v-else>
        <el-row class="parent" style="min-height: 250px;height: 250px;top: 25px;">
            <div class="station" style="min-height: 250px;"></div>
            <div class="titleDiv">
                <el-row style="position: relative;;width: 100%;height: 10%;font-size: 18px;text-align: left;left: 5%;">语言</el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag1[0].value" class="tag" @click="this.changeTag(this.optiontag1[0].value)">{{ this.optiontag1[0].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag1[0].value)">{{ this.optiontag1[0].value }}</div>
                    <div v-if="this.keywords!=this.optiontag1[1].value" class="tag" @click="this.changeTag(this.optiontag1[1].value)">{{ this.optiontag1[1].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag1[1].value)">{{ this.optiontag1[1].value }}</div>
                    <div v-if="this.keywords!=this.optiontag1[2].value" class="tag" @click="this.changeTag(this.optiontag1[2].value)">{{ this.optiontag1[2].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag1[2].value)">{{ this.optiontag1[2].value }}</div>
                </el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag1[3].value" class="tag" @click="this.changeTag(this.optiontag1[3].value)">{{ this.optiontag1[3].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag1[3].value)">{{ this.optiontag1[3].value }}</div>
                    <div v-if="this.keywords!=this.optiontag1[4].value" class="tag" @click="this.changeTag(this.optiontag1[4].value)">{{ this.optiontag1[4].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag1[4].value)">{{ this.optiontag1[4].value }}</div>
                    <div v-if="this.keywords!=this.optiontag1[5].value" class="tag" @click="this.changeTag(this.optiontag1[5].value)">{{ this.optiontag1[5].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag1[5].value)">{{ this.optiontag1[5].value }}</div>
                </el-row>
            </div>
            <div class="split"></div>
            <div class="titleDiv">
                <el-row style="position: relative;;width: 100%;height: 10%;font-size: 18px;text-align: left;left: 5%;">流派</el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag2[0].value" class="tag" @click="this.changeTag(this.optiontag2[0].value)">{{ this.optiontag2[0].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag2[0].value)">{{ this.optiontag2[0].value }}</div>
                    <div v-if="this.keywords!=this.optiontag2[1].value" class="tag" @click="this.changeTag(this.optiontag2[1].value)">{{ this.optiontag2[1].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag2[1].value)">{{ this.optiontag2[1].value }}</div>
                    <div v-if="this.keywords!=this.optiontag2[2].value" class="tag" @click="this.changeTag(this.optiontag2[2].value)">{{ this.optiontag2[2].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag2[2].value)">{{ this.optiontag2[2].value }}</div>
                </el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag2[3].value" class="tag" @click="this.changeTag(this.optiontag2[3].value)">{{ this.optiontag2[3].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag2[3].value)">{{ this.optiontag2[3].value }}</div>
                    <div v-if="this.keywords!=this.optiontag2[4].value" class="tag" @click="this.changeTag(this.optiontag2[4].value)">{{ this.optiontag2[4].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag2[4].value)">{{ this.optiontag2[4].value }}</div>
                    <div v-if="this.keywords!=this.optiontag2[5].value" class="tag" @click="this.changeTag(this.optiontag2[5].value)">{{ this.optiontag2[5].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag2[5].value)">{{ this.optiontag2[5].value }}</div>
                </el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag2[6].value" class="tag" @click="this.changeTag(this.optiontag2[6].value)">{{ this.optiontag2[6].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag2[6].value)">{{ this.optiontag2[6].value }}</div>
                    <div v-if="this.keywords!=this.optiontag2[7].value" class="tag" @click="this.changeTag(this.optiontag2[7].value)">{{ this.optiontag2[7].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag2[7].value)">{{ this.optiontag2[7].value }}</div>
                    <div v-if="this.keywords!=this.optiontag2[8].value" class="tag" @click="this.changeTag(this.optiontag2[8].value)">{{ this.optiontag2[8].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag2[8].value)">{{ this.optiontag2[8].value }}</div>
                </el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag2[9].value" class="tag" @click="this.changeTag(this.optiontag2[9].value)">{{ this.optiontag2[9].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag2[9].value)">{{ this.optiontag2[9].value }}</div>
                </el-row>
            </div>
            <div class="split"></div>
            <div class="titleDiv">
                <el-row style="position: relative;;width: 100%;height: 10%;font-size: 18px;text-align: left;left: 5%;">主题</el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag3[0].value" class="tag" @click="this.changeTag(this.optiontag3[0].value)">{{ this.optiontag3[0].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag3[0].value)">{{ this.optiontag3[0].value }}</div>
                    <div v-if="this.keywords!=this.optiontag3[1].value" class="tag" @click="this.changeTag(this.optiontag3[1].value)">{{ this.optiontag3[1].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag3[1].value)">{{ this.optiontag3[1].value }}</div>
                    <div v-if="this.keywords!=this.optiontag3[2].value" class="tag" @click="this.changeTag(this.optiontag3[2].value)">{{ this.optiontag3[2].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag3[2].value)">{{ this.optiontag3[2].value }}</div>
                </el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag3[3].value" class="tag" @click="this.changeTag(this.optiontag3[3].value)">{{ this.optiontag3[3].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag3[3].value)">{{ this.optiontag3[3].value }}</div>
                    <div v-if="this.keywords!=this.optiontag3[4].value" class="tag" @click="this.changeTag(this.optiontag3[4].value)">{{ this.optiontag3[4].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag3[4].value)">{{ this.optiontag3[4].value }}</div>
                    <div v-if="this.keywords!=this.optiontag3[5].value" class="tag" @click="this.changeTag(this.optiontag3[5].value)">{{ this.optiontag3[5].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag3[5].value)">{{ this.optiontag3[5].value }}</div>
                </el-row>
            </div>
            <div class="split"></div>
            <div class="titleDiv">
                <el-row style="position: relative;;width: 100%;height: 10%;font-size: 18px;text-align: left;left: 5%;">心情</el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag4[0].value" class="tag" @click="this.changeTag(this.optiontag4[0].value)">{{ this.optiontag4[0].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag4[0].value)">{{ this.optiontag4[0].value }}</div>
                    <div v-if="this.keywords!=this.optiontag4[1].value" class="tag" @click="this.changeTag(this.optiontag4[1].value)">{{ this.optiontag4[1].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag4[1].value)">{{ this.optiontag4[1].value }}</div>
                    <div v-if="this.keywords!=this.optiontag4[2].value" class="tag" @click="this.changeTag(this.optiontag4[2].value)">{{ this.optiontag4[2].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag4[2].value)">{{ this.optiontag4[2].value }}</div>
                </el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag4[3].value" class="tag" @click="this.changeTag(this.optiontag4[3].value)">{{ this.optiontag4[3].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag4[3].value)">{{ this.optiontag4[3].value }}</div>
                </el-row>
            </div>
            <div class="split"></div>
            <div class="titleDiv">
                <el-row style="position: relative;;width: 100%;height: 10%;font-size: 18px;text-align: left;left: 5%;">场景</el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag5[0].value" class="tag" @click="this.changeTag(this.optiontag5[0].value)">{{ this.optiontag5[0].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[0].value)">{{ this.optiontag5[0].value }}</div>
                    <div v-if="this.keywords!=this.optiontag5[1].value" class="tag" @click="this.changeTag(this.optiontag5[1].value)">{{ this.optiontag5[1].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[1].value)">{{ this.optiontag5[1].value }}</div>
                    <div v-if="this.keywords!=this.optiontag5[2].value" class="tag" @click="this.changeTag(this.optiontag5[2].value)">{{ this.optiontag5[2].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[2].value)">{{ this.optiontag5[2].value }}</div>
                </el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag5[3].value" class="tag" @click="this.changeTag(this.optiontag5[3].value)">{{ this.optiontag5[3].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[3].value)">{{ this.optiontag5[3].value }}</div>
                    <div v-if="this.keywords!=this.optiontag5[4].value" class="tag" @click="this.changeTag(this.optiontag5[4].value)">{{ this.optiontag5[4].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[4].value)">{{ this.optiontag5[4].value }}</div>
                    <div v-if="this.keywords!=this.optiontag5[5].value" class="tag" @click="this.changeTag(this.optiontag5[5].value)">{{ this.optiontag5[5].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[5].value)">{{ this.optiontag5[5].value }}</div>
                </el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag5[6].value" class="tag" @click="this.changeTag(this.optiontag5[6].value)">{{ this.optiontag5[6].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[6].value)">{{ this.optiontag5[6].value }}</div>
                    <div v-if="this.keywords!=this.optiontag5[7].value" class="tag" @click="this.changeTag(this.optiontag5[7].value)">{{ this.optiontag5[7].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[7].value)">{{ this.optiontag5[7].value }}</div>
                    <div v-if="this.keywords!=this.optiontag5[8].value" class="tag" @click="this.changeTag(this.optiontag5[8].value)">{{ this.optiontag5[8].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[8].value)">{{ this.optiontag5[8].value }}</div>
                </el-row>
                <el-row>
                    <div v-if="this.keywords!=this.optiontag5[9].value" class="tag" @click="this.changeTag(this.optiontag5[9].value)">{{ this.optiontag5[9].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[9].value)">{{ this.optiontag5[9].value }}</div>
                    <div v-if="this.keywords!=this.optiontag5[10].value" class="tag" @click="this.changeTag(this.optiontag5[10].value)">{{ this.optiontag5[10].value }}</div>
                    <div v-else class="tag" style="color: #42b983;" @click="this.changeTag(this.optiontag5[10].value)">{{ this.optiontag5[10].value }}</div>
                </el-row>
            </div>
            <div class="station" style="min-height: 250px;"></div>
        </el-row>
        <el-row class="parent" style="margin-top: 50px;height: 30px;">
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
            <div class="lineDiv" style="width: 330px;font-size: 18px;text-align: left;">这个标签似乎没什么有，不如试试别的吧</div>
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
    </div>
    <div class="parent" style="height: 150px;"></div>
    <el-drawer v-model="table" title="选择添加到的歌单" direction="rtl" size="30%">
        <el-table :data="this.gripData" @row-click="addMusicToSong" style="cursor: pointer;">
            <el-table-column property="title" label="歌单名字" width="360px" />
        </el-table>
    </el-drawer>
</template>

<style scoped>
.split{
    position: relative;
    width: 1px;background-color: rgb(137, 163, 159);
    height: 90%;
    right: 10px;
}
.tag{
    position: relative;
    height: 50px;
    line-height: 50px;
    width: 30%;
}
.tag:hover{
    color: #42b983;
}
.titleDiv{
    position: relative;
    min-height: 250px;
    width: 16%;
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
import { getTagSong, getTagSongList} from '@/api/search';
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
            isInitialization: false,
            keywords: '国语',//标签
            totalPage: 0,
            count: 0,
            listOfSong: [],
            listOfSongList: [],
            isSong: true,
            uploaderName: [],
            likelist: [],
            pageNumber: [],
            searchKeywords: '',
            optiontag1:[
                {value: '国语', label: '国语'},//语言
                {value: '日语', label: '日语'},
                {value: '英语', label: '英语'},
                {value: '韩语', label: '韩语'},
                {value: '法语', label: '法语'},
                {value: '俄语', label: '俄语'},
            ],
            optiontag2:[
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
            ],
            optiontag3:[
                {value: 'ACG', label: 'ACG'},//主题
                {value: '经典', label: '经典'},
                {value: '古风', label: '古风'},
                {value: '情歌', label: '情歌'},
                {value: '佛教音乐', label: '佛教音乐'},
                {value: '网络歌曲', label: '网络歌曲'},
            ],
            optiontag4:[
                {value: '伤感', label: '伤感'},//心情
                {value: '安静', label: '安静'},
                {value: '治愈', label: '治愈'},
                {value: '励志', label: '励志'},
            ],
            optiontag5:[
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
        async changeTag(tag){
            this.isInitialization=true;
            this.keywords=tag;
            this.listOfSong=[];
            this.listOfSongList=[];
            this.uploaderName=[];
            this.pageNumber=[];
            this.$router.push('/partition/'+this.keywords);
            await this.changePageNum(1);
            this.isInitialization=false;
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
        playSong(item){
            this.playAudio1(item);
        },
        playSongList(item){
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
                console.log(err);
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
                data=await getTagSong(this.keywords,pageNum);
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
                data=await getTagSongList(this.keywords,pageNum);
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
            this.keywords=this.$route.params.tag;
            var data=await getTagSong(this.keywords,1);
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
        setInterval(async () => {
            var data=await getLikeList();
            this.checkLikeList(data.data.content);
            this.gripData = await getUserAllSongList1();
        }, 5000);
        this.initialization();
    }
}

</script>