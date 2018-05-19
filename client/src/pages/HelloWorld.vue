<template>
  <div class="hello">
      <router-link :to="{ name: 'additionalinfo' }" type="button" name="button"><button type="button" name="button">Non Nationwide Members</button></router-link>
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
      },
      user: {
        monthly_salary: '',
        savings: '',
        percent: '',
        waitmonths: ''
      }
    }
  },
  methods: {
    async getData (e) {
      e.preventDefault()
      const response = await NationService.getNationwide(this.form.id)
      this.user.monthly_salary = response.data.monthly_salary
      this.user.savings = response.data.savings
      this.user.percent = response.data.percent
      this.user.waitmonths = response.data.waitmonths
      this.$localStorage.set('user', JSON.stringify(this.user))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
