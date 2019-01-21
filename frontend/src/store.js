import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import http from './utils/http';

Vue.use(Vuex)

export default new Vuex.Store({
	plugins: [createPersistedState({key: '__syllable'})],
	state: {
		currentUser: null,
		gripsOnGrid: [],
	},
	mutations: {
		updateUser(state, userObject) {
			state.currentUser = Object.assign({}, state.currentUser, userObject);
		},
		clearUser(state) {
			state.currentUser = null;
		},
		updateGripGrid(state, grips) {
			grips.sort((a,b) => b.votes - a.votes);
			state.gripsOnGrid = grips;
		},
	},
	actions: {
		async refreshUser(context) {
			const users = await http.get('v1/users/me');
			context.commit('updateUser', users.data);
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
