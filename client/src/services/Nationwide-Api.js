import Api from '@/services/Api'

export default {
  getNationwide (id) {
    return Api().get('customerBalances?id=' + id)
  },
  processData (user) {
    return Api().post('processTotalFunds', user)
  },
  callOnboardApi (data) {
    // return Api().post('', data)
    return [{'id': 1234}]
  }
}
