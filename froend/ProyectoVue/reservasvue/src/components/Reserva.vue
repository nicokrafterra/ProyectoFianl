<template>
	<div class="contpri">
		<button class="back-button" @click="volver">
			<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
		</button>
		<div class="reserva-form">
			<div class="form">
				<form @submit.prevent="hacerReserva">
					<h2>Formulario de Reserva</h2>

					<div class="form-group">
						<RouterLink class="reserva-button" to="tpPlan">Selecciona el Tipo de Plan</RouterLink>
					</div>
					<label for="fecha">Fecha de Reserva: </label>
					<div class="form-group">
						<input type="datetime-local" id="fecha" v-model="fecha" :min="minFecha"
						required />
					</div>
					<label for="tipo_Reserva">Tipo de Reserva: </label>
					<div class="form-group">
						<select id="tipo_Reserva" v-model="tipo_Reserva" required>
							<option disabled value="">Selecciona un tipo de reserva</option>
							<option value="basica">Reserva Básica</option>
							<option value="premium">Reserva Premium</option>
						</select>
					</div>

					<div v-if="descripcionReserva" class="texto-descriptivo">
						<p>{{ descripcionReserva }}</p>
					</div>


					<button type="submit" class="reserva-button">Hacer Reserva</button>
					<button class="ver-reservas-button" @click="verReservas">Ver todas mis reservas</button>
				</form>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { jwtDecode } from 'jwt-decode';// Importación correcta
import Swal from 'sweetalert2';

const router = useRouter();
const fecha = ref('');
const tipo_Reserva = ref('');
const tipo_Plan = ref('');
const minFecha = ref('');
const usuarioId = ref(null);
const tipoPlan = ref(null);

// 🔹 Obtener el ID de usuario desde el token JWT usando "sub"
const obtenerUsuarioDesdeJWT = () => {
	const token = localStorage.getItem('token');
	if (token) {
		try {
			const decodedToken = jwtDecode(token);
			// Usa "sub" (como se definió en el token) en lugar de "user_id"
			usuarioId.value = decodedToken.sub;
			if (!usuarioId.value) {
				console.error('El token no contiene "sub".');
			}
		} catch (error) {
			console.error('Error al decodificar el token:', error);
			usuarioId.value = null;
		}
	}
};

// 🔹 Obtener el tipo de plan desde el almacenamiento local (simulando Vuex)
const obtenerTipoPlan = () => {
	const planGuardado = localStorage.getItem('tipoPlan');
	if (planGuardado) {
		tipoPlan.value = JSON.parse(planGuardado);
	}
};

// 🔹 Establecer la fecha mínima (10:00 AM del día actual)
minFecha.value = (() => {
	const ahora = new Date();
	const fechaMinima = new Date(ahora.getFullYear(), ahora.getMonth(), ahora.getDate(), 10, 0, 0);
	return fechaMinima.toISOString().slice(0, 16);
})();

// 🔹 Función para volver a la pantalla principal
const volver = () => {
	router.push('/index');
};

// 🔹 Computed para mostrar la descripción del tipo de reserva
const descripcionReserva = computed(() => {
	if (tipo_Reserva.value === 'basica') {
		return "La reserva básica ofrece acceso estándar a nuestras instalaciones con un costo más económico.";
	} else if (tipo_Reserva.value === 'premium') {
		return "La reserva premium incluye servicios exclusivos como acceso VIP y opciones personalizadas.";
	}
	return "";
});

