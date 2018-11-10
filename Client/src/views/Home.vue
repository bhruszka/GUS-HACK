<template>
  <div>
    <section class="hero has-background-white-ter main-hero">
      <div class="hero-body">
        <div class="container display-option-container">
          <div class="filter-container">
            <div class="level">
              <div class="level-item">
                <h2 class="subtitle">FILTER BY CATEGORY</h2>

              </div>
            </div>
            <div class="categories-container">
              <img v-for="c in categories" v-bind:key="c.id" :src="getImageUrl(c.id+1)" alt="img" class="category-pick-image" @click="filterCategorie = c.id" v-bind:class="{ greyed: filterCategorie != null && filterCategorie != c.id}">
            </div>
          </div>
          <div class="sort-container">
            <div class="level">
              <div class="level-item ">
                <h2 class="subtitle has-text-right">SORT BY</h2>
              </div>
            </div>
            <div style="width: 100%">
              <div class="buttons has-addons is-centered">
                <span class="button"><i class="mdi mdi-24px mdi-heart"></i></span>
                <span class="button"><i class="mdi mdi-24px mdi-emoticon-sad"></i></span>
                <span class="button is-success is-selected"><i class="mdi mdi-24px mdi-alert"></i></span>
                <span class="button"><i class="mdi mdi-24px mdi-school"></i></span>
              </div>
            </div>

            <div class="level" style="margin-top: 32px">
              <div class="level-item ">
                <h2 class="subtitle has-text-right">FACT TYPE</h2>
              </div>
            </div>
            <div style="width: 100%">
              <div class="buttons has-addons is-centered">
                <div class="select">
                  <select>
                    <option>All</option>
                    <option>Milestone</option>
                    <option>High vs Low</option>
                    <option>Progress</option>
                    <option>Charts</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <div class="container">
      <Fact v-for="fact in facts" :fact="fact" v-bind:key="fact.content" />
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
