<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <a class="navbar-brand" href="#">In_Short</a>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/" class="nav-link" aria-current="page">トップ</router-link>
            </li>
            <li class="nav-item">
              <template v-if="checkLogined">
                <a @click="logout()" class="nav-link" aria-current="page">ログアウト</a>
              </template>
              <template v-else>
               <router-link to="/login" class="nav-link" aria-current="page">ログイン</router-link>
              </template>
            </li>
            <li class="nav-item">
              <template v-if="checkLogined">
                <router-link to="/user" class="nav-link" aria-current="page">ユーザー画面</router-link> 
              </template>
            </li>
            <li>
              <router-link to="/register" class="nav-link" aria-current="page">新規登録</router-link>
            </li>
          </ul>
          <form class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
    }
  },

  computed: {
    //ログインしてるか確認
    checkLogined() {
      if (this.$cookies.isKey('token')) {
        return true 
      } else {
       return false 
      }
    }
  },

  methods: {
    logout() {
      this.$cookies.remove('token')
      location.reload()
    }
  }

}
</script>

<style>
.header {
  text-align: center;
  display: flex;
  justify-content: center;
}
.header--link {
  padding: 10px;
}

.board {
  margin-top: 10px;
  margin-left: 20px;
}

</style>
