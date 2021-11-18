<template>
  <div>
    <div class="border square">
      <h1>{{ name }}</h1>
      <img src="@/assets/img/5084617_m.jpg" alt="#" class="rounded-circle face">
    </div>
    <div class="button">
    </div>
    <div>
      <div v-for="post in posts" v-bind:key="post">
        {{post}}
  </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      name: "",
      user_id: 0,
      posts: [],
      like: [],
    }
  },

  methods: {
    //ユーザー取得
    async getUserInfo() {
      const token = await this.$cookies.get('token')
      try {
        const response = await axios.get('http://localhost:5004/get',
                                {
                                  headers: {
                                    Authorization: `Bearer ${token}`,
                                  }
                                })
        console.log(response.data.user_name)
        this.name = response.data.user_name
        this.user_id = response.data.user_id

        this.getUserPosted()
      } catch(err) {
        console.log(err)
      }
      },
    //投稿取得
    async getUserPosted() {
      const token = await this.$cookies.get('token')
      console.log(token)
      try {
        //レスポンス取得
        const response = await axios.post('http://localhost:5004',
                             { user_id: this.user_id },
                             {
                                headers: {
                                    Authorization: `Bearer ${token}`,
                                }
                             })
        //ユーザー投稿データを代入
        const info = response.data.user_info
        //投稿データ数を代入
        const len = Object.keys(info).length
        //explanationsをpostsにいれる
        for (let i = 0; i< len; i ++) {
          this.posts.push(info[i].explanations)
        }

      } catch(err) {
        console.log(err)
      }
    }
  },

  mounted: function() {
    this.getUserInfo()
  }
}
</script>
<style>
.square {
  margin-right: 70%;
  background-color: red;
}
.face {
  width: 300px;
  height: 250px;
  margin-left: 30px;
}

</style>
