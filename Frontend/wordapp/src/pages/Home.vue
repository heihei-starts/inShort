<template>
  <div class="container">
    <h2>Topページ</h2>
    <div class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="text" placeholder="Search" />
      <br />
      <b-button variant="outline-success" @click="getWord()"> Search </b-button>
      
      <!-- 単語一覧表示 -->
      <!-- DBの単語情報を表示  -->
    </div>
  </div>
</template>

<script>
import axios from "../axios-for-auth.js"; //axiosのインスタンスをインポート
// import axios from 'axios';
export default {
  //data追記
  data() {
    return {
      word_name: "",
      field_id: "",
      words:[]
    };
  },
  methods: {
    getWord() {
      axios.get("//localhost:5000")
      .then(response => {
        this.words = response.data.words
        console.log(response.data.words);
        //DBから検索した単語獲得
      }
      )
    },
  },
};
</script>
<style>
.container {
  text-align: center;
}
</style>
