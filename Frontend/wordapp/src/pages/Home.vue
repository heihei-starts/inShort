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
export default {
  methods: {
    getWord() {
      return;
      //DBから検索した単語獲得
    },
  },
};
</script>

<style>
.container {
  text-align: center;
}
</style>
