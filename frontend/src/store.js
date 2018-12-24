import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		userToken: ""
	},
	mutations: {
		updateUserToken(state, userToken) {
			state.userToken = userToken
		}
	}
})
