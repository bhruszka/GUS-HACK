<template>
    <div>
        <section class="hero has-background-grey-darker main-hero">
            <div class="hero-body">
                <div class="container">
                    <p class="title random-title has-text-white">
                        Get 20 <a class="button is-outlined is-link title random-button" @click="getFacts" v-bind:class="{ 'is-loading': isLoading}">RANDOM</a> facts
                    </p>
                </div>
            </div>
        </section>
        <div class="container facts-container">
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
  props: ["user"],
  components: {
    Fact
  },
  data() {
    return {
      facts: [],
      isLoading: true
    };
  },
  computed: {
    apiUrl: function() {
      return config.apiUrl;
    }
  },
  mounted: function() {
    this.getFacts();
  },
  methods: {
    getImageUrl: function(i) {
      return getImageUrl(i);
    },
    getFacts: function() {
      let self = this;
      this.isLoading = true;
      axios
        .get(`${this.apiUrl}/api/random_facts/20`)
        .then(function(response) {
          console.log(response.data);
          self.facts = response.data;
          self.isLoading = false;
        })
        .catch(function(error) {
          console.log("facts");
          console.log(error);
          self.isLoading = false;
        });
    }
  }
};
</script>


<style lang="scss">
.random-button {
  margin-left: 5px;
  margin-right: 5px;
}
.random-title {
  height: 72px;
  line-height: 72px !important;
}
</style>
