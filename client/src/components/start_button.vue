<template>
  <v-layout class="start-button">
    <v-flex xs12 sm8 offset-sm2>

      <Panel title="Non Nationwide Members">
        <v-btn
          flat
          absolute
          right
          slot="toolbar-item"
          @click="goBack"
          >Go Back</v-btn>

        <v-container>

          <v-form v-model="valid" ref="form" lazy-validation @submit="submitHandler">
          <v-text-field
            label="Monthly Salary:"
            type="number"
            name="monthly_salary"
            id="monthly_salary"
            :rules="[rules.required]"
            v-model="user.monthly_salary"
            required></v-text-field>
          <v-text-field
            label="Savings set aside for a Home:"
            type="number"
            name="savings"
            id="savings"
            v-model="user.savings"
            :rules="[rules.required]"
            required></v-text-field>
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
      valid: true,
      user: {
        monthly_salary: null,
        savings: null
      },
      rules: {
        required: v => !!v || 'Required.'
      }
    }
  },
  methods: {
    submitHandler (e) {
      e.preventDefault()
      if (this.$refs.form.validate()) {
        this.$localStorage.set('user', JSON.stringify(this.user))
        this.$router.push({ name: 'additionalinfo' })
      }
    },
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
  .start-button {
    margin-top: 60px;
  }
</style>
