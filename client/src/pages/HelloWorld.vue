<template>
  <div class="hello">
      <button type="button" name="button">Start</button>
    <form @submit="getData">
      <input v-model="form.id" type="text">
      <button type="submit" name="button">Nationwide</button>
    </form>
  </div>
</template>

<script>
import NationService from '@/services/Nationwide-Api'
export default {
  name: 'HelloWorld',
  data () {
    return {
      form: {
        id: ''
      }
    }
  },
  methods: {
    async getData (e) {
      e.preventDefault()
      const response = await NationService.getNationwide(this.form.id)
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
