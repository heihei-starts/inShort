<template>
  <div>
    <div class="border square">
      <img src="@/assets/img/5084617_m.jpg" alt="#" class="rounded-circle face">
    </div>
    <div class="button">
      <button type="button" class="btn btn-secondary">投稿</button>
      <button type="button" class="btn btn-success">いいね</button>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      name: "",
      posts: [],
      like: [],
    }
  },

  methods: {
    //投稿取得
    async getUserPosted() {
     // const token = await this.$cookies.get('token')
      //try {
        //const reponse = await axios.post('http://localhost:5004',
          //                                { })
      //}
    }
  }
}
</script>
<style>
.square {
  margin-right: 950px;
  background-color: blue;
}
.face {
  width: 300px;
  height: 250px;
  margin-left: 30px;
}

</style>
