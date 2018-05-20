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
              <p v-if="house.bedrooms">Bed rooms: {{house.bedrooms}}</p>
              <p v-if="house.bathrooms">Bath rooms: {{house.bathrooms}}</p>
              <p v-if="house.lotSizeSqFt">Size: {{house.lotSizeSqFt}} Square Feet</p>
              <p v-if="house.address">{{house.address.street}} {{house.address.city}} {{house.address.state}} {{house.address.zipcode}}</p>
            </v-flex>
            <v-flex xs6>
              <p v-if="house.wait_months">Will need to wait {{house.wait_months}} month(s) in order to buy this house</p>
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
      center: { lat: 45.508, lng: -73.587 }
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
      this.house.wait_months = this.calcuateMortgage(this.house)
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
      console.log(total)
      let user = JSON.parse(this.$localStorage.get('user'))
      let mortgage = parseInt(user.mortgage_years) * 12 * parseInt(user.monthly_salary) * (parseInt(user.percent) / 100)
      console.log(mortgage)
      let result = total - parseInt(user.savings) - mortgage
      console.log(result)
      let results = result / (+user.monthly_salary * (+user.percent / 100))
      return Math.ceil(results)
    }
  }
}
</script>

<style scoped>
</style>
