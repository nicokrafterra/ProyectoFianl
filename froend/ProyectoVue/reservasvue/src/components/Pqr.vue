<template>
	<div class="contpri">
	<button class="back-button" @click="volver">
		<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<div class="pqr-form">
		<h2>Crear PQR</h2>
		<form @submit.prevent="enviarPqr">
			<div class="form-group">
				<label for="correo">Correo Electrónico:</label>
				<input type="email" id="correo" v-model="correo" required />
			</div>

			<div class="form-group">
				<label for="descripcion">Descripción:</label>
				<textarea id="descripcion" v-model="descripcion" required></textarea>
			</div>

			<button class="btn" type="submit">Enviar PQR</button>
		</form>
		<p v-if="mensaje" class="mensaje">{{ mensaje }}</p>
	</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const correo = ref('');
const descripcion = ref('');
const mensaje = ref('');

const store = useStore();
const router = useRouter();

const usuario = computed(() => store.state.usuario);

const volver = () => {
	router.back();
};

const enviarPqr = async () => {
	if (!usuario.value || !usuario.value.id) {
		mensaje.value = 'El usuario no está definido. Inicia sesión para enviar un PQR.';
		return;
	}

	const pqrData = {
		usuario_id: usuario.value.id,
		correo: correo.value,
		descripcion: descripcion.value,
	};

	try {
		const response = await fetch('http://localhost:8000/pqr/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(pqrData),
		});

		if (!response.ok) {
			throw new Error('Error al enviar el PQR');
		}

		const data = await response.json();
		mensaje.value = 'PQR enviado exitosamente';

		correo.value = '';
		descripcion.value = '';
	} catch (error) {
		console.error('Error:', error);
		mensaje.value = 'No se pudo enviar el PQR. Intenta nuevamente.';
	}
};
</script>

<style scoped>

.contpri{
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center;
}

.pqr-form {
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
	backdrop-filter: blur(10px);
}

h2 {
	color: #000000;
	font-size: 24px;
	margin-bottom: 20px;
}

.form-group {
	margin-bottom: 20px;
	text-align: left;
}

label {
	font-weight: bold;
	color: #000000;
	display: block;
	margin-bottom: 8px;
}

input[type="email"],
textarea {
	width: 245px;
	min-height: 45px;
	color: #fff;
	outline: none;
	transition: 0.35s;
	padding: 0px 7px;
	background-color: #212121;
	border-radius: 6px;
	border: 2px solid #212121;
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6);
}

input[type="email"]:focus,
textarea:focus {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
}


textarea {
	resize: vertical;
	min-height: 100px;
}

.btn {
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

.btn:hover {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
}

.mensaje {
	margin-top: 20px;
	color: #d9534f;
	font-weight: bold;
}

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
	transition: transform 0.2s ease;
}

</style>
