<template>
    <article class="fact-container media standard-padding" href="google.com">
        <div class="media-left">
            <figure class="image is-128x128">
                <img :src="categoryImage" class="category-image" alt="image">
            </figure>
        </div>
        <div class="media-content">
            <div class="content">
                <p class="is-size-5">
                    <a :href="'/fact/' + fact.id">
                        <i class="mdi mdi-12px mdi-more"></i>
                    </a>
                    <small> [{{fact.unit_parsed}}]</small>
                    <br>
                    {{fact.content}}
                </p>
                <nav class="level">
                    <div class="level-left">
                        <a class="level-item has-text-danger">
                            <span class="icon"><i class="mdi mdi-24px mdi-heart"></i></span>
                        </a>
                        <a class="level-item has-text-success">
                            <span class="icon"><i class="mdi mdi-24px mdi-emoticon-sad"></i></span>
                        </a>
                        <a class="level-item has-text-warning">
                            <span class="icon"><i class="mdi mdi-24px mdi-alert"></i></span>
                        </a>
                        <a class="level-item">
                            <span class="icon"><i class="mdi mdi-24px mdi-school"></i></span>
                        </a>
                    </div>
                    <div class="level-right has-text-link">
                        <div class="fb-share-button" :data-href="'/fact/' + fact.id" data-layout="button_count">
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
      return getImageUrl(this.fact.goal);
    }
  }
};
</script>
<style>
.fact-container {
  margin-top: 36px;
  margin-bottom: 36px;
  border-top: none !important;
}
</style>


