import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		userToken: ""
	},
	mutations: {
		onUserLoggedIn(state, userToken) {
			state.userToken = userToken
		}
	}
})
