<template>
  <div class="additionalinfo">
    <h1>Additional Information</h1>
    <form @submit="submitHandler">
      <label for="percent">Percent of month income you want to set aside for a home</label>
      <input type="number" name="percent" id="percent" v-model="user.percent">
      <br>
      <label for="waitmonths">How long do you want to wait until you buy a home?</label>
      <input type="number" name="waitmonths" id="waitmonths" v-model="user.waitmonths">
      <br>
      <button type="submit" name="submit">Submit</button>
    </form>
  </div>
</template>

<script scoped>
export default {
  data () {
    return {
      user: {
        monthly_salary: JSON.parse(this.$localStorage.get('user')).monthly_salary,
        savings: JSON.parse(this.$localStorage.get('user')).savings,
        percent: null,
        waitmonths: null
      }
    }
  },
  methods: {
    submitHandler (e) {
      e.preventDefault()
      this.$localStorage.set('user', JSON.stringify(this.user))
    }
  }
}
</script>
