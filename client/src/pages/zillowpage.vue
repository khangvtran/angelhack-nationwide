<template>
	<div>
		<p>this is the zillowpage</p>
		<form @submit.prevent="submitHandler">
			<label for="zipcode">Zip Code</label>
			<input type="text" name="zipcode" id="zipcode" v-model="zipcode.number">
			<input type="submit" name="submit" value="submit">
		</form>
		<table></table>
	</div>
</template>

<script>
	export default {
		data(){
			zipcode: {
				number: ""
			}
		},
		methods: {
			submitHandler(){

			}
		}
	}
</script>
