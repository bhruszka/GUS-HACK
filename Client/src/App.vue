<template>
  <div id="app">
      <nav class="level main-nav is-size-4 has-text-primary has-text-weight-bold">
        <p class="level-item has-text-centered">
          9GUS
        </p>
      </nav>
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<style lang="scss">
.main-nav {
  padding-top: 10px;
  padding-bottom: 10px;
}
</style>
