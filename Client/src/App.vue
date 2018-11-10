<template>
  <div id="app">
    <div id="fb-root"></div>
    <div class="has-background-black-ter has-text-white	">
      <nav class="level main-nav container">
        <div class="level-left standard-padding">
          <div class="level-item is-size-4 has-text-weight-bold">
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
    <router-view/>
  </div>
</template>
<script>
import axios from "axios";
import config from "./config.js";
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
      facts: [
        {
          content: "Szotuka była dyscypliną olimpijską od 1912 do 1948 roku",
          category: 1
        },
        {
          content:
            "10% ze wszystkich zdjęć istniejących na świecie zostało zrobione w ciągu ostatnich 12 miesięcy",
          category: 2
        },
        {
          content:
            "Co 10 mieszkaniec Centralnej Azji jest potomkiem Czyngis-chana",
          category: 1
        },
        {
          content:
            "W pewnej austriackiej wiosce znaki drogowe zrobione są z cementu, by zapobiec kradzieży",
          category: 3
        },
        {
          content:
            "Istnieje trzy razy większe ryzyko, że umrzemy w katastrofie lotniczej, niż zostaniemy zaatakowani przez pumę",
          category: 1
        },
        {
          content:
            "Jeśli rocznie zarabiasz więcej niż 64.000 złotych to należysz do 4% najbogatszych ludzi na świecie",
          category: 2
        },
        {
          content:
            "Kiedy „Mona Liza” została ukradziona z Luwru w 1911 roku, jednym z podejrzanych był Pablo Picasso",
          category: 4
        },
        {
          content:
            "W dniu urodzin ryzyko śmierci jest 14% większe niż w jakikolwiek inny dzień",
          category: 3
        },
        {
          content:
            "W książce Jerome K. Jerome „Trzech panów w łódce” pierwsze zdanie brzmi „Było nas czterech",
          category: 1
        },
        {
          content:
            "Ponad 7000 osób umiera, a 1.5 miliona ma problemy zdrowotne spowodowane nieczytelnym pismem lekarzy",
          category: 2
        },
        { content: "Większość diamentów ma ponad 3 miliardy lat", category: 4 },
        {
          content: "Co 10 dziecko w Europie zostało poczęte w łóżku z IKEA",
          category: 3
        }
      ]
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
  height: 90px;
  margin: 0px;
}

.category-pick-image:hover {
  height: 140px;
  position: relative;
  margin: -25px;
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
</style>
