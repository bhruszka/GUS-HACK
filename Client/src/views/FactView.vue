<template>
  <div>
    <h1> {{id}}</h1>
    <div class="fb-comments" data-href="https://developers.facebook.com/docs/plugins/comments#configurator" data-width="100%" data-numposts="25"></div>
  </div>

</template>
<script>
import Fact from "@/components/Fact.vue";

export default {
  data() {
    return { id: null };
  },
  components: {
    Fact
  },
  created: function() {

    this.id = this.$route.params.id;
  }
};
</script>
<style>
</style>

