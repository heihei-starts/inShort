<template>
<div class="login">
  <div class="login-triangle"></div>
  
  <h2 class="login-header">Log in</h2>

  <p><input type="email" placeholder="Email" v-model="email"></p>
  <p><input type="password" placeholder="Password" v-model="password"></p>
  <p><input type="submit" value="Log in" @click="login()"></p>
</div>

</template>

<script>
import axios from 'axios'; //axiosのインスタンスをインポート
export default {
  data() {
    return {
      email: "",
      password: "",
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
        //location.reload()
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
@import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700);

body {
  background: #456;
  font-family: 'Open Sans', sans-serif;
}

.login {
  width: 400px;
  margin: 16px auto;
  font-size: 16px;
}

/* Reset top and bottom margins from certain elements */
.login-header,
.login p {
  margin-top: 0;
  margin-bottom: 0;
}

/* The triangle form is achieved by a CSS hack */
.login-triangle {
  width: 0;
  margin-right: auto;
  margin-left: auto;
  border: 12px solid transparent;
  border-bottom-color: #28d;
}

.login-header {
  background: #28d;
  padding: 20px;
  font-size: 1.4em;
  font-weight: normal;
  text-align: center;
  text-transform: uppercase;
  color: #fff;
}

.login-container {
  background: #ebebeb;
  padding: 12px;
}

/* Every row inside .login-container is defined with p tags */
.login p {
  padding: 12px;
}

.login input {
  box-sizing: border-box;
  display: block;
  width: 100%;
  border-width: 1px;
  border-style: solid;
  padding: 16px;
  outline: 0;
  font-family: inherit;
  font-size: 0.95em;
}

.login input[type="email"],
.login input[type="password"] {
  background: #fff;
  border-color: #bbb;
  color: #555;
}

/* Text fields' focus effect */
.login input[type="email"]:focus,
.login input[type="password"]:focus {
  border-color: #888;
}

.login input[type="submit"] {
  background: #28d;
  border-color: transparent;
  color: #fff;
  cursor: pointer;
}

.login input[type="submit"]:hover {
  background: #17c;
}

/* Buttons' focus effect */
.login input[type="submit"]:focus {
  border-color: #05a;
}
.input-group {
  margin: 5px;
  text-align: center;
}
</style>

