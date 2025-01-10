<template>
	<div class="contpri">
		<button class="back-button" @click="volver">
			<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
		</button>
		<div class="form">
			<h2>Añadir Plan</h2>
			<form @submit.prevent="agregarPlan">
				<div class="form-group">
					<label for="nombre">Nombre:</label>
					<input v-model="nombre" type="text" id="nombre" required maxlength="50" placeholder="Nombre del plan" />
				</div>
				<div class="form-group">
					<label for="cantidad_m">Cantidad Máxima:</label>
					<input
						v-model.number="cantidad_maxima"
						type="number"
						id="cantidad_m"
						required
						min="1"
						max="1000"
						placeholder="Cantidad máxima de participantes"
					/>
				</div>
				<div class="form-group">
					<label for="tipo_Plan">Tipo Plan:</label>
					<select v-model="tipo_Plan" id="tipo_Plan" required>
						<option disabled value="">Seleccione un tipo</option>
						<option value="Recorrido">Recorrido</option>
						<option value="Mesa">Mesa</option>
						<option value="Camping">Camping</option>
						<option value="Evento">Evento</option>
					</select>
				</div>
				<div class="form-group">
					<label for="descripcion">Descripción:</label>
					<textarea
						v-model="descripcion"
						id="descripcion"
						required
						maxlength="500"
						placeholder="Descripción del plan"
					></textarea>
				</div>
				<button type="submit" :disabled="loading" class="reserva-button">
					{{ loading ? "Guardando..." : "Agregar Plan" }}
				</button>
				<button @click="verPlanes" class="reserva-button">Ver Planes</button>
			</form>
			
		</div>
	</div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import Swal from "sweetalert2";

const nombre = ref("");
const cantidad_maxima = ref(null);
const tipo_Plan = ref("");
const descripcion = ref("");
const loading = ref(false);

const router = useRouter();

const volver = () => {
	router.back();
};

const agregarPlan = async () => {
	const planData = {
		nombre: nombre.value,
		descripcion: descripcion.value,
		tipo: tipo_Plan.value,
		cantidad_maxima: cantidad_maxima.value,
	};

	loading.value = true;

	try {
		const response = await axios.post("http://localhost:8000/planes", planData);

		if (!response.ok) {
			throw new Error("Error al agregar el plan");
		} else {
			Swal.fire({
				icon: "success",
				title: "¡Plan añadido con éxito!",
				text: "El plan ha sido registrado correctamente.",
				confirmButtonText: "Aceptar",
			});
			limpiarFormulario();
		}
	} catch (error) {
		Swal.fire({
			icon: "error",
			title: "Error",
			text: "Ocurrió un error al añadir el plan. Por favor, inténtalo de nuevo.",
			confirmButtonText: "Aceptar",
		});
		console.error(error);
	} finally {
		loading.value = false;
	}
};

const limpiarFormulario = () => {
	nombre.value = "";
	cantidad_maxima.value = null;
	tipo_Plan.value = "";
	descripcion.value = "";
};

const verPlanes = () => {
	router.push("/planVer");
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

.form {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	position: relative;
	margin-top: 70px;
	backface-visibility: hidden;
	padding: 65px 45px;
	border-radius: 15px;
	box-shadow: inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	backdrop-filter: blur(10px);
	background-color: rgba(33, 33, 33, 0.8);
	
}

.form-group {
	margin: 20px;
	justify-content: center;
	align-items: center;
	display: flex;
	flex-direction: column;
}

label {
	color: #fff;
	font-weight: bold;
	margin-bottom: 5px;
}

input,
textarea,
select {
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
	width: 250px;
	margin-left: 20px;
}

.reserva-button:hover {
	transform: scale(1.01);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	background-color: #002e02;
}
</style>
