import { createStore } from "vuex";
import { jwtDecode } from "jwt-decode"; // Importación con llaves

const storedToken = localStorage.getItem("token");

let usuario = null;
if (storedToken) {
  try {
    const payload = jwtDecode(storedToken);

    // Verificar si el token ha expirado
    if (payload.exp * 1000 < Date.now()) {
      localStorage.removeItem("token"); // Eliminar token expirado
    } else {
      usuario = payload; // Restaurar usuario si el token es válido
    }
  } catch (error) {
    console.error("Error al decodificar el token:", error);
    localStorage.removeItem("token"); // Si hay error, eliminar el token inválido
  }
}

const token = localStorage.getItem("token");
const payload = jwtDecode(token);
console.log(payload); // Verifica si contiene información sobre la imagen

const store = createStore({
  state: {
    usuario: null, // Datos del usuario extraídos del token
    token: null, // Token JWT
    tipoPlan: null,
  },
  mutations: {
    setUsuario(state, usuario) {
      state.usuario = usuario; // Esto asegura que Vue detecte el cambio
    },
    setImagen(state, imagen) {
      if (state.usuario) {
        state.usuario.imagen = imagen; // Actualiza la imagen del usuario
      }
    },
    setToken(state, token) {
      state.token = token;
    },
    clearAuth(state) {
      state.usuario = null;
      state.token = null;
    },
    actualizarFoto(state, nuevaRuta) {
      console.log("Actualizando imagen en el store:", nuevaRuta); // Depuración
      if (state.usuario) {
        state.usuario.imagen = nuevaRuta;
      }
    },
    setTipoPlan(state, plan) {
      state.tipoPlan = plan;
    },
    RESET_TIPO_PLAN(state) {
      state.tipoPlan = null;
    },
  },
  actions: {
    async loginUsuario({ commit }, token) {
      commit("setToken", token);
      const payload = jwtDecode(token);
      commit("setUsuario", payload);
      localStorage.setItem("token", token); // Guardar token en localStorage
    },
    cargarToken({ commit }) {
      const storedToken = localStorage.getItem("token");
      if (storedToken) {
        const payload = jwtDecode(storedToken);
        commit("setToken", storedToken);
        commit("setUsuario", payload);
      }
    },
    logoutUsuario({ commit }) {
      commit("clearAuth");
      localStorage.removeItem("token");
      location.reload(); // Recarga la página
    },
    guardarTipoPlan({ commit }, plan) {
      commit("setTipoPlan", plan);
    },
    resetTipoPlan({ commit }) {
      commit("RESET_TIPO_PLAN");
    },
    async actualizarFoto({ commit }, response) {
      try {
        // Supongamos que el backend devuelve un nuevo token con la imagen actualizada
        const nuevoToken = response.data.token;

        // Actualizar el token en el store y en localStorage
        commit("setToken", nuevoToken);
        localStorage.setItem("token", nuevoToken);

        // Decodificar el nuevo token para obtener la información actualizada del usuario
        const payload = jwtDecode(nuevoToken);
        commit("setUsuario", payload);

        console.log("Token y usuario actualizados después de cambiar la foto:", payload);
      } catch (error) {
        console.error("Error al actualizar la foto y el token:", error);
      }
    },
  },
  getters: {
    usuarioId: (state) => state.usuario?.id, // ID del usuario
    esAdmin: (state) => state.usuario?.esAdmin, // Si es administrador
    obtenerTipoPlan: (state) => state.tipoPlan,
    isAuthenticated: (state) => !!state.token, // Verifica si hay sesión activa
  },
});

export default store;
