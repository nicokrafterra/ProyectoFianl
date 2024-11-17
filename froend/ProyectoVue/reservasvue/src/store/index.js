import { createStore } from 'vuex';

const store = createStore({
  state: {
    usuario: null, // Estado para almacenar la información del usuario
  },
  mutations: {
    setUsuario(state, usuario) {
      state.usuario = usuario;
    },
    clearUsuario(state) {
      state.usuario = null;
    },
  },
  actions: {
    registerUsuario({ commit }, usuario) {
      commit('setUsuario', usuario); // Guardar el usuario en el estado
    },
    loginUsuario({ commit }, usuario) {
      commit('setUsuario', usuario); // Guardar el usuario en el estado
    },
    logoutUsuario({ commit }) {
      commit('clearUsuario'); // Limpiar el estado del usuario
    },
  },
  getters: {
    usuarioId: (state) => state.usuario?.id, // Retorna el ID del usuario si existe
    esAdmin: (state) => state.usuario?.esAdmin, // Getter opcional para verificar si el usuario es admin
  },
});

export default store;