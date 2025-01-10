import { createStore } from 'vuex';

const store = createStore({
  state: {
    usuario: null, // Estado para almacenar la información del usuario
    tipoPlan: null,
  },
  mutations: {
    actualizarFoto(state, nuevaRuta) {
      if (state.usuario) {
          state.usuario.imagen = nuevaRuta;
      }
    },
    setUsuario(state, usuario) {
      state.usuario = usuario;
    },
    clearUsuario(state) {
      state.usuario = null;
      
    },
    setTipoPlan(state, plan) {
      state.tipoPlan = plan;
    },
    RESET_TIPO_PLAN(state) {
      state.tipoPlan = null;
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
    guardarTipoPlan({ commit }, plan) {
      commit("setTipoPlan", plan);
    },
    resetTipoPlan({ commit }) {
      commit("RESET_TIPO_PLAN"); // Llama a la mutación que resetea el tipo de plan
    },
  },
  getters: {
    usuarioId: (state) => state.usuario?.id, // Retorna el ID del usuario si existe
    esAdmin: (state) => state.usuario?.esAdmin, // Getter opcional para verificar si el usuario es admin
    obtenerTipoPlan: (state) => state.tipoPlan,
  },
});

export default store;