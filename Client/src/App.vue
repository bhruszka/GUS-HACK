<template>
  <div id="app">
    <nav class="level main-nav is-size-4 has-text-primary has-text-weight-bold">
      <p class="level-item has-text-centered">
        9GUS
      </p>
    </nav>
    <section class="hero is-primary main-hero">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            Explore facts about sustainable development
          </h1>
          <h2 class="subtitle">
            Like and share what <b>YOU</b> think is important
          </h2>
        </div>
      </div>
    </section>
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<style lang="scss">
.main-nav {
  padding-top: 10px;
  padding-bottom: 10px;
  margin-bottom: 0px !important;
}

.main-hero {
  margin-bottom: 16px;
}
</style>
