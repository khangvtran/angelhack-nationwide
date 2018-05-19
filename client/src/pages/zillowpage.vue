<template>
	<div>
		<form @submit.prevent="submitHandler">
			<label for="zipcode">Zip Code</label>
			<input type="text" name="zipcode" id="zipcode" v-model="zipcode.number">
			<input type="submit" name="submit" value="submit">
		</form>
		<table>{{res}}</table>
	</div>
</template>

<script>
	import NationService from '@/services/Nationwide-Api'
	export default {
		data(){
			return {
				zipcode: {
					number: ""
				},
				res: null
			}
		},
		methods: {
			async submitHandler(){
				var data = {
					"zipcode": this.zipcode.number,
					"monthly_salary": this.$localStorage.get('monthly_salary'),
					"savings": this.$localStorage.get('savings')
				}
				this.res = await NationService.postToZipcode(data)
			}

		}
	}
</script>
