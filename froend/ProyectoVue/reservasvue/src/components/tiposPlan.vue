<template>
	<button class="back-button" @click="volver">
			<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<div class="configuracion">
			<div class="menu">
					<h2>Tipos de Planes</h2>
					<router-link class="config-button" to="/camping">Campings</router-link>
					<router-link class="config-button" to="/recorrido">Recorridos</router-link>
					<router-link class="config-button" to="/mesas">Mesas</router-link>
					<router-link class="config-button" to="/eventos">Eventos</router-link>
			</div>
	</div>
</template>

<script setup>
import { computed, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import axios from 'axios';
import Swal from 'sweetalert2';

const router = useRouter();
const store = useStore();
const imagenInput = ref(null);

const volver = () => {
	router.back();
};


</script>

<style scoped>
/* Importar FontAwesome para iconos */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

/* Estilos del botón "Volver" */
.back-button {
	position: absolute;
	top: 20px;
	left: 20px;
	background: none;
	border: none;
	cursor: pointer;
	transition: 0.35s;
	font-size: 24px;
	color: #6B8E23; /* Verde Oliva */
}

.back-button:hover {
	transform: scale(1.05);
	color: #8B5A2B; /* Marrón Tierra al hacer hover */
}

/* Contenedor central */
.configuracion {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;
 /* Beige Arena como fondo principal */
}

/* Menú de configuración */
.menu {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	gap: 20px;
	padding: 40px 30px;
	border-radius: 15px;
	background-color: #F5DEB3;
	box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Sombra suave */
	width: 400px;
	animation: fadeInUp 0.8s ease-out; /* Animación de entrada */
}

.menu h2 {
	margin-bottom: 25px;
	color: #6B8E23; /* Verde Oliva */
	font-weight: bold;
	font-size: 1.5em;
	font-family: 'Courier New', Courier, monospace;
	text-align: center;
}

/* Botones */
.config-button,
.eliminar-button {
	width: 200px; /* Mismo ancho para todos los botones */
	padding: 12px 20px;
	cursor: pointer;
	border-radius: 6px;
	border: 2px solid transparent;
	font-size: 15px;
	font-weight: bold;
	transition: 0.35s;
	text-align: center;
	display: flex;
	align-items: center;
	justify-content: center;
	gap: 10px; /* Espacio entre icono y texto */
}

.config-button {
	background-color: #6B8E23; /* Verde Oliva */
	color: #FFFFFF; /* Texto blanco */
}

.config-button:hover {
	background-color: #8B5A2B; /* Marrón Tierra al hacer hover */
	transform: scale(1.05);
}

.eliminar-button {
	background-color: #C1440E; /* Rojo Terracota */
	color: #FFFFFF; /* Texto blanco */
}

.eliminar-button:hover {
	background-color: #A8380B; /* Rojo más oscuro al hacer hover */
	transform: scale(1.05);
}

/* Iconos dentro de los botones */
.config-button i,
.eliminar-button i {
	font-size: 18px;
}

/* Animaciones */
@keyframes fadeInUp {
	from {
		opacity: 0;
		transform: translateY(20px);
	}
	to {
		opacity: 1;
		transform: translateY(0);
	}
}
</style>