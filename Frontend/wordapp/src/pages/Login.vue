<template>
  <div class="container">
    <h3 style="margin-top: 30px;">ログイン</h3>
    <div class="form-middle">
      <div class="form-group" style="margin-top: 30px;">
        <input type="email" class="form-control" name="email" placeholder="メールアドレスを入力してください。" v-model="email">
      </div>

      <div class="form-group" style="margin-top: 30px;">
        <input type="password" class="form-control" name="password" placeholder="パスワードを入力してください。" v-model="password">
      </div>

      <div class="form-bottom" style="margin-top: 30px;"> 
        <button type="submit" class="btn btn-outline-dark" @click="login()">ログイン</button>
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'; //axiosのインスタンスをインポート
export default {
  data() {
    return {
      email: "",
      password: "",
      logined: true
    }
  },

  methods: {
    async login() {
      try {
        const response = await axios.post( 
          'http://localhost:5002/login',
          {
            email: this.email,//送る情報は新規登録と同じ
            password: this.password,
          })
        console.log(response.data)
        const token = response.data.token
        console.log(token)

        this.$cookies.set('token', token)
        location.reload()
      } catch (err) {
        console.log(err)
        
      }
      /* .then((response) => { */
      /* this.$cookies.set('updateIdToken', response.data.idToken) //追記 */
      /* this.$router.push('/'); //追記 */
      /* }); */
      /* this.email = ""; */
      /* this.password = ""; */
    }
  }
}
</script>


<style>
</style>
