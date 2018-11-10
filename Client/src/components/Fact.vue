<template>
    <article class="fact-container media standard-padding">
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
                <nav class="level">
                    <div class="level-left">
                        <a class="level-item">
                            <span class="icon"><i class="mdi mdi-24px mdi-heart"></i></span>
                        </a>
                        <a class="level-item">
                            <span class="icon"><i class="mdi mdi-24px mdi-emoticon-sad"></i></span>
                        </a>
                        <a class="level-item">
                            <span class="icon"><i class="mdi mdi-24px mdi-alert"></i></span>
                        </a>
                        <a class="level-item">
                            <span class="icon"><i class="mdi mdi-24px mdi-school"></i></span>
                        </a>
                    </div>
                    <div class="level-right">
                        <div class="fb-share-button" data-href="https://www.your-domain.com/your-page.html" data-layout="button_count">
                        </div>

                    </div>
                </nav>
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


