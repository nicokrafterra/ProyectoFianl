<template>
	<div class="container">
		<div class="form">
			<form @submit.prevent="handleRegister" class="form_front">
				<h2 class="form_details">Regístrate</h2>

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
			const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
			return emailPattern.test(email);
		},
		validatePassword(password) {
			const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d{3,})(?=.*[!@#$%^&*_-])[A-Za-z\d!@#$%^&*_-]{8,}$/;
			return passwordRegex.test(password);
		},
		validateNumeroCelular(numero) {
			const numeroRegex = /^[0-9]+$/;
			return numeroRegex.test(numero) && numero.length >= 10;
		},
		async handleRegister() {
			this.clearErrors();

			let valid = true;

			// Validaciones
			if (!this.nombre || !this.validateNombre(this.nombre)) {
				this.nombreError = "El nombre debe contener al menos 2 letras.";
				valid = false;
			}
			if (!this.apellido || !this.validateNombre(this.apellido)) {
				this.apellidoError = "El apellido debe contener al menos 2 letras.";
				valid = false;
			}
			if (!this.email || !this.validateEmail(this.email)) {
				this.emailError = "Por favor, introduce un correo electrónico válido.";
				valid = false;
			}
			if (!this.password || !this.validatePassword(this.password)) {
				this.passwordError =
					"La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula, 3 números y un carácter especial.";
				valid = false;
			}
			if (this.password !== this.vpassword) {
				this.vpasswordError = "Las contraseñas no coinciden.";
				valid = false;
			}
			if (!this.numeroCelular || !this.validateNumeroCelular(this.numeroCelular)) {
				this.celularError = "Número de celular inválido (mínimo 10 dígitos).";
				valid = false;
			}

			if (valid) {
				try {
					const response = await axios.post("http://localhost:8000/usuarios/", {
						nombre: this.nombre,
						apellido: this.apellido,
						correoElectronico: this.email,
						contraseñaUsuario: this.password,
						numeroCelular: this.numeroCelular,
					});

					// Guardar el token en localStorage
					const token = response.data.access_token;
					localStorage.setItem("token", token);

					Swal.fire({
						icon: "success",
						title: "¡Registro exitoso!",
						text: "Te has registrado correctamente. Redirigiendo...",
						background: "#e0f7fa",
						color: "#004d40",
						showConfirmButton: false,
						timer: 3000,
					});

					setTimeout(() => {
						this.$router.push("/index"); // Redirigir al usuario
					}, 1000);
				} catch (error) {
					if (error.response && error.response.data) {
						this.emailError = error.response.data.detail || "Error al registrar usuario.";
					}
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

:root {
	--verde-oliva: #6B8E23;
	--marron-tierra: #8B5A2B;
	--beige-arena: #F5DEB3;
	--rojo-terracota: #C1440E;
	--amarillo-mostaza: #D4A017;
	--texto: #fff;
	--fondo: #212121;
}

.container {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;
	background-color: var(--marron-tierra); /* Fondo con Marrón Tierra */
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
	box-shadow: inset 2px 2px 10px rgba(0, 0, 0, 0.5),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	backdrop-filter: blur(10px);
	background-color: var(--beige-arena); /* Fondo del formulario con Beige Arena */
}

.input {
	width: 245px;
	min-height: 45px;
	color: var(--texto); /* Texto en blanco */
	outline: none;
	transition: 0.35s;
	padding: 0px 7px;
	background-color: var(--fondo); /* Fondo del input con Marrón Tierra */
	border-radius: 6px;
	border: 2px solid var(--rojo-terracota); /* Borde con Rojo Terracota */
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.5),
		1px 1px 10px rgba(255, 255, 255, 0.6);
}

.input::placeholder {
	color: var(--amarillo-mostaza); /* Placeholder con Amarillo Mostaza */
}

.input:focus {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.5),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 0.5),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
}

.btn-reg {
	padding: 10px 35px;
	cursor: pointer;
	background-color: var(--rojo-terracota); /* Fondo del botón con Rojo Terracota */
	border-radius: 6px;
	border: 2px solid var(--rojo-terracota); /* Borde con Rojo Terracota */
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.5),
		1px 1px 10px rgba(255, 255, 255, 0.6);
	color: var(--texto); /* Texto en blanco */
	font-size: 15px;
	font-weight: bold;
	transition: 0.35s;
}

.btn-reg:hover {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.5),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 0.5),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
}

.switch {
	font-size: 13px;
	color: var(--texto); /* Texto en blanco */
}

.signup_tog {
	font-weight: 700;
	cursor: pointer;
	text-decoration: none;
	color: var(--amarillo-mostaza); /* Enlace con Amarillo Mostaza */
}

.signup_tog:hover {
	text-decoration: underline;
}

/*------------------- responsive ---------------------*/
@media (max-width: 768px) {
    .container {
        padding: 10px;
    }

    .form .form_front {
        height: auto;
        padding: 30px 20px;
        gap: 15px;
        box-shadow: inset 1px 1px 5px rgba(0, 0, 0, 0.5),
            inset -1px -1px 3px rgba(255, 255, 255, 0.4);
    }

    .input {
        width: 100%; /* Ocupa todo el ancho disponible */
        font-size: 14px; /* Ajusta el tamaño de fuente */
        min-height: 40px;
    }

    .btn-reg {
        padding: 8px 20px;
        font-size: 14px;
    }

    .switch {
        font-size: 12px; /* Escala el texto para dispositivos más pequeños */
        text-align: center;
    }
}

/* agregado extra animated------------- */
.form_front {
    animation: slideIn 1s ease-in-out;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>

