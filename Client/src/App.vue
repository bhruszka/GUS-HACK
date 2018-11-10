<template>
  <div id="app">
    <div class="container">
      <nav class="level main-nav">
        <div class="level-left standard-padding">
          <div class="level-item is-size-4 has-text-primary has-text-weight-bold">
            <p>9GUS</p>
          </div>
        </div>
        <div class="level-right standard-padding">
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
        </div>
      </nav>
    </div>
    <section class="hero is-primary main-hero">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            Explore facts about sustainable development
          </h1>
          <h2 class="subtitle">
            Like and share what <b>YOU</b> think is important
          </h2>
          <h2>FILTER BY CATEGORY</h2>
          <div class="categories-container">
            <img v-for="c in categories" v-bind:key="c.id" :src="getImageUrl(c.id+1)" alt="img" class="category-pick-image">
          </div>
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
import { getImageUrl } from "@/common/utility.js";

export default {
  data() {
    return {
      user: null,
      loginUrl: "/accounts/login",
      logoutUrl: "/accounts/logout",
      signupUrl: "/accounts/signup",
      categories: Array.from(new Array(17), (x, i) => ({id: i})),
      filterCategorie: null
    };
  },
  computed: {
    apiUrl: function() {
      return config.apiUrl;
    }
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
  },
  methods: {
    getImageUrl: function(i) {
      return getImageUrl(i);
    }
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

@media only screen and (max-width: 1070px) {
  .standard-padding {
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
  }
}

.category-pick-image {
  height: 96px;
  -webkit-filter: grayscale(100%);
  -moz-filter: grayscale(100%);
  -o-filter: grayscale(100%);
  -ms-filter: grayscale(100%);
  filter: grayscale(100%);
  margin: 0px;
}

.category-pick-image:hover {
  height: 128px;
  position: relative;
  margin: -16px;
  -webkit-filter: none;
  -moz-filter: none;
  -o-filter: none;
  -ms-filter: none;
  filter: none;
  z-index: 9;
}

.categories-container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 50%;
}
</style>
