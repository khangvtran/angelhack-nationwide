<template>
  <v-layout>
    <v-flex xs12 sm8 offset-sm2>
      <v-card>
        <v-toolbar dark color="primary">
          <v-toolbar-title>Start Planning!</v-toolbar-title>
        </v-toolbar>
        <v-card-actions>
          <v-btn :to="{ name: 'start_button' }" flat name="button">Non Nationwide Members</v-btn>
          <form @submit="getData">
            <input v-model="form.id" type="text">
            <v-btn flat type="submit" name="button">Nationwide</v-btn>
          </form>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
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
