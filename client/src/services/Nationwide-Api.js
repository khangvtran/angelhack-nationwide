import axios from 'axios'

let headers = {
  'Access-Control-Allow-Origin' : '*',
  'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
  'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token'
}

export default {
  getNationwide (id) {
    return axios.create({ baseURL: 'http://localhost:5000/api/' }).get('customerBalances/' + id)
  },
  processData (user) {
    return axios.create({baseURL: 'http://localhost:5000/api/'}).post('processTotalFunds', user, headers)
  },
  callOnboardApi (data) {
    // return axios.create({baseURL: ""}).post('', data)
    return [{"id": "form data is working right now!"}]
  }
}
