<template>
  <v-layout class="zillowpage">
    <v-flex xs12>
      <v-container>
        <h3>Your estimated house you can afford: {{price}}</h3>
        <v-form @submit.prevent="submitHandler">
          <v-text-field label="Zip Code" type="text" name="zipcode" id="zipcode" pattern="[0-9]{5}" maxlength="5" title="Please enter valid zipcode" v-model="zipcode" required></v-text-field>
          <v-btn type="submit" name="submit">Submit</v-btn>
          <v-btn
            @click="goBack"
            >Go Back</v-btn>

        </v-form>
        <GmapMap
          :center="center"
          :zoom="18"
          style="width:100%;  height: 600px;"
          >
          <GmapMarker
              :key="index"
              v-for="(m, index) in houses"
              :position="m.position"
              @click="zillowcall(m)"
          ></GmapMarker>
        </GmapMap>
        <v-card id="zillow" v-if="house">
          <v-card-title>
            <div>
              <h3>{{house.useCode}}</h3>
            </div>
          </v-card-title>
          <v-layout row>
            <v-flex xs6>
              <h3 v-if="house.zestimate">Price: {{house.zestimate.amount}}</h3>
              <span v-if="house.bedrooms">Bed rooms: {{house.bedrooms}}</span><br>
              <span v-if="house.bathrooms">Bath rooms: {{house.bathrooms}}</span><br>
              <span v-if="house.lotSizeSqFt">Size: {{house.lotSizeSqFt}} Square Feet</span><br>
              <span v-if="house.address">{{house.address.street}} {{house.address.city}} {{house.address.state}} {{house.address.zipcode}}</span>
            </v-flex>
            <v-flex xs6>
              <p v-if="house.wait_months">Will need to wait {{house.wait_months}} month(s) in order to buy this house</p>
              <div v-if="house.downpayment">
                  <p>With a down payment of ${{Math.ceil(house.downpayment.five)}} (5%)<br>
                  Mortgage will be ${{Math.ceil(house.mortgage.five)}} per month for {{user.mortgage_years}} years</p>
                  <p>With a down payment of ${{Math.ceil(house.downpayment.ten)}} (10%)<br>
                  Mortgage will be ${{Math.ceil(house.mortgage.ten)}} per month for {{user.mortgage_years}} years</p>
                  <p>With a down payment of ${{Math.ceil(house.downpayment.twenty)}} (20%)<br>
                  Mortgage will be ${{Math.ceil(house.mortgage.twenty)}} per month for {{user.mortgage_years}} years</p>
              </div>
            </v-flex>
          </v-layout>
          <v-card-actions>
            <v-btn flat color="orange">Contact Agents</v-btn>
            <v-btn flat color="orange">Contact Owner</v-btn>
          </v-card-actions>
        </v-card>
      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
import Panel from '@/components/Panel'
import NationService from '@/services/Nationwide-Api'
export default {
  components: {
    Panel
  },
  data () {
    return {
      zipcode: '',
      houses: [],
      price: this.$localStorage.get('price'),
      house: null,
      center: { lat: 45.508, lng: -73.587 },
      user: JSON.parse(this.$localStorage.get("user")),
    }
  },
  mounted () {
    this.geolocate()
  },
  methods: {
    async submitHandler () {
      var data = {
        'zipcode': this.zipcode,
        'price': this.price
      }
      let res = await NationService.callOnboardApi(data)
      this.addMarkers(res)
    },
    async zillowcall (house) {
      let res = await NationService.callZillowApi(house.address)
      this.house = res.data.result
      if (this.house.zestimate.amount > +this.price) {
        this.mortgage = Math.ceil (this.user.monthly_salary * (this.user.percent/ 100))
        this.house.wait_months = this.calcuateMortgage(this.house)
      }
      else {
        this.calcuateLowMortgage(this.house)
      }
    },
    geolocate: function () {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        }
      })
    },
    addMarkers (res) {
      for (var i in res.data.property) {
        var house = {
          position: {
            lat: parseFloat(res.data.property[i].location.latitude),
            lng: parseFloat(res.data.property[i].location.longitude)
          },
          address: res.data.property[i].address
        }
        this.houses.push(house)
      }
      this.center = house.position
    },
    goBack () {
      this.$router.go(-1)
    },
    calcuateMortgage (house) {
      let total = house.zestimate.amount
      let user = JSON.parse(this.$localStorage.get("user"))
      let mortgage = parseInt(user.mortgage_years) * 12 * parseInt(user.monthly_salary) * (parseInt(user.percent) / 100)
      let result = total - parseInt(user.savings) - mortgage
      let results = result / (+user.monthly_salary * (+user.percent / 100))
      return Math.ceil(results)
    },
    calcuateLowMortgage(house) {
      let total = house.zestimate.amount
      this.house.downpayment = {
        five: total * 0.05,
        ten:  total * 0.1,
        twenty: total * 0.20
      }
      this.house.mortgage = {
        five: (total - this.house.downpayment.five)/ (this.user.mortgage_years * 12),
        ten: (total - this.house.downpayment.ten)/ (this.user.mortgage_years * 12),
        twenty: (total - this.house.downpayment.twenty)/ (this.user.mortgage_years * 12)
      }
      console.log(this.house.mortgage, this.house.downpayment)
    }
  }
}
</script>

<style scoped>
</style>
