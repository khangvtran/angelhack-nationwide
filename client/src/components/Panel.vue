<template lang="html">
  <v-card class="elevation-6">
    <v-toolbar dense dark color="primary">
      <v-toolbar-title>{{ title }}</v-toolbar-title>

      <v-toolbar-items>
        <slot name="toolbar-item"></slot>
      </v-toolbar-items>
    </v-toolbar>

    <slot>No slot content defined.</slot>
  </v-card>
</template>

<script>
export default {
  name: 'Panel',
  props: [
    'title',
    'toolbar-item'
  ]
}
</script>

<style lang="css">
</style>
