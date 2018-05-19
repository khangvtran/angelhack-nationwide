import axios from 'axios'

export default {
  // http://nw-angelhack-2018-mocks.us-east-1.elasticbeanstalk.com/customers
  getData (customerId) {
    return axios.create({ baseURL: 'http://nw-angelhack-2018-mocks.us-east-1.elasticbeanstalk.com/' }).get(customerId)
  },

  getNationwide (id) {
    return axios.create({ baseURL: 'localhost:5000/api/' }).get('customerBalances/' + id)
  }
}
