<template>
  <div class="hello">
      <button type="button" name="button">Start</button>
      <button type="button" name="button">Nationwide</button>
    <form class="" action="index.html" method="post">
      <input type="text">
      <input type="text">
    </form>
  </div>
</template>

<script>
import NationService from '@/services/Nationwide-Api'
export default {
  name: 'HelloWorld',
  data () {
    return {
    }
  },
  methods: {
    async getData () {
      const response = await NationService.get()
      console.log(response)
    }
  },
  mounted () {
    this.getData()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
