<template>
  <v-layout class="additionalinfo">
    <v-flex xs12 sm8 offset-sm2>
      <Panel title="Additional Information">
        <v-btn
          flat
          absolute
          right
          slot="toolbar-item"
          @click="goBack"
          >Go Back</v-btn>

        <v-container>
          <v-form v-model="valid" ref="form" lazy-validation @submit.prevent="submitHandler">
            <v-text-field
            label="Percent of month income you want to set aside for a home"
            type="number"
            name="percent"
            id="percent"
            v-model="user.percent"
            :rules="[rules.required]"
            required>
            </v-text-field>
            <v-text-field
            label="How long do you want to wait until you buy a home? (Months)"
            type="number"
            name="waitmonths"
            id="waitmonths"
            v-model="user.wait_months"
            :rules="[rules.required]"
            required>
            </v-text-field>
            <v-text-field
            label="How long do you want your mortgage to be? (Years)"
            type="number"
            name="mortgage_years"
            id="mortgage_years"
            v-model="user.mortgage_years"
            :rules="[rules.required]"
            required>
            </v-text-field>
            <v-btn type="submit" name="submit">Submit</v-btn>
          </v-form>
        </v-container>
      </Panel>

    </v-flex>
  </v-layout>
</template>

<script scoped>
import Panel from '@/components/Panel'
import NationService from '@/services/Nationwide-Api'
export default {
  components: {
    Panel
  },
  data () {
    return {
      valid: true,
      user: {
        monthly_salary: JSON.parse(this.$localStorage.get('user')).monthly_salary,
        savings: JSON.parse(this.$localStorage.get('user')).savings,
        percent: null,
        wait_months: null,
        mortgage_years: null
      },
      rules: {
        required: v => !!v || 'Required.'
      }
    }
  },
  methods: {
    async submitHandler (e) {
      e.preventDefault()
      if (this.$refs.form.validate()) {
        this.$localStorage.set('user', JSON.stringify(this.user))
        const res = await NationService.processData(this.user)
        this.$localStorage.set('price', JSON.stringify(res.data.price))
        this.$router.push({ name: 'zillowpage' })
      }
    },
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>

<style media="screen">
  .additionalinfo {
    margin-top: 60px;
  }
</style>
