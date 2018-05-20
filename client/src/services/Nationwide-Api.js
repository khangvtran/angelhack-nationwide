import Api from '@/services/Api'

export default {
  getNationwide (id) {
    return Api().get('customerBalances?id=' + id)
  },
  processData (user) {
    return Api().post('processTotalFunds', user)
  },
  callOnboardApi (data) {
    // return axios.create({baseURL: ""}).post('', data)
    return [{'id': 'form data is working right now!'}]
  }
}
