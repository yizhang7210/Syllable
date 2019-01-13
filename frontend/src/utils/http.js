import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  getAuthHeader() {
    const store = require('../store.js').default;
    if (store && store.state && store.state.currentUser) {
      return { headers: { Authorization: 'Bearer ' + store.state.currentUser.token }};
    }
  },
  post(subUrl, payload) {
    return axios.post(SERVER_URL + subUrl, payload, this.getAuthHeader());
  },
  delete(subUrl) {
    return axios.delete(SERVER_URL + subUrl, this.getAuthHeader());
  },
  get(subUrl) {
		return axios.get(SERVER_URL + subUrl, this.getAuthHeader());
  }

}
