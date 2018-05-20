<template>
  <div>
    <h1>Your estimated house you can afford: {{price}}</h1>
    <form @submit.prevent="submitHandler">
      <label for="zipcode">Zip Code</label>
      <input type="text" name="zipcode" id="zipcode" pattern="[0-9]{5}" maxlength="5" title="Please enter valid zipcode" v-model="zipcode" required>
      <input type="submit" name="submit" value="submit">
    </form>
    <table>
      <tr v-for="item in res">
        <td>{{item.id}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import NationService from '@/services/Nationwide-Api'
export default {
  data () {
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
