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
.contpri {
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center;

}

.reservas-container {
	width: 90%; /* Ocupa más espacio */
	max-width: 1200px; /* Límite máximo para no estirarse demasiado */
	margin: auto;
	padding: 40px 20px; /* Más padding para mejor espaciado */
	background-color: #F5DEB3; /* Beige Arena como fondo principal */
	border-radius: 15px; /* Bordes redondeados */
	box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Sombra suave */
	position: relative; /* Para posicionar el botón de regresar */
}

.back-button {
	position: absolute;
	top: 20px;
	left: 20px;
	background-color: transparent;
	border: none;
	cursor: pointer;
	transition: transform 0.2s ease;
}

.back-button img {
	width: 30px;
	height: 30px;
}

.back-button:hover {
	transform: scale(1.1);
}

h2 {
	text-align: center;
	color: #6B8E23; /* Verde Oliva para el título */
	font-size: 2rem;
	margin-bottom: 30px;
}

table {
	width: 100%;
	border-collapse: collapse;
	margin-top: 20px;
}

th,
td {
	padding: 12px;
	text-align: left;
	border-bottom: 1px solid #8B5A2B; /* Marrón Tierra para los bordes */
}

th {
	background-color: #6B8E23; /* Verde Oliva para el encabezado */
	color: #FFFFFF; /* Texto blanco para contraste */
	font-weight: bold;
}

tr:hover {
	background-color: #F5DEB3; /* Beige Arena al hacer hover */
}

button {
	padding: 10px 15px;
	background-color: #D4A017; /* Amarillo Mostaza para el botón */
	color: #FFFFFF; /* Texto blanco */
	border: none;
	border-radius: 5px;
	cursor: pointer;
	font-weight: bold;
	transition: background-color 0.3s;
}

button:hover {
	background-color: #8B5A2B; /* Marrón Tierra al hacer hover */
}

.action-button {
	padding: 8px 12px;
	font-size: 14px;
	margin: 5px;
	cursor: pointer;
}

.pagar {
	background-color: #4CAF50; /* Verde para el botón de pagar */
}

.pagar:hover {
	background-color: #45a049; /* Verde más oscuro al hacer hover */
}

.delete {
	background-color: #C1440E; /* Rojo Terracota para el botón de eliminar */
}

.delete:hover {
	background-color: #A8380B; /* Rojo más oscuro al hacer hover */
}

.estado-pagado {
	color: #4CAF50; /* Verde para indicar estado pagado */
	font-weight: bold;
}

@media (max-width: 768px) {
	.reservas-container {
		width: 95%; /* Más ancho en pantallas pequeñas */
		padding: 20px 10px;
	}

	h2 {
		font-size: 1.5rem;
	}

	th,
	td {
		padding: 8px;
		font-size: 14px;
	}

	button {
		padding: 8px 12px;
		font-size: 14px;
	}
}
</style>