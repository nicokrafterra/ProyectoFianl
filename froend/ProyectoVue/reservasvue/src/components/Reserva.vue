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
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import Swal from 'sweetalert2';

const store = useStore();
const router = useRouter();

const usuario = computed(() => store.state.usuario);

const tipoPlan = computed(() => store.getters.obtenerTipoPlan);

const fecha = ref('');
const tipo_Reserva = ref('');
const tipo_Plan = ref('');
const minFecha = ref('');

// Dentro de setup()
minFecha.value = (() => {
    // Crea una nueva fecha con cualquier fecha que se pase, pero establece la hora a las 10:00 AM
    const ahora = new Date();
    // Establecer la fecha actual (sin importar la hora) a las 10 AM
    const fechaMinima = new Date(ahora.getFullYear(), ahora.getMonth(), ahora.getDate(), 10, 0, 0);
    return fechaMinima.toISOString().slice(0, 16); // Retorna la fecha con hora mínima a las 10 AM
})();


const volver = () => {
	router.push('/index');
};


const descripcionReserva = computed(() => {
	if (tipo_Reserva.value === 'basica') {
		return "La reserva básica ofrece acceso estándar a nuestras instalaciones con un costo más económico.";
	} else if (tipo_Reserva.value === 'premium') {
		return "La reserva premium incluye servicios exclusivos como acceso VIP y opciones personalizadas.";
	}
	return "";
});

const hacerReserva = async () => {
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
		usuario_id: usuario.value.id,
		plan_id: tipoPlan.value.id,
		fecha: fecha.value,
		tipo_Reserva: tipo_Reserva.value,
		tipo_Plan: tipoPlan.value.tipo,
		Detalle: tipoPlan.value.nombre,
		pagada: false,
	};


	console.log("Datos enviados:", reservaData);

	try {
		const response = await fetch('http://localhost:8000/reservas/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
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

		store.dispatch("resetTipoPlan");

		console.log(store.state.tipoPlan);
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
}


const verReservas = () => {
	router.push('/ResVer');
};

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
