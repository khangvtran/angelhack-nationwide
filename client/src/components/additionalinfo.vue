<template>
  <form @submit.prevent="submitHandler">
    <label for="percent">Percent of month income you want to set aside for a home</label>
    <input type="number" name="percent" id="percent" v-model="user.percent" required>
    <label for="wait_months">How long do you want to wait until you buy a home? (Months)</label>
    <input type="number" name="waitmonths" id="waitmonths" v-model="user.wait_months" required>
    <label for="mortgage_years">How long do you want your mortgage to be? (Years)</label>
    <input type="number" name="mortgage_years" id="mortgage_years" v-model="user.mortgage_years" required>
    <input type="submit" name="submit" value="submit">
  </form>
</template>

<script scoped>
import NationService from '@/services/Nationwide-Api'
export default {
  data () {
    return {
      user: {
        monthly_salary: JSON.parse(this.$localStorage.get('user')).monthly_salary,
        savings: JSON.parse(this.$localStorage.get('user')).savings,
        percent: null,
        wait_months: null,
        mortgage_years: null
      }
    }
  },
  methods: {
    async submitHandler (e) {
      e.preventDefault()
      this.$localStorage.set('user', JSON.stringify(this.user))
      const res = await NationService.processData(this.user)
      this.$localStorage.set('price', JSON.stringify(res.data.price))
      console.log(res.data.price)
      this.$router.push({ name: 'zillowpage' })
    }
  }
}
</script>
