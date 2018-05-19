import axios from 'axios'

export default {
  // http://nw-angelhack-2018-mocks.us-east-1.elasticbeanstalk.com/customers
  get () {
    return axios.create({ baseURL: 'http://nw-angelhack-2018-mocks.us-east-1.elasticbeanstalk.com/' }).get('customers')
  },

  getNationwide(id) {
  	return axios.create({ baseURL: 'localhost:5000/api/'}).get('customerBalances/' + id)
  }
}
