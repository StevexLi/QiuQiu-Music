<template>
  <div class="userNoLogin">
    <img src="../../public/background.png" id="background">
    <div class="glass-container" id="glass"></div>
    <kinesis-container id="textContainer">
      <kinesis-element :strength="20" class="textContent"> 这里还是一片荒漠 </kinesis-element>
      <kinesis-element :strength="20" class="textContent"> 您还未登录 </kinesis-element>
      <kinesis-element :strength="20" class="textContent"> 管理我的音乐实现同步 </kinesis-element>
    </kinesis-container>
    <button id="loginButton" @click="changeLoginStatus">点击登录</button>
  </div>
</template>
<style>
:root {
  --main-color: #42b983;
}

#background {
  position: absolute;
  left: 0px;
  height: 606px;
  width: 1481px;
}

#loginButton {
  position: absolute;
  height: 50px;
  width: 120px;
  top: 80%;
  left: 45%;
  background-color: var(--main-color);
  color: white;
  border: 0;
  border-radius: 8px;
  cursor: pointer;
}

.glass-container {
  position: absolute;
  width: 1481px;
  height: 606px;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  border-radius: 10px;
  backdrop-filter: blur(4px);
  background-color: rgba(4, 0, 255, 0.105);
  box-shadow: rgba(0, 0, 0, 0.3) 2px 8px 8px;
  border: 2px rgba(255, 255, 255, 0.4) solid;
  border-bottom: 2px rgba(40, 40, 40, 0.35) solid;
  border-right: 2px rgba(40, 40, 40, 0.35) solid;
}

#textContainer {
  position: absolute;
  top: 20%;
  left: 35%;
  height: 200px;
  width: 400px;
  text-align: center;
}

.textContent {
  margin-top: 20%;
  font-size: 40px;
  font-family: 'YourChosenFont', cursive;
  color: white;
  font-weight: bolder;
}
</style>
<script>
import User from "@/components/User";
import { KinesisContainer, KinesisElement } from "vue-kinesis";
import store from '../store'
import router from '../router'
export default {
  name: "App",
  components: {
    KinesisContainer,
    KinesisElement,
  },
  data() {
    return {
      nowLoginUser: null,
    }
  },
  watch: {
    nowLoginUser(newValue) {
      store.commit('updateLoginUser', newValue);
    },
    'store.state.loginUser'(newValue) {
      this.nowLoginUser = newValue;
    },
  },
  methods: {
    changeLoginStatus() {
      this.nowLoginUser = store.state.testUserList[1];
      store.commit('updateLoginUser',this.nowLoginUser);
      store.commit('updateVisitUser',this.nowLoginUser);
      this.$router.push({ name: 'userLogined', params: { uid: this.nowLoginUser.id } });
    },
  }
};
</script>
