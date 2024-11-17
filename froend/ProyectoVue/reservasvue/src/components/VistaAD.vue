<template>
  <div class="main-container">
    <nav>
      <div class="sidebar-top">
        <a href="#" class="logo__wrapper">
          <img src="../assets/admin.svg" alt="Logo" class="logo">
          <h1 :class="{ hide: sidebarCollapsed }">Administrador</h1>
        </a>
        <div class="expand-btn" @click="toggleCollapse">
          <img src="../assets/chevron.svg" alt="Chevron">
        </div>
      </div>
      <div class="sidebar-links">
        <ul>
          <li>
            <router-link to="/ClientesVer" class="tooltip">
              <img src="../assets/customer-service-information-svgrepo-com.svg" alt="Dashboard">
              <span :class="{ hide: sidebarCollapsed }" class="link">Clientes</span>
              <span class="tooltip__content">Clientes</span>
            </router-link>
          </li>
          <li>
            <router-link to="/ReservasView" class="tooltip">
              <img src="../assets/reservation-smartphone-svgrepo-com.svg" alt="Analytics">
              <span :class="{ hide: sidebarCollapsed }" class="link">Historial Reservas</span>
              <span class="tooltip__content">Historial Reservas</span>
            </router-link>
          </li>
          <li>
            <router-link class="tooltip" to="/TablaPqrAd">
              <img src="../assets/help.svg" alt="PQRS">
              <span :class="{ hide: sidebarCollapsed }" class="link">NOVEDADES</span>
              <span class="tooltip__content">NOVEDADES</span>
            </router-link>
          </li>
        </ul>
      </div>
      <div class="sidebar-bottom">
        <div class="sidebar-links">
          <ul>
            <li>
              <router-link to="/conf" class="tooltip">
                <img src="../assets/settings.svg" alt="Settings">
                <span :class="{ hide: sidebarCollapsed }" class="link">Ajustes</span>
                <span class="tooltip__content">Ajustes</span>
              </router-link>
            </li>
            <li>
              <router-link to="/Iniciar" class="tooltip">
                <img src="../assets/logout-svgrepo-com.svg" alt="salir">
                <span :class="{ hide: sidebarCollapsed }" class="link">Salir</span>
                <span class="tooltip__content">Salida</span>
              </router-link>
            </li>
          </ul>
        </div>
        <div class="sidebar__profile">
          <div class="avatar__wrapper">
            <img class="avatar" :src="imagenPerfil" alt="Profile">
            <div class="online__status"></div>
          </div>
          <div :class="{ hide: sidebarCollapsed }" class="avatar__name">
            <div class="user-name">{{ usuario.nombre }}</div>
            <div class="email">{{ usuario.correoElectronico }}</div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>


<script>
import { mapState } from 'vuex';
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  name: "VistaAD",
  data() {
    return {
      sidebarCollapsed: false,
	  imagenPorDefecto: 'ruta/a/imagen/por/defecto.jpg',
    };
  },

  computed: {
    imagenPerfil() {
      const store = useStore();
      return store.state.usuario.imagen 
        ? `http://localhost:8000/${store.state.usuario.imagen}` 
        : this.imagenPorDefecto;
    },
	...mapState(['usuario']),
  },

  methods: {
  toggleCollapse() {
    this.sidebarCollapsed = !this.sidebarCollapsed;
    if (this.sidebarCollapsed) {
      document.body.classList.add('collapsed');
    } else {
      document.body.classList.remove('collapsed');
    }
  },
},
  
};
</script>
  
<style scoped>
/*Estilos generales para el template del html */ 
.main-container {
    --primary-color: #c13515;
    --text: #EDF0F7;
    --sidebar-gray: #111926;
    --sidebar-gray-light: #F8F7FD;
    --sidebar-gray-background: #db3d19;
    --success: #00C896;
    --white: #fff;
}

