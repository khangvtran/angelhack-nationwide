import axios from 'axios'

export default {
  getNationwide (id) {
    return axios.create({ baseURL: 'http://localhost:5000/api/' }).get('customerBalances/' + id)
  },
  processData(user){
    return axios.create({baseURL: 'http://localhost:5000/api/'}).post('processTotalFunds', user)
  },
  callonboardApi(data){
    return axios.create({baseURL: })
  }
}
