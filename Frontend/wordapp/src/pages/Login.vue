<template>
<div class="container">
  <h2>ログイン</h2>
  <form class="login-form">
    <div class="input-group">
      <label for="email">メールアドレス</label>
      <input type="email" id="email" v-model="email">
    </div>
    <div class="input-group">
      <label for="password">パスワード</label>
      <input type="password" id="password" v-model="password">
    </div>
    <div class="input-group">
      <b-button variant="primary" @click="login()">送信</b-button>
    </div>
  </form>
</div>
</template>

<script>
import axios from '../axios-for-auth.js'; //axiosのインスタンスをインポート
export default {
  data() {
    return {
      email: "",
      password: ""
    }
  },
  methods: {
    login() {//axiosでログイン用のインスタンスにアクセスするメソッドを定義
      axios.post( //エンドポイントのURLがログイン用のものを使う
        '/accounts:signInWithPassword?key=AIzaSyAnhZpWVg_cweTrgCMli-aQNbkhCo6zWNA',
        {
          email: this.email,//送る情報は新規登録と同じ
          password: this.password,
          returnSecureToken: true
        }
      ).then((response) => {
        this.$store.commit('updateIdToken', response.data.idToken) //追記
        this.$router.push('/'); //追記
      });
      this.email = "";
      this.password = "";
    }
  }
}
</script>

<style>
.input-group {
  margin: 5px;
  text-align: center;
}
</style>

