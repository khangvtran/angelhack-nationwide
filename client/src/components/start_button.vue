<template>
  <v-layout class="start-button">
    <v-flex xs12 sm8 offset-sm2>

      <Panel title="Non Nationwide Members">
        <v-container>
          <v-form @submit="submitHandler">
          <v-text-field label="Monthly Salary:" type="number" name="monthly_salary" id="monthly_salary" v-model="user.monthly_salary"></v-text-field>
          <v-text-field label="Savings set aside for a Home:" type="number" name="savings" id="savings" v-model="user.savings"></v-text-field>
          <v-btn type="submit">Submit</v-btn>
        </v-form>
        </v-container>
      </Panel>

    </v-flex>
  </v-layout>
</template>

<script scoped>
import Panel from '@/components/Panel'
export default {
  components: {
    Panel
  },
  data () {
    return {
      user: {
        monthly_salary: null,
        savings: null
      }
    }
  },
  methods: {
    submitHandler (e) {
      e.preventDefault()
      this.$localStorage.set('user', JSON.stringify(this.user))
      this.$router.push({ name: 'additionalinfo' })
    }
  }
}
</script>

<style scoped>
  .start-button {
    margin-top: 60px;
  }
</style>
