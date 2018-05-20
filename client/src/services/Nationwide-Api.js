import Api from '@/services/Api'

let headers = {
  'Access-Control-Allow-Origin' : '*',
  'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
  'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token'
}

export default {
  getNationwide (id) {
    return Api().get('customerBalances?id=' + id)
  },
  processData (user) {
    return Api().post('processTotalFunds', user, headers)
  },
  callOnboardApi (data) {
    return Api().post('houseData', data, headers)
    // return [{'id': 'form data is working right now!'}]
  },
  callZillowApi(address){
    return Api().get('', address, headers)
  }
}
