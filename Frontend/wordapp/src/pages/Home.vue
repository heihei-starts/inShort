<template>
  <div class="container">
    <h2>Topページ</h2>
    <div class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="text" placeholder="Search" />
      <br />
      <b-button variant="outline-success"> 用語検索 </b-button>
      <ul style="list-style: none;">
        <li v-for="word in words" :key="word.word_name">
          <router-link to="/explain" style="text-decoration: none; color: black;" @click.native="setWordId(word.id, word.word_name)">{{word.word_name}}</router-link>
        </li>
      </ul>
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
    async getWord() {
      try {
        const response = await axios.get("//localhost:5000")
        console.log(response.data.words)
        const info = response.data.words
        const len = Object.keys(info).length
        console.log(len)
        console.log(info[0].field_id)
        for (let i = 0; i< len; i ++) {
          this.words.push({'id': info[i].id, 'field_id': info[i].field_id, 'word_name': info[i].word_name})
        }
      } catch(err) {
        console.log(err)
      }
        

    },
    setWordId(word_id, word_name) {
      this.$cookies.set('word_id', word_id)
      this.$cookies.set('word_name', word_name)
    }

  },
  mounted: function() {
    this.getWord()
  }
};
</script>
<style>
.container {
  text-align: center;
}
</style>
