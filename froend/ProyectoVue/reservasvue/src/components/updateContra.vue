<template>
	<button class="back-button" @click="volver">
		<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<div class="update-form">
		<h2>Actualizar Contraseña</h2>
		<form @submit.prevent="updatePassword">
			<div>
				<label for="currentPassword">Contraseña Actual:</label>
				<input type="password" v-model="currentPassword" required />
			</div>
			<div>
				<label for="newPassword">Nueva Contraseña:</label>
				<input type="password" v-model="newPassword" required />
			</div>
			<button class="btn" type="submit">Actualizar Contraseña</button>
		</form>
	</div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';
import Swal from 'sweetalert2';
import { jwtDecode } from 'jwt-decode'; // Importamos la librería para decodificar JWT

export default {
	data() {
		return {
			currentPassword: '',
			newPassword: '',
		};
	},
	computed: {
		...mapState(['usuario', 'token']),
		userId() {
			// Si Vuex tiene el ID, lo usa. Si no, lo extrae del token JWT.
			if (this.usuario?.id) {
				return this.usuario.id;
			}
			if (this.token) {
				try {
					const decoded = jwtDecode(this.token); // Decodifica el token
					return decoded.sub; // "sub" es el ID del usuario en el token JWT
				} catch (error) {
					console.error("Error decodificando el token:", error);
					return null;
				}
			}
			return null;
		},
	},
	methods: {
		async updatePassword() {
			try {
				if (!this.userId) {
					Swal.fire("Error", "No se encontró el ID del usuario. Intenta iniciar sesión nuevamente.", "error");
					return;
				}

				if (!this.currentPassword || !this.newPassword) {
					Swal.fire("Error", "Por favor, completa todos los campos.", "error");
					return;
				}

				if (this.currentPassword === this.newPassword) {
					Swal.fire("Error", "La nueva contraseña no puede ser igual a la actual.", "error");
					return;
				}

				if (!this.token) {
					Swal.fire("Error", "No estás autenticado. Inicia sesión nuevamente.", "error");
					return;
				}

				// Enviar solicitud con el token JWT en los headers
				const response = await axios.post(
					`http://localhost:8000/usuarios/${this.userId}/actualizar_contraseña`,
					{
						contraseñaActual: this.currentPassword,
						nuevaContraseña: this.newPassword,
					},
					{
						headers: {
							Authorization: `Bearer ${this.token}`,
						},
					}
				);

				Swal.fire({
					icon: "success",
					title: "Contraseña actualizada",
					text: response.data.message || "La contraseña se ha actualizado correctamente.",
				});

				// Limpiar los campos después de actualizar
				this.currentPassword = "";
				this.newPassword = "";
			} catch (error) {
				console.error(error);
				Swal.fire({
					icon: "error",
					title: "Error al actualizar",
					text: error.response?.data?.detail || "No se pudo actualizar la contraseña. Intenta de nuevo.",
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
	max-width: 450px;
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