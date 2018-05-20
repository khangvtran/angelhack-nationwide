<template>
  <div>
    <h1>Your estimated house you can afford: {{price}}</h1>
    <form @submit.prevent="submitHandler">
      <label for="zipcode">Zip Code</label>
      <input type="number" name="zipcode" id="zipcode" v-model="zipcode" required>
      <input type="submit" name="submit" value="submit">
    </form>
    <table>
      <tr v-for="item in res">
        <td></td>
      </tr>
    </table>
  </div>
</template>

<script>
import NationService from '@/services/Nationwide-Api'
export default {
  data() {
    return {
      zipcode: '',
      res: null,
      price: this.$localStorage.get('price')
    }
  },
  methods: {
    async submitHandler () {
      var data = {
        'zipcode': this.zipcode,
        'price': this.price
      }
      console.log(data)
      this.res = NationService.callOnboardApi(data)
    }
  }
}
</script>
