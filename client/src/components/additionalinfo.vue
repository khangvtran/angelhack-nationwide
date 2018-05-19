<template>
  <form @submit.prevent="submitHandler">
    <label for="percent">Percent of month income you want to set aside for a home</label>
    <input type="number" name="percent" id="percent" v-model="user.percent">
    <label for="waitmonths">How long do you want to wait until you buy a home?</label>
    <input type="number" name="waitmonths" id="waitmonths" v-model="user.waitmonths">
    <input type="submit" name="submit" value="submit">
  </form>
</template>

<script scoped>
  export default {
    data() {
      return {
        user: {
          monthy_salary: JSON.parse(this.$localStorage.get("user")).monthly_salary,
          savings: JSON.parse(this.$localStorage.get("user")).savings,
          percent: '',
          waitmonths: ''
        }
      }
    },
    methods: {
      submitHandler(){
        this.$localStorage.set("user", JSON.stringify(this.user))
        let object = this.$localStorage.get('user')
        console.log(object)
      }
    }
  }
</script>