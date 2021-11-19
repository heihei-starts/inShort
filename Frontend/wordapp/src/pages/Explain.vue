<template>
  <div class="container">
    <div>
      <h1 v-if="matchName">{{name}}</h1>
      <ul v-for="explanation in explanations" :key="explanation.id">
        {{ matchName() }}
        <li>{{ explanation.explanation }}</li>
      </ul>
    </div>
    <br /><br /><br />
    <h2>解説投稿</h2>
    <template v-if="checkLogined">
      <b-form-textarea
        id="textarea"
        v-model="text"
        placeholder="Enter something..."
        rows="5"
        max-rows="10"
      ></b-form-textarea>
      <br /><br />
      <!-- <pre class="mt-3 mb-0">{{ text }}</pre> -->
      <b-button variant="primary" @click="getExplanation">投稿する</b-button>
    </template>
    <template v-else>
      <p style="color: gray;">(投稿するにはログインが必要です。)</p>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      name: "",
      text: "",
      id: 0,
      explanations:[]
    };
  },
  computed: {
    checkLogined() {
      if (this.$cookies.isKey('token')) {
        return true
      } else {
        return false
      }
    },
  },
  methods: {
    async getExplanation(id) {
      //解説をDBに登録
      try {
        const response = await axios.post(
              'http://localhost:5001',
              {
                word_id: id
              })
        console.log(response.data.explanations)

        const info = response.data.explanations
        const len = Object.keys(info).length
        console.log(len)

        for (let i = 0; i< len; i ++) {
          this.explanations.push({'explanation': info[i].explanations, 'user_id': info[i].user_id, 'word_id': info[i].word_id, 'good': info[i].good})
        }
      } catch (err) {
        console.log(err)
      }  
    },

    getId(id) {
      this.id = id
      console.log(this.id)
    },
    wordName(name) {
      this.name = name
      console.log(this.name)
    },
    matchName() {
      if (this.$cookies.get('word_name') != this.name) {
        location.reload()
        console.log(this.name)
      }
    }

  },
  mounted: function() {
    console.log(this.$cookies.get('word_name'))
    this.wordName(this.$cookies.get('word_name'))
    this.getId(this.$cookies.get('word_id'))
    this.getExplanation(this.id)
  }
};
</script>
