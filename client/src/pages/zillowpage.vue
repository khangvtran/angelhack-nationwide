<template>
  <div>
    <h1>Your estimated house you can afford: {{price}}</h1>
    <form @submit.prevent="submitHandler">
      <label for="zipcode">Zip Code</label>
      <input type="text" name="zipcode" id="zipcode" pattern="[0-9]{5}" maxlength="5" title="Please enter valid zipcode" v-model="zipcode" required>
      <input type="submit" name="submit" value="submit">
    </form>
    <table id="table">
      <tr v-for="house in houses" v-on:click="zillowcall(house)">
        <td>{{house.summary.propclass}}</td>
      </tr>
    </table>
    <div id="zillow" style="visibility: hidden;">
      <h1>This will be the zillow element</h1>
    </div>
  </div>
</template>

<script>
import NationService from '@/services/Nationwide-Api'
export default {
  data () {
    return {
      zipcode: '',
      houses: null,
      price: this.$localStorage.get('price'),
      house: null
    }
  },
  methods: {
    async submitHandler () {
      var data = {
        'zipcode': this.zipcode,
        'price': this.price
      }
      console.log(data)
      let res = await NationService.callOnboardApi(data)
      this.houses = res.data.property
    },
    zillowcall(house){
      // let res = await NationService.zillowcall(house.address)
      var table = document.getElementById('table')
      table.style.visibility = "hidden"
      var zillow = document.getElementById('zillow')
      zillow.style.visibility = "visible"
      // this.house = res
    }
  }
}
</script>
