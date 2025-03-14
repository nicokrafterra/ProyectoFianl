<template>
	<div class="recuperar-container">
		<h2>Recuperar Contraseña</h2>
		<form @submit.prevent="solicitarRecuperacion" class="form-recuperar">
			<label for="email">Ingresa tu correo electrónico:</label>
			<input type="email" id="email" v-model="email" required />
			<button type="submit" class="boton-enviar">Enviar</button>
		</form>
		<p v-if="mensaje" class="mensaje">{{ mensaje }}</p>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
			email: '',
			mensaje: ''
		};
	},
	methods: {
		async solicitarRecuperacion() {
			try {
				const response = await axios.post('http://localhost:8000/recuperarpassword', { email: this.email });
				this.mensaje = response.data.message;
			} catch (error) {
				this.mensaje = error.response?.data?.detail || "Error al enviar el correo";
			}
		}
	}
};
</script>

<style scoped>
.recuperar-container {
	max-width: 400px;
	margin: auto;
	text-align: center;
	background-color: #f7f7f7;
	padding: 20px;
	border-radius: 10px;
	box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
	animation: fadeIn 1s ease-in-out;
}

.recuperar-container h2 {
	color: #333;
}

.form-recuperar {
	display: flex;
	flex-direction: column;
	gap: 10px;
}

.form-recuperar label {
	font-size: 14px;
	color: #555;
}

.form-recuperar input {
	padding: 10px;
	font-size: 16px;
	border: 1px solid #ccc;
	border-radius: 5px;
	transition: border-color 0.3s;
}

.form-recuperar input:focus {
	border-color: #007BFF;
	outline: none;
}

.boton-enviar {
	padding: 10px;
	font-size: 16px;
	color: white;
	background-color: #007BFF;
	border: none;
	border-radius: 5px;
	cursor: pointer;
	transition: background-color 0.3s;
}

.boton-enviar:hover {
	background-color: #0056b3;
}

.mensaje {
	margin-top: 15px;
	font-size: 14px;
	color: green;
	animation: slideDown 0.5s ease;
}

@keyframes fadeIn {
	from {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@keyframes slideDown {
	from {
		transform: translateY(-10px);
		opacity: 0;
	}

	to {
		transform: translateY(0);
		opacity: 1;
	}
}
</style>