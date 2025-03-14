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
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { jwtDecode } from 'jwt-decode';

const correo = ref('');
const descripcion = ref('');
const mensaje = ref('');
const usuarioId = ref(null);

const router = useRouter();

// 🔹 Obtener el ID de usuario desde el token JWT
const obtenerUsuarioDesdeJWT = () => {
	const token = localStorage.getItem('token');

	if (!token) {
		console.error('⚠️ No se encontró el token en localStorage.');
		return;
	}

	try {
		const decodedToken = jwtDecode(token);
		console.log('🔍 Token decodificado:', decodedToken); // 👉 Depuración

		if (!decodedToken.sub) {
			console.error('⚠️ El token no contiene "user_id". Verifica la estructura del token.');
			return;
		}

		usuarioId.value = decodedToken.sub;
	} catch (error) {
		console.error('❌ Error al decodificar el token:', error);
	}
};

// 🔹 Enviar PQR con JWT
const enviarPqr = async () => {
	if (!usuarioId.value) {
		mensaje.value = 'Error: No se pudo obtener la información del usuario. Inicia sesión nuevamente.';
		return;
	}

	const pqrData = {
		usuario_id: usuarioId.value,
		correo: correo.value,
		descripcion: descripcion.value,
	};

	try {
		const response = await fetch('http://localhost:8000/pqr/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${localStorage.getItem('token')}`, // 🔹 Token JWT en la cabecera
			},
			body: JSON.stringify(pqrData),
		});

		if (!response.ok) {
			throw new Error('Error al enviar el PQR');
		}

		mensaje.value = '✅ PQR enviado exitosamente';
		correo.value = '';
		descripcion.value = '';
	} catch (error) {
		console.error('Error:', error);
		mensaje.value = '❌ No se pudo enviar el PQR. Intenta nuevamente.';
	}
};

// 🔹 Recuperar el ID del usuario cuando se monta el componente
onMounted(() => {
	obtenerUsuarioDesdeJWT();
});

// 🔹 Función para volver atrás
const volver = () => {
	router.go(-1);
};
</script>


<style scoped>
.contpri {
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center;
 /* Beige Arena como fondo principal */
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
	background-color: #f5deb3e6; /* Fondo blanco para el formulario */
	box-shadow: inset 2px 2px 10px rgba(0, 0, 0, 0.2),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	backdrop-filter: blur(10px);
	border: 1px solid #8B5A2B; /* Marrón Tierra para el borde */
}

h2 {
	color: #6B8E23; /* Verde Oliva para el título */
	font-size: 24px;
	margin-bottom: 20px;
}

.form-group {
	margin-bottom: 20px;
	text-align: left;
}

label {
	font-weight: bold;
	color: #6B8E23; /* Verde Oliva para las etiquetas */
	display: block;
	margin-bottom: 8px;
}

input[type="email"],
textarea {
	width: 245px;
	min-height: 45px;
	color: #212121; /* Texto oscuro para contraste */
	outline: none;
	transition: 0.35s;
	padding: 0px 7px;
	background-color: #FFFFFF; /* Fondo blanco para los inputs */
	border-radius: 6px;
	border: 2px solid #8B5A2B; /* Marrón Tierra para el borde */
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.1),
		1px 1px 10px rgba(255, 255, 255, 0.6);
}

input[type="email"]:focus,
textarea:focus {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.2),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 0.2),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	border-color: #D4A017; /* Amarillo Mostaza al enfocar */
}

textarea {
	resize: vertical;
	min-height: 100px;
}

.btn {
	padding: 10px 35px;
	cursor: pointer;
	background-color: #6B8E23; /* Verde Oliva para el botón */
	border-radius: 6px;
	border: 2px solid #6B8E23; /* Verde Oliva para el borde */
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.1),
		1px 1px 10px rgba(255, 255, 255, 0.6);
	color: #FFFFFF; /* Texto blanco para contraste */
	font-size: 15px;
	font-weight: bold;
	transition: 0.35s;
}

.btn:hover {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.2),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 0.2),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	background-color: #8B5A2B; /* Marrón Tierra al hacer hover */
	border-color: #8B5A2B; /* Marrón Tierra al hacer hover */
}

.mensaje {
	margin-top: 20px;
	color: #C1440E; /* Rojo Terracota para mensajes de error */
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

.back-button:hover {
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.2),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 0.2),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	background-color: #6B8E23; /* Verde Oliva al hacer hover */
	border-radius: 6px;
}

.back-button img {
	width: 24px;
	height: 24px;
	transition: transform 0.2s ease;
}

/* Animación de entrada */
.pqr-form {
    animation: zoomRotateIn 1s ease-out;
}

@keyframes zoomRotateIn {
    from {
        opacity: 0;
        transform: scale(0.5) rotate(-10deg); /* Zoom reducido y ligero giro */
    }
    to {
        opacity: 1;
        transform: scale(1) rotate(0deg); /* Estado final: tamaño normal y sin giro */
    }
}
</style>