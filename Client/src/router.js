import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import FactView from "./views/FactView.vue";
import Random from "./views/Random.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/fact/:id",
      name: "fact",
      component: FactView
    },
    {
      path: "/random",
      name: "random",
      component: Random
    }
  ]
});
