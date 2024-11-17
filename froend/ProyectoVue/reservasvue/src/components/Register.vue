<template>
	<div class="container">
		<div class="form">
			<form @submit.prevent="handleRegister" class="form_front">
				<h2 class="form_details">Registrate</h2>

				<input type="text" v-model="nombre" placeholder="Nombre *" required class="input" />
				<div v-if="nombreError" style="color: red">{{ nombreError }}</div>

				<input type="text" v-model="apellido" placeholder="Apellido *" required class="input" />
				<div v-if="apellidoError" style="color: red">{{ apellidoError }}</div>

				<input type="email" v-model="email" placeholder="Email *" required class="input" />
				<div v-if="emailError" style="color: red">{{ emailError }}</div>

				<input type="password" v-model="password" placeholder="Password *" required class="input" />
				<div v-if="passwordError" style="color: red">{{ passwordError }}</div>

				<input type="password" v-model="vpassword" placeholder="Confirmar Password *" required class="input" />
				<div v-if="vpasswordError" style="color: red">{{ vpasswordError }}</div>

				<input type="text" v-model="numeroCelular" placeholder="Número de Celular *" required class="input" />
				<div v-if="celularError" style="color: red">{{ celularError }}</div>

				<button type="submit" class="btn-reg">Crear</button>
				<p class="switch">
					¿Ya tienes una cuenta?
					<RouterLink to="/Iniciar" class="signup_tog">Inicia Sesión</RouterLink>
				</p>
			</form>



		</div>
	</div>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";
import { mapActions } from "vuex";

export default {
	data() {
		return {
			nombre: "",
			apellido: "",
			email: "",
			password: "",
			vpassword: "",
			numeroCelular: "",
			nombreError: "",
			apellidoError: "",
			emailError: "",
			passwordError: "",
			vpasswordError: "",
			celularError: "",
		};
	},
	methods: {
		clearErrors() {
			this.nombreError = "";
			this.apellidoError = "";
			this.emailError = "";
			this.passwordError = "";
			this.vpasswordError = "";
			this.celularError = "";
		},
		validateNombre(nombre) {
			const nombreRegex = /^[a-zA-Z\s]+$/;
			return nombreRegex.test(nombre);
		},
		validateEmail(email) {
			const emailPattern =
				/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
			return emailPattern.test(email);
		},
		validatePassword(password) {
			const passwordRegex =
				/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d{3,})(?=.*[!@#$%^&*_-])[A-Za-z\d!@#$%^&*_-]{8,}$/;
			return passwordRegex.test(password);
		},
		validateNumeroCelular(numero) {
			return numero.length >= 10;
		},
		...mapActions(["registerUsuario"]),
		async handleRegister() {
			this.clearErrors();

			let valid = true;

			if (!this.nombre) {
				this.nombreError = "El nombre es obligatorio.";
				valid = false;
			} else if (!this.validateNombre(this.nombre) || this.nombre.length <= 1) {
				this.nombreError = "El nombre debe contener al menos 2 letras.";
				valid = false;
			}

			if (!this.apellido) {
				this.apellidoError = "El apellido es obligatorio.";
				valid = false;
			} else if (!this.validateNombre(this.apellido) || this.apellido.length <= 1) {
				this.apellidoError = "El apellido debe contener al menos 2 letras.";
				valid = false;
			}

			if (!this.email) {
				this.emailError = "El correo electrónico es obligatorio.";
				valid = false;
			} else if (!this.validateEmail(this.email)) {
				this.emailError = "Por favor, introduce un correo electrónico válido.";
				valid = false;
			}

			if (!this.password) {
				this.passwordError = "La contraseña es obligatoria.";
				valid = false;
			} else if (!this.validatePassword(this.password)) {
				this.passwordError =
					"La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una minúscula, 3 números y un carácter especial.";
				valid = false;
			}

			if (this.password !== this.vpassword) {
				this.vpasswordError = "Las contraseñas no coinciden.";
				valid = false;
			}

			if (
				!this.numeroCelular ||
				!this.validateNumeroCelular(this.numeroCelular)
			) {
				this.celularError =
					"Por favor, introduce un número de celular válido (mínimo 10 dígitos).";
				valid = false;
			}

			if (valid) {
				const esAdmin = this.email.endsWith(".ad");

				try {
					const response = await axios.post(
						"http://localhost:8000/usuarios/",
						{
							nombre: this.nombre,
							apellido: this.apellido,
							correoElectronico: this.email,
							contraseñaUsuario: this.password,
							numeroCelular: this.numeroCelular,
							esAdmin: esAdmin,
						}
					);

					this.registerUsuario(response.data);
					Swal.fire({
						icon: "success",
						title: "¡Bienvenido!",
						text: "Te has registrado exitosamente. Redirigiendo...",
						background: "#e0f7fa",
						color: "#004d40",
						showConfirmButton: false,
						timer: 3000,
					});

					setTimeout(() => {
						if (esAdmin) {
							this.$router.push("/VistaAd");
						} else {
							this.$router.push("/index");
						}
					}, 3000);
				} catch (error) {
					console.error("Error al registrar el usuario:", error);
					Swal.fire({
						icon: "error",
						title: "Error al registrar",
						text: "Ocurrió un error al intentar registrar el usuario",
						background: "#ffebee",
						color: "#b71c1c",
					});
				}
			}
		},
	},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap");

.container {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;
}

.form {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	transform-style: preserve-3d;
	transition: all 1s ease;
}

.form .form_front {
	margin-top: 40px;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	width: 400px;
	height: 500px;
	gap: 20px;
	position: absolute;
	backface-visibility: hidden;
	padding: 65px 45px;
	border-radius: 15px;
	box-shadow: inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	backdrop-filter: blur(10px);
}

.input {
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

.input::placeholder {
	color: #999;
}

.input:focus {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
}

.btn-reg {
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

.btn-reg:hover {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
}

.switch {
	font-size: 13px;
	color: white;
}

.signup_tog {
	font-weight: 700;
	cursor: pointer;
	text-decoration: none;
	color: #fff;
}

.signup_tog:hover {
	text-decoration: underline;
}

</style>
