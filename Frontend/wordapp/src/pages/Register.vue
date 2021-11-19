<template>
  <div class="container">
    <div class="Head">
      <h2 style="margin-top: 30px;">登録画面</h2>
    </div>
    <div class="form">
      <div class="form-middle">
        <div class="form-group">
          <input type="text" class="form-control"  name="name" placeholder="名前を入力してください。" style="margin-top: 40px;" v-model="name">
        </div>

        <div class="form-group">
          <input type="email" class="form-control" name="email" placeholder="メールアドレスを入力してください。" style="margin-top: 40px;" v-model="email">
        </div>

        <div class="form-group">
          <input type="password" class="form-control" name="password" placeholder="パスワードを入力してください。" style="margin-top: 40px;" v-model="password">
        </div>
          
      </div>

      <div class="form-bottom"> 
          <button type="submit" class="btn btn-outline-dark" style="margin-top: 30px;" @click="register()">登録</button>
      </div>
    </div>
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
