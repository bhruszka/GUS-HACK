<template>
  <div>
    <section class="hero has-background-grey-darker main-hero">
      <div class="hero-body">
        <div class="container display-option-container">
          <div class="filter-container">
            <div class="level">
              <div class="level-item">
                <p class="subtitle has-text-white is-size-4">FILTER BY CATEGORY <i v-if="filterCategorie != null" class="mdi mdi-24px mdi-close has-text-danger" @click="filterCategorie = null"></i></p>
              </div>
            </div>
            <div class="categories-container">
              <img v-for="c in categories" v-bind:key="c.id" :src="getImageUrl(c.id+1)" alt="img" class="category-pick-image" @click="filterCategorie = c.id" v-bind:class="{ greyed: filterCategorie != null && filterCategorie != c.id}">
            </div>
          </div>
          <div class="sort-container">
            <div class="level">
              <div class="level-item ">
                <p class="subtitle has-text-right has-text-white is-size-4">SORT BY <i v-if="sort != null" class="mdi mdi-24px mdi-close has-text-danger" @click="sort = null"></i></p>
              </div>
            </div>
            <div style="width: 100%">
              <div class="buttons has-addons is-centered">
                <span class="button" @click="sort='love'" v-bind:class="{'is-danger is-selected': sort=='love'}"><i class="mdi mdi-24px mdi-heart"></i></span>
                <span class="button" @click="sort='sad'" v-bind:class="{'is-success is-selected': sort=='sad'}"><i class="mdi mdi-24px mdi-emoticon-sad"></i></span>
                <span class="button" @click="sort='alert'" v-bind:class="{'is-warning is-selected': sort=='alert'}"><i class="mdi mdi-24px mdi-alert"></i></span>
                <span class="button" @click="sort='edu'" v-bind:class="{'is-info is-selected': sort=='edu'}"><i class="mdi mdi-24px mdi-school"></i></span>
              </div>
            </div>

            <div class="level" style="margin-top: 32px">
              <div class="level-item ">
                <h2 class="subtitle has-text-right has-text-white is-size-4">FACT TYPE</h2>
              </div>
            </div>
            <div style="width: 100%">
              <div class="buttons has-addons is-centered">
                <div class="select is-size-5">
                  <select v-model="type">
                    <option class="is-size-5">All</option>
                    <option class="is-size-5">One data point</option>
                    <option class="is-size-5">New vs Old</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <div class="container facts-container">
      <Fact v-for="fact in facts" :fact="fact" v-bind:key="fact.content" />
      <nav class="pagination is-right" role="navigation" aria-label="pagination">
        <a class="pagination-previous">Previous</a>
        <a class="pagination-next">Next page</a>
        <ul class="pagination-list">
          <li v-if="page != 1"><a class="pagination-link" aria-label="Goto page 1" @click="page = 1">1</a></li>
          <li v-if="page - 2 > 1"><span class="pagination-ellipsis">&hellip;</span></li>
          <li v-if="page - 1 > 1"><a class="pagination-link" :aria-label="'Goto page ' + (page - 1)" @click="page = page -1">{{page - 1}}</a></li>
          <li><a class="pagination-link is-current" :aria-label="'Page ' + page" aria-current="page">{{page}}</a></li>
          <li v-if="page + 1 < totalPages"><a class="pagination-link" :aria-label="'Goto page ' + (page + 1)" @click="page = page + 1">{{page + 1}}</a></li>
          <li v-if="page + 2 < totalPages"><span class="pagination-ellipsis">&hellip;</span></li>
          <li v-if="page != totalPages"><a class="pagination-link" :aria-label="'Goto page' + totalPages" @click="page = totalPages">{{totalPages}}</a></li>
        </ul>
      </nav>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import config from "../config.js";
import { getImageUrl } from "@/common/utility.js";
import Fact from "@/components/Fact.vue";

export default {
  components: {
    Fact
  },
  data() {
    return {
      user: null,
      loginUrl: "/accounts/login",
      logoutUrl: "/accounts/logout",
      signupUrl: "/accounts/signup",
      categories: Array.from(new Array(17), (x, i) => ({ id: i })),
      filterCategorie: null,
      facts: [],
      type: "All",
      page: 1,
      totalPages: 1,
      sort: null
    };
  },
  computed: {
    apiUrl: function() {
      return config.apiUrl;
    }
  },
  watch: {
    filterCategorie: function(old_value, new_value) {
      this.page = 1;
      this.getFacts();
    },
    type: function(old_value, new_value) {
      this.page = 1;
      this.getFacts();
    },
    page: function(old_value, new_value) {
      this.getFacts();
    },
    sort: function(old_value, new_value) {
      this.page = 1;
      this.getFacts();
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

    this.getFacts();
  },
  methods: {
    getImageUrl: function(i) {
      return getImageUrl(i);
    },
    getFacts: function() {
      let self = this;

      let params = {
        params: {
          page: this.page,
          page_size: 20
        }
      };
      if (this.filterCategorie != null) {
        params.params.goal = this.filterCategorie + 1;
      }

      if(this.sort != null) {
        params.params.order_by = '-' + this.sort;
      }

      if (this.type != "All") {
        if (this.type == "One data point") {
          params.params.fact_type = "one_point";
        } else if (this.type == "New vs Old") {
          params.params.fact_type = "new_old";
        }
      }
      axios
        .get(`${this.apiUrl}/api/facts/`, params)
        .then(function(response) {
          console.log(response.data);
          self.facts = response.data.results;
          self.totalPages = response.data.total_pages;
          window.scrollTo(0, 0);
        })
        .catch(function(error) {
          console.log("facts");
          console.log(error);
        });
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
  border-bottom: 1px solid rgba(219, 219, 219, 0.5);
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
  height: 100px;
  margin: 0px;
}

.category-pick-image:hover {
  height: 140px;
  position: relative;
  margin: -20px;
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
}

.filter-container {
  width: 70%;
  padding-left: 8px;
  display: inline-block;
  max-width: 900px;
  flex-grow: 1;
}

.sort-container {
  width: 30%;
  padding-right: 8px;
  display: inline-block;
  min-width: 300px;
  flex-grow: 1;
}

.greyed {
  -webkit-filter: grayscale(98%);
  -moz-filter: grayscale(98%);
  -o-filter: grayscale(98%);
  -ms-filter: grayscale(98%);
  filter: grayscale(98%);
}

.display-option-container {
  display: flex;
  flex-wrap: wrap;
}

.container {
  max-width: 1000px !important;
}
</style>
