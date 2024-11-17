<template>
	<button class="back-button" @click="volver">
			<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<div class="configuracion">
			<div class="menu">
					<h2>Configuración</h2>
					<router-link class="config-button" to="/updateCorreo">Actualizar Correo</router-link>
					<router-link class="config-button" to="/updateContra">Actualizar Contraseña</router-link>
					<button class="config-button" @click="seleccionarImagen">Cambiar Foto</button>
					<button class="config-button eliminar-button" @click="eliminarCuenta">Eliminar Cuenta</button>
					<input type="file" ref="imagenInput" @change="cambiarFoto" style="display: none;" />
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

const usuario = computed(() => store.state.usuario);

const seleccionarImagen = () => {
	imagenInput.value.click(); // Abrir el selector de archivos
};

const cambiarFoto = async (event) => {
	const archivo = event.target.files[0];
	if (!archivo) return;

	const formData = new FormData();
	formData.append("imagen", archivo);

	try {
			await axios.post(`http://localhost:8000/usuarios/${usuario.value.id}/imagen`, formData, {
					headers: { "Content-Type": "multipart/form-data" }
			});
			Swal.fire({
					icon: 'success',
					title: 'Imagen actualizada',
					text: 'Tu foto de perfil se ha actualizado correctamente.',
			});
	} catch (error) {
			console.error("Error al subir la imagen:", error);
			Swal.fire({
					icon: 'error',
					title: 'Error',
					text: 'No se pudo actualizar la foto de perfil.',
			});
	}
};


const eliminarCuenta = async () => {
	try {
			await axios.delete(`http://localhost:8000/usuarios/${usuario.value.id}`);
			store.commit('logoutUsuario');
			Swal.fire({
					icon: 'success',
					title: 'Cuenta eliminada exitosamente',
					text: 'Redirigiendo...',
					timer: 2000,
					showConfirmButton: false,
			}).then(() => {
					router.push('/');
			});
	} catch (error) {
			console.error("Error al eliminar la cuenta:", error);
			Swal.fire({
					icon: 'error',
					title: 'Error',
					text: 'No se pudo eliminar la cuenta.',
			});
	}
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