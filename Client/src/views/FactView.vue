<template>
  <div class="container">
    <Fact v-if="fact != null" :fact="fact" />
    <div class="fb-comments" data-href="https://developers.facebook.com/docs/plugins/comments#configurator" data-width="100%" data-numposts="25"></div>
  </div>

</template>
<script>
import axios from "axios";
import Fact from "@/components/Fact.vue";
import config from "../config.js";

export default {
  data() {
    return {
      id: null,
      fact: null
    };
  },
  components: {
    Fact
  },
  mounted: function() {
    this.id = this.$route.params.id
    let self = this;
    axios
      .get(`${this.apiUrl}/api/facts/${this.id}/`)
      .then(function(response) {
        console.log(response.data);
        self.fact = response.data;
      })
      .catch(function(error) {});

    this.id = this.$route.params.id;
  },
  computed: {
    apiUrl: function() {
      return config.apiUrl;
    }
  }
};
</script>
<style>
</style>

