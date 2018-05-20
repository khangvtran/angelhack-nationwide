<template>
  <v-layout class="zillowpage">
    <v-flex xs12>
      <v-container>
        <h3>Your estimated house you can afford: {{price}}</h3>
        <v-form @submit.prevent="submitHandler">
          <v-text-field label="Zip Code" type="text" name="zipcode" id="zipcode" pattern="[0-9]{5}" maxlength="5" title="Please enter valid zipcode" v-model="zipcode" required></v-text-field>
          <v-btn type="submit" name="submit">Submit</v-btn>
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
        <div id="zillow">
          <h1>{{house}}</h1>
        </div>
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
      console.log(this.house)
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
    }
  }
}
</script>

<style scoped>
</style>
