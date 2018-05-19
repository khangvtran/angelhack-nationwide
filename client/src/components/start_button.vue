<template>
	<form @submit.prevent="submitHandler">
		<label for="monthly_salary">Monthly Salary</label>
		<input type="number" name="monthly_salary" id="monthly_salary" v-model="user.monthly_salary">
		<label for="savings">Savings set aside for a Home</label>
		<input type="number" name="savings" id="savings" v-model="user.savings">
		<input type="submit" value="Submit">
	</form>
</template>

<script scoped>
	export default {
		data() {
			return {
				user: {
					monthly_salary: '',
					savings: ''
				}
			}
		},
		methods: {
			submitHandler(){
				this.$localStorage.set("user", JSON.stringify(this.user))
			}
		}
	}
</script>
