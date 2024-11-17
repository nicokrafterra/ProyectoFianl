<template>
	<button class="back-button" @click="volver">
		<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<div class="reservas-container">
		<h2>Mis Reservas</h2>
		<table v-if="reservas.length > 0">
			<thead>
				<tr>
					<th>Fecha</th>
					<th>Estado</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="reserva in reservas" :key="reserva.id">
					<td>{{ reserva.fecha }}</td>
					<td>
						<button 
							v-if="!reserva.pagada" 
							@click="pagarReserva(reserva.id)" 
							class="action-button pagar">
							💳 Pagar
						</button>
						<span v-else class="estado-pagado">✔️ Pagada</span>
						<button @click="eliminarReserva(reserva.id)" class="action-button delete">🗑️</button>
					</td>
				</tr>
			</tbody>
		</table>
		<p v-else>No tienes reservas registradas.</p>
	</div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import axios from 'axios';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import Swal from 'sweetalert2';

const store = useStore();
const reservas = ref([]);
const router = useRouter();
const usuario = computed(() => store.state.usuario);

const volver = () => {
	router.back();
};

// Obtener reservas del usuario
const obtenerReservas = async () => {
	try {
		const response = await axios.get(`http://localhost:8000/reservas/${usuario.value.id}/user`);
		reservas.value = response.data;
	} catch (error) {
		console.error("Error al obtener las reservas:", error);
	}
};

// Método para pagar una reserva
const pagarReserva = async (id) => {
	try {
		const response = await axios.post(`http://localhost:8000/reservas/${id}/pagar`);
		if (response.status === 200) {
			// Actualizar el estado de la reserva
			const updatedReserva = response.data;
			const index = reservas.value.findIndex(reserva => reserva.id === id);
			if (index !== -1) {
				reservas.value[index] = updatedReserva;
			}
			
			// Mostrar la alerta de éxito con SweetAlert
			Swal.fire({
				icon: 'success',
				title: 'Reserva pagada',
				text: 'Tu reserva ha sido pagada exitosamente.',
				confirmButtonText: 'Aceptar'
			});
		}
	} catch (error) {
		// Mostrar alerta en caso de error
		Swal.fire({
			icon: 'error',
			title: 'Error',
			text: 'Hubo un problema al intentar pagar la reserva.',
			confirmButtonText: 'Aceptar'
		});
		console.error("Error al pagar la reserva:", error);
	}
};

// Método para eliminar una reserva
const eliminarReserva = async (id) => {
	try {
		const response = await axios.delete(`http://localhost:8000/reservas/${id}`);
		if (response.status === 200) {
			// Eliminar la reserva de la lista local
			reservas.value = reservas.value.filter(reserva => reserva.id !== id);
			
			// Mostrar la alerta de éxito con SweetAlert
			Swal.fire({
				icon: 'success',
				title: 'Reserva eliminada',
				text: 'Tu reserva ha sido eliminada exitosamente.',
				confirmButtonText: 'Aceptar'
			});
		}
	} catch (error) {
		// Mostrar alerta en caso de error
		Swal.fire({
			icon: 'error',
			title: 'Error',
			text: 'Hubo un problema al intentar eliminar la reserva.',
			confirmButtonText: 'Aceptar'
		});
		console.error("Error al eliminar la reserva:", error);
	}
};

onMounted(obtenerReservas);
</script>

<style scoped>
.reservas-container {
	width: 80%;
	margin: auto;
	margin-top: 20px;
	background-color: #f8f9fa;
	padding: 20px;
	border-radius: 10px;
	box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

h2 {
	text-align: center;
	color: #234666;
}

table {
	width: 100%;
	border-collapse: collapse;
	margin-top: 20px;
}

th,
td {
	padding: 10px;
	text-align: left;
	border-bottom: 1px solid #ddd;
}

th {
	background-color: #234666;
	color: #fff;
}

tr:hover {
	background-color: #f1f1f1;
}

button {
	padding: 10px 15px;
	background-color: #4caf50;
	color: white;
	border: none;
	border-radius: 5px;
	cursor: pointer;
	font-weight: bold;
	transition: background-color 0.3s;
}

button:hover {
	background-color: #ff9800;
}

.action-button {
	padding: 8px 12px;
	font-size: 14px;
	margin: 5px;
	cursor: pointer;
}

.pagar {
	background-color: #007bff;
}

.pagar:hover {
	background-color: #0056b3;
}

.delete {
	background-color: #f44336;
}

.delete:hover {
	background-color: #e53935;
}

.estado-pagado {
	color: green;
	font-weight: bold;
}
</style>
