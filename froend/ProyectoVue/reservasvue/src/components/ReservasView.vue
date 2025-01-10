<template>
	<div class="contpri">
	<button class="back-button" @click="volver">
		<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<nav class="reservas-container">
		<h2>Reservas de Usuarios</h2>
		<div class="user-table">
			<table>
				<thead>
					<tr>
						<th>ID Reservas</th>
						<th>Cliente</th>
						<th>Fecha</th>
						<th>Tipo PLan</th>
						<th>Nombre Plan</th>
						<th>Estado</th>
						<th>Acciones</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="reserva in reservas" :key="reserva.id">
						<td>{{ reserva.id }}</td>
						<td>{{ reserva.usuario_id }}</td>
						<td>{{ reserva.fecha }}</td>
						<td>{{ reserva.tipo_Plan }}</td>
						<td>{{ reserva.Detalle }}</td>
						<td :class="{'estado-pagado': reserva.pagada, 'estado-pendiente': !reserva.pagada}">
							{{ reserva.pagada ? '✔️ Pagada' : '❌ Pendiente' }}
						</td>

						<td>
							<button @click="eliminarReserva(reserva.id)" class="action-button delete">🗑️</button>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</nav>
	</div>
</template>

<style scoped>
.contpri{
	height: 100vh;
}
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

.estado-pendiente {
	color: red;
	font-weight: bold;
}

.back-button {
	padding: 10px 15px;
	background-color: #4caf50;
	color: white;
	border: none;
	border-radius: 5px;
	cursor: pointer;
	font-weight: bold;
	transition: background-color 0.3s;
}

.back-button:hover {
	background-color: #ff9800;
}
</style>

<script>
import Swal from 'sweetalert2';
export default {
	data() {
		return {
			reservas: [],
		};
	},
	methods: {
		async obtenerReservas() {
			try {
				const response = await fetch('http://127.0.0.1:8000/reservas/');
				if (response.ok) {
					this.reservas = await response.json();
				} else {
					console.error('Error al obtener las reservas:', response.status);
				}
			} catch (error) {
				console.error('Error en la solicitud:', error);
			}
		},
		async eliminarReserva(id) {
			try {
				const response = await fetch(`http://127.0.0.1:8000/reservas/${id}`, {
					method: 'DELETE',
				});
				if (response.ok) {
					this.reservas = this.reservas.filter((reserva) => reserva.id !== id);
					console.log('Reserva eliminada exitosamente');
					Swal.fire({
						icon: 'success',
						title: 'Reserva eliminada',
						text: 'La reserva se ha eliminado exitosamente.',
					});
				} else {
					console.error('Error al eliminar la reserva:', response.status);
				}
			} catch (error) {
				console.error('Error en la solicitud:', error);
			}
		},
		volver() {
			this.$router.back();
		},
	},
	mounted() {
		this.obtenerReservas();
	},
};
</script>