// 🔹 Función para hacer la reserva
const hacerReserva = async () => {
	if (!usuarioId.value) {
		Swal.fire({
			icon: 'warning',
			title: 'Sesión no válida',
			text: 'Debes iniciar sesión para realizar una reserva.',
			confirmButtonColor: '#d33',
		});
		return;
	}

	if (!tipoPlan.value || !tipoPlan.value.tipo) {
		Swal.fire({
			icon: 'warning',
			title: 'Selección de Plan',
			text: 'Por favor, selecciona el tipo de plan que deseas.',
			confirmButtonColor: '#d33',
		});
		return;
	}

	const reservaData = {
		usuario_id: usuarioId.value,
		plan_id: tipoPlan.value.id,
		fecha: fecha.value,
		tipo_Reserva: tipo_Reserva.value,
		tipo_Plan: tipoPlan.value.tipo,
		Detalle: tipoPlan.value.nombre,
		pagada: false,
	};

	console.log("Datos enviados:", reservaData);

	try {
		const token = localStorage.getItem('token');
		const response = await fetch('http://localhost:8000/reservas/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`, // Se incluye el token JWT
			},
			body: JSON.stringify(reservaData),
		});

		if (!response.ok) {
			const errorData = await response.json();
			console.error("Detalles del error:", errorData);
			throw new Error('Error al hacer la reserva');
		}

		const data = await response.json();
		console.log('Reserva exitosa:', data);

		fecha.value = '';
		tipo_Reserva.value = '';
		tipo_Plan.value = '';

		localStorage.removeItem("tipoPlan");

		Swal.fire({
			icon: 'success',
			title: 'Reserva exitosa',
			text: 'Tu reserva ha sido realizada con éxito.',
			confirmButtonColor: '#3085d6',
		});
	} catch (error) {
		console.error('Error:', error);
		Swal.fire({
			icon: 'error',
			title: 'Error',
			text: 'No se pudo realizar la reserva. Intenta nuevamente.',
			confirmButtonColor: '#d33',
		});
	}
};

// 🔹 Función para ver reservas
const verReservas = () => {
	router.push('/ResVer');
};

// 🔹 Recuperar datos al montar el componente
onMounted(() => {
	obtenerUsuarioDesdeJWT();
	obtenerTipoPlan();
});
</script>





<style scoped>
.contpri {
	height: 100vh;
	display: flex;
	justify-content: center;
}

.back-button {
	position: absolute;
	top: 20px;
	left: 20px;
	background: none;
	border: none;
	cursor: pointer;
	transition: 0.35s;
	height: 40px;
	width: 60px;
}

.back-button:hover {
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


.reserva-message {
	margin-top: 20px;
	color: #707070;
	font-size: 14px;
}

.reserva-button {
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
	width: 250px;
}

.reserva-button:hover {
	transform: scale(1.01);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	background-color: #002e02;
	margin-right: 1px;
}

body {
	height: 100vh;
	overflow: hidden;
	font-family: "Poppins", sans-serif;
	display: flex;
	background-size: cover;
}

.reserva-form {
	width: 400px;
}

.form {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	position: absolute;
	margin-top: 70px;
	backface-visibility: hidden;
	padding: 65px 45px;
	border-radius: 15px;
	box-shadow: inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	backdrop-filter: blur(10px);
}

.form input,
.form select {
	width: 254px;
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



.form .ver-reservas-button {
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
	margin-left: 10px;
	width: 250px;
}

.form .ver-reservas-button:hover {
	transform: scale(1.01);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	background-color: #002e02;
	margin-left: 11px;
}

.form-group {
	margin: 20px;
	justify-content: center;
	align-items: center;
	display: flex;
	margin-left: auto;
	margin-right: auto;
}

.texto-descriptivo {
	margin: 20px;
	justify-content: center;
	align-items: center;
	display: flex;
	width: 400px;
	text-align: center;
}

#tipo_Reserva {
	width: 320px;
}

#fecha {
	width: 310px;
}

@media (max-width: 768px) {
	.form {
		padding: 20px;
	}

	.form input,
	.form select {
		max-width: 100%;
	}

	.reserva-button,
	.ver-reservas-button {
		max-width: 100%;
	}
}

@media (max-width: 480px) {
	.form {
		padding: 15px;
	}

	.form input,
	.form select {
		font-size: 14px;
		padding: 5px;
	}

	.reserva-button,
	.ver-reservas-button {
		font-size: 14px;
		padding: 8px 20px;
	}

	.texto-descriptivo {
		font-size: 12px;
	}
}
</style>
