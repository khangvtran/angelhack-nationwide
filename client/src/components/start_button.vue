<template>
  <form @submit.prevent="submitHandler">
    <label for="monthly_salary">Monthly Salary</label>
    <input type="number" name="monthly_salary" id="monthly_salary" v-model="user.monthly_salary">
    <label for="savings">Total Savings</label>
    <input type="number" name="savings" id="savings" v-model="user.savings">
    <input type="submit" value="Submit">
  </form>
</template>

<script >
export default {
  data () {
    return {
      user: {
        monthly_salary: '',
        savings: ''
      }
    }
  },
  methods: {
    submitHandler () {
      this.$localStorage.set('monthly_salary', this.user.monthly_salary)
      this.$localStorage.set('savings', this.user.savings)
      console.log(this.$localStorage.get('monthly_salary'))
      this.$router.push({name: 'zillowpage'})
    }
  }
}
</script>
