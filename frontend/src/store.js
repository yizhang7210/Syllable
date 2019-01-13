import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import http from './utils/http';

Vue.use(Vuex)

export default new Vuex.Store({
	plugins: [createPersistedState()],
	state: {
		currentUser: {},
		gripsOnGrid: [],
	},
	mutations: {
		updateUser(state, userObject) {
			state.currentUser = Object.assign({}, state.currentUser, userObject);
		},
		updateGripGrid(state, grips) {
			state.gripsOnGrid = grips;
		},
	},
	actions: {
		async refreshUser(context) {
			const users = await http.get('v1/users');
			context.commit('updateUser', users.data[0]);
		},
		async fetchAllGrips(context) {
			const grips = await http.get('v1/grips');
			context.commit('updateGripGrid', grips.data);
    },
		async searchGrips(context, searchTerm) {
			const grips = await http.get('v1/grips/search?q=' + searchTerm);
			context.commit('updateGripGrid', grips.data);
		}
	}
})
