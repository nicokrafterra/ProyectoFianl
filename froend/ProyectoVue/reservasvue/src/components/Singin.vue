<template>
	<div class="container">
		<div class="form">
			<div class="form_front">
				<h2 class="form_details"><i class="fas fa-lock"></i> Inicia Sesión</h2>
				<input class="input" type="email" v-model="email" placeholder="Email" required />
				<div v-if="loginError" style="color: red">{{ loginError }}</div>

				<input class="input" type="password" v-model="password" placeholder="Password" required />
				<div v-if="loginPasswordError" style="color: red">
					{{ loginPasswordError }}
				</div>

				<button class="btn" type="submit" @click.prevent="handleLogin">
					Inicia Sesión
				</button>
				<p class="switch">
					¿Aún no tienes cuenta?
					<RouterLink to="/Registrar" class="signup_tog">Regístrate</RouterLink>
				</p>
			</div>
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
			email: "",
			password: "",
			loginError: "",
			loginPasswordError: "",
		};
	},
	methods: {
		clearErrors() {
			this.loginError = "";
			this.loginPasswordError = "";
		},
		...mapActions(["loginUsuario"]),
		async handleLogin() {
			this.clearErrors();
			try {
				const response = await axios.post("http://localhost:8000/login", {
					nombre_usuario: this.email,
					password: this.password,
				});

				this.loginUsuario(response.data);

				const esAdmin = response.data.esAdmin;

				Swal.fire({
					icon: "success",
					title: "¡Bienvenido!",
					text: "Tu inicio de sesión ha sido exitoso. Redirigiendo...",
					background: "#e0f7fa",
					color: "#004d40",
					showConfirmButton: false,
					timer: 3000,
					customClass: {
						popup: "my-swal-popup",
					},
				});

				setTimeout(() => {
					if (esAdmin) {
						this.$router.push("/VistaAd");
					} else {
						this.$router.push("/index");
					}
				}, 1000);
			} catch (error) {
				Swal.fire({
					icon: "error",
					title: "Error al iniciar sesión",
					text: "Verifica tus credenciales e intenta nuevamente.",
					background: "#ffebee",
					color: "#b71c1c",
				});
			}
		},
	},
};
</script>

<style scoped>
/* Importación de estilos proporcionados */
@import url(https://fonts.googleapis.com/css?family=Poppins:300);

.container {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;
	width: 100%;

}

.form {
	display: flex;
	justify-content: center;
	align-items: center;
	transform-style: preserve-3d;
	transition: all 1s ease;
}

.form_front {
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
