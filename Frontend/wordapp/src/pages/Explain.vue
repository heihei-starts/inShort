<template>
  <div class="container">
    <div>
      <h1>単語</h1>
      <ul>
        <li>解説</li>
        <li>解説</li>
        <li>解説</li>
        <li>解説</li>
      </ul>
    </div>
    <br /><br /><br />
    <h2>解説投稿</h2>
    <b-form-textarea
      id="textarea"
      v-model="text"
      placeholder="Enter something..."
      rows="5"
      max-rows="10"
    ></b-form-textarea>
    <br /><br />
    <!-- <pre class="mt-3 mb-0">{{ text }}</pre> -->
    <b-button variant="primary" @click="post">投稿する</b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: "",
    };
  },
  methods: {
    post() {
      //解説をDBに登録
    },
  },
};
</script>
