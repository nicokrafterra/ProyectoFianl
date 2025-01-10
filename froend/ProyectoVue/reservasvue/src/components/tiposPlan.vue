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
/* Estilos del botón "Volver" */
.back-button {
	position: absolute;
	top: 20px;
	left: 20px;
	background: none;
	border: none;
	cursor: pointer;
	transition: 0.35s;
}

.back-button:hover{
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
		background-color: #002e02;
		border-radius: 6px;
}

.back-button img {
	width: 24px;
	height: 24px;
}

/* Contenedor central */
.configuracion {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;
}

/* Menú de configuración */
.menu {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	gap: 20px;
	position: absolute;
	backface-visibility: hidden;
	padding: 65px 45px;
	border-radius: 15px;
	box-shadow: inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	backdrop-filter: blur(20px);
	width: 400px;
}


.menu h2 {
	margin-bottom: 25px;
	color: #000000;
	font-weight: bold;
	font-size: 1.5em;
	font-family: 'Courier New', Courier, monospace
}


.config-button {
	padding: 10px 35px;
	cursor: pointer;
	background-color: #212121;
	border-radius: 6px;
	border: 2px solid #212121;
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6);
	color: #fff;
	font-size: 15px;
	font-weight: bold;
	transition: 0.35s;
	text-decoration: none;
	width: 100px;
}

.config-button:hover {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
		background-color: #002e0d;
}


.eliminar-button {
	padding: 10px 35px;
	cursor: pointer;
	background-color: #212121;
	border-radius: 6px;
	border: 2px solid #212121;
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6);
	color: #fff;
	font-size: 15px;
	font-weight: bold;
	transition: 0.35s;
}

.eliminar-button:hover {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
		background-color: #2e0000;
}
</style>