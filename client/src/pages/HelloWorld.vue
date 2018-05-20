<template>
  <v-layout class="helloworld">
    <v-flex xs12 sm8 offset-sm2>

      <Panel title="Start Planning!">
        <v-container>
          <v-card-actions>
            <v-btn :to="{ name: 'start_button' }" name="button">Non Nationwide Members</v-btn>
            <v-form @submit="getData">
              <v-text-field label="Enter your Nationwide ID:" v-model="form.id" type="text"></v-text-field>
              <v-btn type="submit" name="button">Nationwide</v-btn>
            </v-form>
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
      }
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
