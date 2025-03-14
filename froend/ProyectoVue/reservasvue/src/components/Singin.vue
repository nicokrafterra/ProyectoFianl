<template>
	<div class="container">
		<div class="form">
			<div class="form_front">
				<h2 class="form_details"><i class="fas fa-lock"></i> Inicia Sesión</h2>
				<input class="input" type="email" v-model="email" placeholder="Email" required />
				<div v-if="loginError" style="color: red">{{ loginError }}</div>

				<input class="input" type="password" v-model="password" placeholder="Password" required />
				<div v-if="loginPasswordError" style="color: red">{{ loginPasswordError }}</div>

				<button class="btn" type="submit" @click.prevent="handleLogin">Inicia Sesión</button>
				<p class="switch">
					¿Aún no tienes cuenta?
					<RouterLink to="/Registrar" class="signup_tog">Regístrate</RouterLink>
				</p>
				<p class="switch">
					¿No recuerdas tu contraseña?
					<RouterLink to="/RecuperarPasword" class="singup_top">Recuperar</RouterLink>
				</p>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";
import { mapActions } from "vuex";
import { jwtDecode } from "jwt-decode";
import api from "@/axiosConfig";

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

			if (!this.email) {
				this.loginError = "El email es obligatorio.";
				return;
			}
			if (!this.password) {
				this.loginPasswordError = "La contraseña es obligatoria.";
				return;
			}

			try {
				const response = await api.post("/login", {
					nombre_usuario: this.email,
					password: this.password,
				});

				if (response.status === 200) {
					const token = response.data.access_token;

					if (typeof token === "string" && token.trim().length > 0) {
						localStorage.setItem("token", token);
						this.loginUsuario(token);

						// 🔹 Nueva solicitud a /protegido después del login exitoso
						this.verificarAccesoProtegido();

						Swal.fire({
							icon: "success",
							title: "¡Bienvenido!",
							text: "Tu inicio de sesión ha sido exitoso. Redirigiendo...",
							background: "#e0f7fa",
							color: "#004d40",
							showConfirmButton: false,
							timer: 3000,
						});

						setTimeout(() => {
							if (this.email.endsWith(".ad")) {
								this.$router.push("/VistaAd");
							} else {
								this.$router.push("/index");
							}
						}, 1000);
					} else {
						this.loginError = "El token proporcionado no es válido.";
					}
				}
			} catch (error) {
				if (error.response) {
					if (error.response.status === 401) {
						this.loginError = "Credenciales incorrectas. Intenta de nuevo.";
					} else if (error.response.status === 400) {
						this.loginError = "Solicitud incorrecta. Verifica los datos.";
					} else {
						this.loginError = "Error al iniciar sesión. Inténtalo más tarde.";
					}
				} else {
					this.loginError = "No se pudo conectar con el servidor.", error;
				}

				Swal.fire({
					icon: "error",
					title: "Error al iniciar sesión",
					text: this.loginError,
					background: "#ffebee",
					color: "#b71c1c",
				});
			}
		},

		// 🔹 Nueva función para verificar acceso a ruta protegida
		async verificarAccesoProtegido() {
			try {
				const token = localStorage.getItem("token");
				if (!token) {
					console.warn("⚠️ No hay token disponible.");
					return;
				}

				const response = await axios.get("http://localhost:8000/protegido", {
					headers: {
						"Authorization": `Bearer ${token}`,
					},
				});

				console.log("✅ Acceso a datos protegidos:", response.data);
			} catch (error) {
				console.error("❌ Error al acceder a la ruta protegida:", error);
			}
		},
	},
};
</script>



<style scoped>
/* Importación de estilos proporcionados */
@import url(https://fonts.googleapis.com/css?family=Poppins:300);

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
	width: 100%;
	background-color: var(--marron-tierra); /* Fondo con Marrón Tierra */
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

.btn {
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

.btn:hover {
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
</style>