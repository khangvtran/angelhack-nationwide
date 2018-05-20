<template>
  <v-app id="app">
    <v-toolbar app flat dark class="light-blue">
      <v-toolbar-title>
        <router-link :to="{ name: 'HelloWorld' }">HouseFinder</router-link>
      </v-toolbar-title>
    </v-toolbar>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.toolbar__title a {
  color: white;
  text-decoration: none;
}
</style>
