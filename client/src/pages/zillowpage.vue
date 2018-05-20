<template>
  <div>
    <h1>Your estimated house you can afford: {{price}}</h1>
    <form @submit.prevent="submitHandler">
      <label for="zipcode">Zip Code</label>
      <input type="text" name="zipcode" id="zipcode" pattern="[0-9]{5}" maxlength="5" title="Please enter valid zipcode" v-model="zipcode" required>
      <input type="submit" name="submit" value="submit">
    </form>
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
    <div id="zillow" v-if="house">
      <!-- <h1>{{house}}</h1> -->
      <h3 v-if="house.zestimate">Price: {{house.zestimate.amount}}</h3>
      <!-- <p v-if="house.totalRooms">Rooms: {{house.totalRooms}}</p> -->
      <p v-if="house.bedrooms">Bed rooms: {{house.bedrooms}}</p>
      <p v-if="house.bathrooms">Bath rooms: {{house.bathrooms}}</p>
      <p v-if="house.lotSizeSqFt">Size: {{house.lotSizeSqFt}} Square Feet</p>
      <p v-if="house.address">{{house.address.street}} {{house.address.city}} {{house.address.state}} {{house.address.zipcode}}</p>

    </div>
  </div>
</template>

<script>
import NationService from '@/services/Nationwide-Api'
export default {
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
