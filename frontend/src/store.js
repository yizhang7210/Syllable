import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		currentUser: {},
		gripsOnGrid: [],
		serverUrl: process.env.VUE_APP_SERVER_URL,
	},
	mutations: {
		updateUser(state, userObject) {
			state.currentUser = userObject
		},
		async fetchAllGrips(state) {
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
    },
		async searchGrips(state, searchTerm) {
			const searchUrl = state.serverUrl + 'v1/grips/search?q=' + searchTerm
			const response = await axios.get(searchUrl, {
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
