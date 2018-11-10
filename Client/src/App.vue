<template>
  <div id="app">
    <nav class="level main-nav">
      <div class="level-item "></div>

      <p class="level-item has-text-centered is-size-4 has-text-primary has-text-weight-bold">
        9GUS
      </p>
      <div class="level-item" v-if="user != null">
        <p>
          {{user}}
        </p>
        <a class="button log-out-button" :href="logoutUrl">LOG OUT</a>
      </div>
      <div class="level-item" v-else>
        <a class="button log-in-button" :href="loginUrl">LOG IN</a>
        <a class="button sign-up-button is-danger has-text-weight-bold" :href="signupUrl">SIGN UP</a>
      </div>
    </nav>
    <section class="hero is-primary main-hero">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            Explore facts about sustainable development
          </h1>
          <h2 class="subtitle">
            Like and share what <b>YOU</b> think is important
          </h2>
        </div>
      </div>
    </section>
    <div class="container">
      <router-view />
    </div>
  </div>
</template>
<script>
import axios from "axios";
import config from "./config.js";

export default {
  data() {
    return {
      user: null,
      loginUrl: "/accounts/login",
      logoutUrl: "/accounts/logout",
      signupUrl: "/accounts/signup",
    };
  },
  computed: {
    apiUrl: function() { return config.apiUrl },
  },
  mounted: function() {
    let self = this;
    axios
      .get(`${this.apiUrl}/accounts/me`)
      .then(function(response) {
        console.log(response.data);
        self.user = response.data.username;
      })
      .catch(function(error) {
        console.log(error);
        self.user = null;
      });
  }
};
</script>


<style lang="scss">
.main-nav {
  padding-top: 10px;
  padding-bottom: 10px;
  margin-bottom: 0px !important;
}

.main-hero {
  margin-bottom: 16px;
}

.log-out-button {
  margin-left: 16px;
}

.sign-up-button {
  margin-left: 16px;
}
</style>
