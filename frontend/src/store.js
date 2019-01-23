import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import http from './utils/http';

Vue.use(Vuex)

export default new Vuex.Store({
	plugins: [createPersistedState({key: '__syllable'})],
	state: {
		currentUser: null,
		mainGrips: [],
		pinnedGrips: [],
	},
	mutations: {
		updateUser(state, userObject) {
			state.currentUser = Object.assign({}, state.currentUser, userObject);
		},
		clearUser(state) {
			state.currentUser = null;
		},
		updateMainGrips(state, grips) {
			grips.sort((a,b) => b.votes - a.votes);
			state.mainGrips = grips;
		},
		updatePinnedGrips(state, grips) {
			grips.sort((a,b) => b.votes - a.votes);
			state.pinnedGrips = grips;
		},
	},
	actions: {
		async refreshUser(context) {
			const users = await http.get('v1/users/me');
			context.commit('updateUser', users.data);
		},
		async fetchAllGrips(context) {
			context.dispatch('fetchPinnedGrips');
			context.dispatch('fetchUnpinnedGrips');
    },
		async fetchPinnedGrips(context) {
			const grips = await http.get('v1/grips?pinned=true');
			context.commit('updatePinnedGrips', grips.data);
    },
		async fetchUnpinnedGrips(context) {
			const grips = await http.get('v1/grips?pinned=false');
			context.commit('updateMainGrips', grips.data);
    },
		async searchGrips(context, searchTerm) {
			const grips = await http.get('v1/grips/search?q=' + searchTerm);
			context.commit('updatePinnedGrips', []);
			context.commit('updateMainGrips', grips.data);
		}
	}
})
