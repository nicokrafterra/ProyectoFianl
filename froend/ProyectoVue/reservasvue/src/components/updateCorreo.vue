<template>
	<button class="back-button" @click="volver">
		<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<div class="update-form">
		<h2>Actualizar Correo Electrónico</h2>
		<form @submit.prevent="updateEmail">
			<div>
				<label for="newEmail">Nuevo Correo Electrónico:</label>
				<input type="email" v-model="newEmail" required />
			</div>
			<button class="btn" type="submit">Actualizar Correo</button>
		</form>
	</div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';
import Swal from "sweetalert2";


export default {
	data() {
		return {
			newEmail: '',
		};
	},
	computed: {
    ...mapState(['usuario']),
  },
	methods: {
		async updateEmail() {
			try {
				const userId = this.usuario.id
				await axios.put(`http://localhost:8000/usuarios/${userId}/correo`, {
					nuevo_correo: this.newEmail,
				});;
				Swal.fire({
					title: 'EXito!',
					text: 'Correo electrónico actualizado exitosamente',
					icon: 'success',
					confirmButtonText: 'Aceptar'
				});
			} catch (error) {
				console.error(error);
				Swal.fire({
					title: 'Error!',
					text: 'Error al actualizar el correo electrónico',
					icon: 'error',
					confirmButtonText: 'Aceptar'
				});
			}
		},
		volver() {
			this.$router.back();
		},
	},
};
</script>

<style scoped>
.back-button {
	padding: 10px 15px;
	background-color: #4caf50;
	color: white;
	border: none;
	border-radius: 5px;
	cursor: pointer;
	font-weight: bold;
	transition: background-color 0.3s;
}

.back-button:hover {
	background-color: #ff9800;
}

.update-form {
	max-width: 400px;
	margin: 20px auto;
	padding: 20px;
	border-radius: 8px;
	box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
	background-color: #f9f9f9;
	font-family: Arial, sans-serif;
}

h2 {
	text-align: center;
	color: #333;
	margin-bottom: 20px;
}

label {
	display: block;
	margin-bottom: 8px;
	font-weight: bold;
	color: #555;
}

input {
	width: 100%;
	padding: 10px;
	margin-bottom: 15px;
	border: 1px solid #ddd;
	border-radius: 4px;
	font-size: 14px;
	transition: border-color 0.3s;
}

input:focus {
	border-color: #007bff;
	outline: none;
}

.btn {
	width: 48%;
	padding: 10px;
	margin: 5px 1%;
	border: none;
	border-radius: 4px;
	cursor: pointer;
	font-size: 16px;
	color: #ffffff;
	transition: background-color 0.3s;
}

button[type="submit"] {
	background-color: #28a745;
}

button[type="button"] {
	background-color: #dc3545;
}

button:hover {
	opacity: 0.9;
}

p {
	text-align: center;
	margin-bottom: 20px;
	color: #555;
}

@media (max-width: 500px) {
	.update-form {
		width: 90%;
	}
}
</style>