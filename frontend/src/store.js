import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		currentUser: {},
		gripsOnGrid: [],
		serverUrl: 'http://localhost:8000/',
	},
	mutations: {
		updateUser(state, userObject) {
			state.currentUser = userObject
		},
		async fetchGrips(state) {
			const response = await axios.get(state.serverUrl + 'v1/grips', {
				headers: {
					Authorization: 'Bearer ' + state.currentUser.token,
				}
			});
			if (response.status === 200) {
				state.gripsOnGrid = response.data;
				return;
			}

			state.gripsOnGrid = [];
    }
	}
})
