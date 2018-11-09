<template>
    <article class="fact-container media ">
        <div class="media-left">
            <figure class="image is-128x128">
                <img :src="categoryImage" class="category-image" alt="image">
            </figure>
        </div>
        <div class="media-content">
            <div class="content">
                <p>
                    {{fact.content}}
                    {{fact.content}}
                    {{fact.content}}
                    {{fact.content}}
                </p>
            </div>
        </div>

    </article>
</template>
<script>
import { getImageUrl } from "@/common/utility.js";

export default {
  props: ["fact"],
  computed: {
    // a computed getter
    categoryImage: function() {
      return getImageUrl(this.fact.category);
    }
  }
};
</script>
<style>
/* .fact-container {
  padding: 10px;
  border-bottom: 1px solid lightgrey;
  margin-bottom: 10px;
} */
</style>


