<template>
	<div class="contpri">
		<button class="back-button" @click="volver">
			<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
		</button>
		<div class="reservas-container">
			<h2>Mis Reservas</h2>
			<table v-if="reservas.length > 0">
				<thead>
					<tr>
						<th>Fecha</th>
						<th>Tipo de Paquete</th>
						<th>Detalle</th>
						<th>Tipo de Plan</th>
						<th>Estado</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="reserva in reservas" :key="reserva.id">
						<td>{{ reserva.fecha }}</td>
						<td>{{ reserva.tipo_Reserva }}</td>
						<td>{{ reserva.Detalle }}</td>
						<td>{{ reserva.tipo_Plan }}</td>
						<td>
							<button v-if="!reserva.pagada" @click="pagarReserva(reserva.id)"
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
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import Swal from 'sweetalert2';
import { jwtDecode } from 'jwt-decode';

const store = useStore();
const router = useRouter();
const reservas = ref([]);

// Computed que obtiene el ID del usuario:
// Primero, intenta usar el usuario almacenado en Vuex.
// Si no existe, intenta decodificar el token JWT y usa el campo "sub".
const usuarioId = computed(() => {
  if (store.state.usuario && store.state.usuario.id) {
    return store.state.usuario.id;
  } else {
    const token = localStorage.getItem('token');
    if (token) {
      try {
        const decoded = jwtDecode(token);
        return decoded.sub; // Asegúrate de que en el token se usa "sub" para el id
      } catch (error) {
        console.error('Error al decodificar el token:', error);
        return null;
      }
    }
    return null;
  }
});

const volver = () => {
	router.back();
};

const obtenerReservas = async () => {
	try {
		const token = localStorage.getItem('token');
		if (!token) {
			throw new Error("No hay token disponible, inicia sesión.");
		}
		if (!usuarioId.value) {
			throw new Error("No se pudo obtener el ID del usuario.");
		}

		const response = await axios.get(`http://localhost:8000/reservas/${usuarioId.value}/user`, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		reservas.value = response.data;
	} catch (error) {
		console.error("Error al obtener las reservas:", error.response ? error.response.data : error.message);
	}
};

const pagarReserva = async (id) => {
	try {
		const token = localStorage.getItem('token');
		if (!token) throw new Error("No hay token disponible, inicia sesión.");
		const response = await axios.post(`http://localhost:8000/reservas/${id}/pagar`, null, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		if (response.status === 200) {
			const updatedReserva = response.data;
			const index = reservas.value.findIndex(reserva => reserva.id === id);
			if (index !== -1) {
				reservas.value[index] = updatedReserva;
			}
			Swal.fire({
				icon: 'success',
				title: 'Reserva pagada',
				text: 'Tu reserva ha sido pagada exitosamente.',
				confirmButtonText: 'Aceptar'
			});
		}
	} catch (error) {
		Swal.fire({
			icon: 'error',
			title: 'Error',
			text: 'Hubo un problema al intentar pagar la reserva.',
			confirmButtonText: 'Aceptar'
		});
		console.error("Error al pagar la reserva:", error.response ? error.response.data : error.message);
	}
};

const eliminarReserva = async (id) => {
	try {
		const token = localStorage.getItem('token');
		if (!token) throw new Error("No hay token disponible, inicia sesión.");
		const response = await axios.delete(`http://localhost:8000/reservas/${id}`, {
			headers: {
				Authorization: `Bearer ${token}`
			}
		});
		if (response.status === 200) {
			reservas.value = reservas.value.filter(reserva => reserva.id !== id);
			Swal.fire({
				icon: 'success',
				title: 'Reserva eliminada',
				text: 'Tu reserva ha sido eliminada exitosamente.',
				confirmButtonText: 'Aceptar'
			});
		}
	} catch (error) {
		Swal.fire({
			icon: 'error',
			title: 'Error',
			text: 'Hubo un problema al intentar eliminar la reserva.',
			confirmButtonText: 'Aceptar'
		});
		console.error("Error al eliminar la reserva:", error.response ? error.response.data : error.message);
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

.contpri{
	height: 100vh;
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
