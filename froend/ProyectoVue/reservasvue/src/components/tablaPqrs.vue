<template>
	<div class="contpri">
	<button class="back-button" @click="volver">
		<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<div class="tabla-pqrs">
		<h2>PQRS Recibidos</h2>
		<table>
			<thead>
				<tr>
					<th>ID</th>
					<th>Correo</th>
					<th>Descripción</th>
					<th>Respuesta</th>
					<th>Acciones</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="pqr in pqrs" :key="pqr.id">
					<td>{{ pqr.id }}</td>
					<td>{{ pqr.correo }}</td>
					<td>{{ pqr.descripcion }}</td>
					<td>{{ pqr.respuesta || 'Pendiente' }}</td>
					<td>
						<button @click="responderPqr(pqr)" v-if="!pqr.respuesta">
							✏️ Responder
						</button>
					</td>
				</tr>
			</tbody>
		</table>
		<formRespuestaPqr v-if="pqrSeleccionado" :pqr="pqrSeleccionado" @close="pqrSeleccionado = null" />
	</div>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import formRespuestaPqr from './formRespuestaPqr.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const pqrs = ref([]);
const pqrSeleccionado = ref(null);


const volver = () => {
	router.back();
};


const obtenerPqrs = async () => {
	try {
		const response = await fetch("http://localhost:8000/pqrs/");
		pqrs.value = await response.json();
	} catch (error) {
		console.error("Error al obtener PQRS:", error);
	}
};

const responderPqr = (pqr) => {
	pqrSeleccionado.value = pqr;
};

onMounted(obtenerPqrs);
</script>

<style scoped>

.contpri{
	height: 100vh;
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

.back-button:hover{
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

.tabla-pqrs {
	max-width: 900px;
	margin: auto;
	padding: 20px;
	background: #f2f2f2;
	border-radius: 15px;
	box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.tabla-pqrs h2 {
	text-align: center;
	margin-bottom: 20px;
	color: #333;
	font-size: 24px;
	font-weight: 600;
}

.tabla-pqrs table {
	width: 100%;
	border-collapse: collapse;
	font-size: 16px;
}

.tabla-pqrs th,
.tabla-pqrs td {
	padding: 12px 15px;
	border-bottom: 1px solid #ddd;
	text-align: left;
}

.tabla-pqrs th {
	background-color: #4caf50;
	color: white;
	font-weight: bold;
}

.tabla-pqrs tr:hover {
	background-color: #f1f1f1;
}

.tabla-pqrs button {
	padding: 8px 12px;
	background-color: #4caf50;
	color: white;
	border: none;
	border-radius: 6px;
	cursor: pointer;
	font-size: 14px;
	transition: background-color 0.3s ease;
	display: flex;
	align-items: center;
	justify-content: center;
}

.tabla-pqrs button:hover {
	background-color: #45a049;
}
</style>
