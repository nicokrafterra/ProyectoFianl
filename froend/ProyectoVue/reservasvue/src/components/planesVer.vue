<template>
	<button class="back-button" @click="volver">
		<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<nav class="planes-container">
		<h2>Gestión de Planes</h2>
		<div class="plan-table">
			<table>
				<thead>
					<tr>
						<th>ID Plan</th>
						<th>Nombre</th>
						<th>Tipo</th>
						<th>Cantidad Máxima</th>
						<th>Acciones</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="plan in planes" :key="plan.id">
						<td>{{ plan.id }}</td>
						<td>{{ plan.nombre }}</td>
						<td>{{ plan.tipo }}</td>
						<td>{{ plan.cantidad_maxima }}</td>
						<td>
							<button @click="eliminarPlan(plan.id)" class="action-button delete">🗑️</button>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</nav>
</template>

<script>
import Swal from 'sweetalert2';
export default {
	data() {
		return {
			planes: [],
		};
	},
	methods: {
		// Método para obtener los planes
		async obtenerPlanes() {
			try {
				const response = await fetch('http://127.0.0.1:8000/planes/');
				if (response.ok) {
					this.planes = await response.json();
				} else {
					console.error('Error al obtener los planes:', response.status);
				}
			} catch (error) {
				console.error('Error en la solicitud:', error);
			}
		},
		// Método para eliminar un plan por ID
		async eliminarPlan(id) {
			try {
				Swal.fire({
					title: '¿Estás seguro?',
					text: 'No podrás deshacer esta acción.',
					icon: 'warning',
					showCancelButton: true,
					confirmButtonColor: '#d33',
					cancelButtonColor: '#3085d6',
					confirmButtonText: 'Sí, eliminar',
					cancelButtonText: 'Cancelar',
				}).then(async (result) => {
					if (result.isConfirmed) {
						const response = await fetch(`http://127.0.0.1:8000/planes/${id}`, {
							method: 'DELETE',
						});
						if (response.ok) {
							this.planes = this.planes.filter((plan) => plan.id !== id);
							Swal.fire('¡Eliminado!', 'El plan ha sido eliminado.', 'success');
						} else {
							console.error('Error al eliminar el plan:', response.status);
							Swal.fire('Error', 'No se pudo eliminar el plan.', 'error');
						}
					}
				});
			} catch (error) {
				console.error('Error en la solicitud:', error);
				Swal.fire('Error', 'Ocurrió un problema al eliminar el plan.', 'error');
			}
		},
		volver() {
			this.$router.back();
		},
	},
	mounted() {
		this.obtenerPlanes();
	},
};
</script>

<style scoped>
.planes-container {
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

.delete {
	background-color: #f44336;
}

.delete:hover {
	background-color: #e53935;
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
