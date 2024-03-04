import axios from 'axios'
import store from "@/store"

var getdata='';
export async function post(url,newdata){
    await axios.post('http://8.130.25.189'+url,newdata).then(response=>{getdata=response.data});
    return getdata;
}

export async function get(url){
    await axios.get('http://8.130.25.189'+url).then(response=>{getdata=response.data});
    return getdata;
}

export async function get2(url,encoding){
    axios.defaults.withCredentials = true;
    axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
    // await axios.get(url).then(response=>{getdata=response.data});
    // var that = this;
    await axios({
        url: url,
        method: "get",
        responseType: 'blob'
    }).then(response=>{
        getdata = response.data;
    });
    // //console.log("getdata in get2:",getdata);
    let reader = new FileReader();
    let lyric="";
    reader.onload = function (e) {
        lyric = reader.result;
        let lyric2 = reader.result;
        store.commit('CHANGENOWPLAYINGLYRIC',lyric2);

        // store.state.globalLogin = true;
        ////console.log("lyric in get 2",lyric);
        // setTimeout(parseLrcString(lyric2),50);
        parseLrcString(lyric2);
    }
    reader.readAsText(getdata, encoding);
    return lyric;
}

export async function parseLrcString(lyric2) {
    let oLRC;
    oLRC = {
        ti: "", //歌曲名
        ar: "", //演唱者
        al: "", //专辑名
        by: "", //歌词制作人
        offset: 0, //时间补偿值，单位毫秒，用于调整歌词整体位置
        kana:"",
        ms: [] //歌词数组{t:时间,c:歌词}
    }
    //console.log("in create lrc:",oLRC);
    if(store.state.globalLyric.length===0) return;
    var lrcs = store.state.globalLyric.split('\n');//用回车拆分成数组
    for(var i in lrcs) {//遍历歌词数组
        lrcs[i] = lrcs[i].replace(/(^\s*)|(\s*$)/g, ""); //去除前后空格
        var t = lrcs[i].substring(lrcs[i].indexOf("[") + 1, lrcs[i].indexOf("]"));//取[]间的内容
        var s = t.split(":");//分离:前后文字
        if(isNaN(parseInt(s[0]))) { //不是数值
            for (var i in oLRC) {
                if (i != "ms" && i == s[0].toLowerCase()) {
                    oLRC[i] = s[1];
                }
            }
        }else { //是数值
            var arr = lrcs[i].match(/\[(\d+:.+?)\]/g);//提取时间字段，可能有多个
            var start = 0;
            for(var k in arr){
                start += arr[k].length; //计算歌词位置
            }
            var content = lrcs[i].substring(start);//获取歌词内容
            for (var k in arr){
                var t = arr[k].substring(1, arr[k].length-1);//取[]间的内容
                var s = t.split(":");//分离:前后文字
                if (content!=='')
                    oLRC.ms.push({//对象{t:时间,c:歌词}加入ms数组
                        t: (parseFloat(s[0])*60+parseFloat(s[1])).toFixed(3),
                        c: content
                    });
            }
        }
    }
    oLRC.ms.sort(function (a, b) {//按时间顺序排序
        return a.t-b.t;
    });

    for(var i in oLRC){ //查看解析结果
        //console.log(i,":",oLRC[i]);
    }

    store.commit('CHANGENOWPLAYINGLYRICSETS',oLRC);
}

export async function get3(url,encoding){
    var getdata3 = '';
    axios.defaults.withCredentials = true;
    axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
    // await axios.get(url).then(response=>{getdata=response.data});
    // var that = this;
    await axios({
        url: url,
        method: "get",
        responseType: 'blob'
    }).then(response=>{
        getdata3 = response.data;
    });
    // //console.log("getdata in get2:",getdata);
    let reader = new FileReader();
    let lyric="";
    reader.onload = function (e) {
        lyric = reader.result;
        let lyric2 = reader.result;
        store.commit('CHANGENOWPLAYINGLYRIC2',lyric2);

        // store.state.globalLogin = true;
        //console.log("lyric in get 3",lyric);
        // setTimeout(parseLrcString(lyric2),50);
        parseLrcString3(lyric2);
    }
    reader.readAsText(getdata3, encoding);
    return lyric;
}

export async function parseLrcString3(lyric2) {
    let oLRC;
    oLRC = {
        ti: "", //歌曲名
        ar: "", //演唱者
        al: "", //专辑名
        by: "", //歌词制作人
        offset: 0, //时间补偿值，单位毫秒，用于调整歌词整体位置
        kana:"",
        ms: [] //歌词数组{t:时间,c:歌词}
    }
    //console.log("in create lrc:",oLRC);
    if(store.state.globalLyric2.length===0) return;
    var lrcs = store.state.globalLyric2.split('\n');//用回车拆分成数组
    for(var i in lrcs) {//遍历歌词数组
        lrcs[i] = lrcs[i].replace(/(^\s*)|(\s*$)/g, ""); //去除前后空格
        var t = lrcs[i].substring(lrcs[i].indexOf("[") + 1, lrcs[i].indexOf("]"));//取[]间的内容
        var s = t.split(":");//分离:前后文字
        if(isNaN(parseInt(s[0]))) { //不是数值
            for (var i in oLRC) {
                if (i != "ms" && i == s[0].toLowerCase()) {
                    oLRC[i] = s[1];
                }
            }
        } else { //是数值
            var arr = lrcs[i].match(/\[(\d+:.+?)\]/g);//提取时间字段，可能有多个
            var start = 0;
            for(var k in arr){
                start += arr[k].length; //计算歌词位置
            }
            var content = lrcs[i].substring(start);//获取歌词内容
            for (var k in arr){
                var t = arr[k].substring(1, arr[k].length-1);//取[]间的内容
                var s = t.split(":");//分离:前后文字
                if (content!=='')
                    oLRC.ms.push({//对象{t:时间,c:歌词}加入ms数组
                        t: (parseFloat(s[0])*60+parseFloat(s[1])).toFixed(3),
                        c: content
                    });
            }
        }
    }
    oLRC.ms.sort(function (a, b) {//按时间顺序排序
        return a.t-b.t;
    });

    for(var i in oLRC){ //查看解析结果
        //console.log(i,":",oLRC[i]);
    }

    store.commit('CHANGENOWPLAYINGLYRICSETS2',oLRC);
}