html {
  font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.main-container{
  display: flex;
}

nav {
    position: sticky;
    top: 0;
    left: 0;
    height: 100vh;
    background-color: var(--primary-color);
    width: 23rem;
    padding: 0.25rem 0.75rem;
    display: flex;
    color: var(--white);
    flex-direction: column;
    transition: width 0.5s linear;
}
/** mas estilos  */


body.collapsed nav {
  width: 5rem;
}

body.collapsed .hide {
  position: absolute;
  display: none;
  pointer-events: none;
}

.sidebar-top {
  position: relative;
  display: flex;
  align-items: start;
  justify-content: center;
  flex-direction: column;
  min-height: 2.5rem;
  padding: 1rem 0;
}
/*de para abajo son mas estilos  */
body.collapsed .sidebar-top {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.logo__wrapper {
  display: flex;
  justify-content: start;
  align-items: center;
  gap: 1.25rem;
  color: var(--white);
  text-decoration: none;
}

.logo {
  width: 3.5rem;
  height: 3.5rem;
  background: var(--sidebar-gray-background);
  border-radius: 0.75rem;
}

.expand-btn {
  top: 1rem;
  right: -4.75rem;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  width: 3rem;
  height: 3rem;
  background: var(--white);
  cursor: pointer;
  box-shadow: #6067EB50 0px 2px 8px 0px;
}

.expand-btn img {
  transform: rotate(180deg);
  stroke: var(--primary-color);
  width: 2.375rem;
  height: 2.375rem;
}


body.collapsed .expand-btn img {
  transform: rotate(360deg);
}

.sidebar-links {
  padding: 0.5rem 0;
  border-top: 1px solid var(--sidebar-gray-background);
}

/* menu de links */
.sidebar-links ul {
  list-style-type: none;
  position: relative;
}

.sidebar-links li {
  position: relative;
}

.sidebar-links li a {
  padding: 0.875rem 0.675rem;
  margin: 0.5rem 0;
  color: var(--sidebar-gray-light);
  font-size: 1.25rem;
  display: flex;
  justify-content: start;
  align-items: center;
  border-radius: 0.675rem;
  height: 3.5rem;
  text-decoration: none;
  transition: all 0.2s ease-in-out;
}

.sidebar-links li a img {
  height: 2.125rem;
  width: 2.125rem;
}


.sidebar-links .link {
  margin-left: 1.875rem;
}

.sidebar-links li a:hover, 
.sidebar-links li a:focus, 
.sidebar-links .active {
  width: 100%;
  text-decoration: none;
  background-color: var(--sidebar-gray-background);
  border-radius: 0.675rem;
  outline: none;
  color: var(--sidebar-gray-light);
}

.sidebar-links .active {
  color: var(--white);
}

/* botones del slidebar */

.sidebar-bottom {
  padding: 0.5rem 0;
  display: flex;
  justify-content: center;
  flex-direction: column;
  margin-top: auto;
}

/* perfil styles */
.sidebar__profile {
  display: flex;
  align-items: center;
  gap: 1.125rem;
  flex-direction: row;
  padding: 1.5rem 0.125rem;
  border-top: 1px solid var(--sidebar-gray-background);
}

.avatar__wrapper {
  position: relative;
  display: flex;
}

.avatar {
  display: block;
  width: 3.125rem;
  height: 3.125rem;
  cursor: pointer;
  border-radius: 50%;
  object-fit: cover;
  filter: drop-shadow(
    -20px 0 10px rgba(0, 0, 0, 0.1)
  );
}

.avatar:hover {
  transform: scale(1.05);
  transition: all 0.2s ease-in-out;
}

.avatar__name {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.user-name {
  font-size: 0.95rem;
  font-weight: 800;
  text-align: left;
}

.email {
  font-size: 0.9rem;
}

.online__status {
  position: absolute;
  width: 0.75rem;
  height: 0.75rem;
  border-radius: 50%;
  background-color: var(--success);
  bottom: 0.1875rem;
  right: 0.1875rem;
}

/* informacion herrmientas */
.tooltip {
  position: relative;
}

.tooltip .tooltip__content {
  visibility: hidden;
  background-color: var(--sidebar-gray-background);
  color: var(--white);
  text-align: center;
  border-radius: 0.375rem;
  padding: 0.375rem 0.75rem;
  position: absolute;
  z-index: 1;
  left: 4.6875rem;
}
body.collapsed .tooltip:hover .tooltip__content,
body.collapsed .tooltip:focus .tooltip__content {
  visibility: visible;
}

/** sylos de tabla de informcaicon */

</style>
