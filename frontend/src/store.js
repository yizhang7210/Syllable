import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		currentUser: {},
		serverUrl: 'http://localhost:8000/',
	},
	mutations: {
		updateUser(state, userObject) {
			state.currentUser = userObject
		}
	}
})
