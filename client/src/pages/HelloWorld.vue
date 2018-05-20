<template>
  <v-layout class="helloworld">
    <v-flex xs12 sm8 offset-sm2>

      <Panel title="Start Planning!">
        <v-container>
          <h2>Do you find the idea of buying a house initimidating?</h2>
          <p>
            It's a big life decision and we know it can be anxious! That's why we're here to make your experience be as smooth and informative.
            <br>
            So let's get Started!
          </p>
          <v-card-title>
            <div>
              <h3>Q. Are you a Nationwide Member?</h3>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-flex>
              <v-btn v-show="!isMember" @click="isMember = !isMember">Yes</v-btn>
              <div v-show="isMember">
                <v-form @submit="getData">
                  <v-text-field label="Enter your Nationwide ID:" v-model="form.id" type="text"></v-text-field>
                  <v-btn type="submit">Submit</v-btn>
                  <v-btn @click="isMember = !isMember" type="button">Cancel</v-btn>
                </v-form>
              </div>
              <v-btn v-show="!isMember" :to="{ name: 'start_button' }">No</v-btn>
            </v-flex>
          </v-card-actions>
        </v-container>
      </Panel>

    </v-flex>
  </v-layout>
</template>

<script>
import Panel from '@/components/Panel'
import NationService from '@/services/Nationwide-Api'
export default {
  name: 'HelloWorld',
  components: {
    Panel
  },
  data () {
    return {
      form: {
        id: null
      },
      user: {
        monthly_salary: null,
        savings: null
      },
      isMember: false
    }
  },
  methods: {
    async getData (e) {
      e.preventDefault()
      const response = await NationService.getNationwide(this.form.id)
      this.user.monthly_salary = response.data.monthly_salary
      this.user.savings = response.data.savings
      this.$localStorage.set('user', JSON.stringify(this.user))
      this.$router.push({ name: 'additionalinfo' })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.helloworld {
  margin-top: 60px;
}
</style>
