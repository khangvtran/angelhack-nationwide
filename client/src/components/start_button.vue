<template>
  <div class="start_button">
    <h1>Non Nationwide Members</h1>
    <form @submit="submitHandler">
      <label for="monthly_salary">Monthly Salary</label>
      <input type="number" name="monthly_salary" id="monthly_salary" v-model="user.monthly_salary">
      <br>
      <label for="savings">Savings set aside for a Home</label>
      <input type="number" name="savings" id="savings" v-model="user.savings">
      <br>
      <input type="submit" value="Submit">
    </form>
  </div>
</template>

<script scoped>
export default {
  data () {
    return {
      user: {
        monthly_salary: null,
        savings: null
      }
    }
  },
  methods: {
    submitHandler (e) {
      e.preventDefault()
      this.$localStorage.set('user', JSON.stringify(this.user))
      this.$router.push({ name: 'additionalinfo' })
    }
  }
}
</script>
