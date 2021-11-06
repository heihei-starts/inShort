<template>
  <div class="container">
    <h2>マイページ</h2>
    <p>ログインが必要なページ</p>
    <b-button variant="danger" @click="logout()">ログアウト</b-button>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$store.commit('updateIdToken', null);
      this.$router.push('/login');
    }
  }
}
</script>
