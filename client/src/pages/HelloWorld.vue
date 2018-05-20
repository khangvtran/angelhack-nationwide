<template>
  <div class="hello">
      <router-link :to="{ name: 'start_button' }" type="button" name="button"><button type="button" name="button">Non Nationwide Members</button></router-link>
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
        id: null
      },
      user: {
        monthly_salary: null,
        savings: null
      }
    }
  },
  methods: {
    async getData (e) {
      e.preventDefault()
      const response = await NationService.getNationwide(this.form.id)
      this.user.monthly_salary = response.data.monthly_salary
      this.user.savings = response.data.savings
      this.$localStorage.set('user', JSON.stringify(this.user))
      this.$router.push({ name: 'additionalinfo' })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
