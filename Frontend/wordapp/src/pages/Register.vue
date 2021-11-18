<template>
  <div class="container">
    <h2>新規登録</h2>
    <form class="login-form">
      <div class="input-group">
        <label for="name">名前</label>
        <input type="name" id="name" v-model="name" />
      </div>
      <div class="input-group">
        <label for="email">メールアドレス</label>
        <input type="email" id="email" v-model="email" />
      </div>
      <div class="input-group">
        <label for="password">パスワード</label>
        <input type="password" id="password" v-model="password" />
      </div>
      <div class="input-group">
        <b-button variant="primary" @click="register()">新規登録</b-button>

      </div>
    </form>
  </div>
</template>

<script>
import axios from "../axios-for-auth.js"; //axiosのインスタンスをインポート
export default {
  data() {
    return {
      name: "",
      email: "",
      password: "",
    };
  },
  methods: {
    register() {
      //axiosでapiを叩くメソッドを定義
      axios
        .post("http://localhost:5002/register", {
          name: this.name,
          email: this.email,
          password: this.password,
        })
        .then((response) => {
          console.log(response)
          this.$router.push("/login"); //追記
        });
      this.email = "";
      this.password = "";
    },
  },
};
</script>
