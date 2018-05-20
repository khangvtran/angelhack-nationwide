<template>
  <form @submit.prevent="submitHandler">
    <label for="percent">Percent of month income you want to set aside for a home</label>
    <input type="number" name="percent" id="percent" v-model="user.percent" required>
    <label for="wait_months">How long do you want to wait until you buy a home?</label>
    <input type="number" name="waitmonths" id="waitmonths" v-model="user.wait_months" required>
    <label for="mortgage_years">how long do you want your mortgage to be?</label>
    <input type="number" name="mortgage_years" id="mortgage_years" v-model="user.mortgage_years" required>
    <input type="submit" name="submit" value="submit">
  </form>
</template>

<script scoped>
export default {
  data () {
    return {
      user: {
        monthly_salary: JSON.parse(this.$localStorage.get('user')).monthly_salary,
        savings: JSON.parse(this.$localStorage.get('user')).savings,
        percent: '',
        wait_months: '',
        mortgage_years: ''
      }
    }
  },
  methods: {
    submitHandler () {
      this.$localStorage.set('user', JSON.stringify(this.user))
      let object = this.$localStorage.get('user')
      console.log(object)
    }
  }
}
</script>
