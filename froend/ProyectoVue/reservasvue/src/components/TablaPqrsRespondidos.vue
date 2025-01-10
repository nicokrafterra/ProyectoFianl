<template>
	<div class="contpri">
		<button class="back-button" @click="volver">
			<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
		</button>
		<div class="pqrs-respondidos-container">
			<h1>PQRs Respondidos</h1>
			<table v-if="pqrs.length > 0">
				<thead>
					<tr>
						<th>Descripción</th>
						<th>Respuesta</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="pqr in pqrs" :key="pqr.id">
						<td>{{ pqr.descripcion }}</td>
						<td>{{ pqr.respuesta }}</td>
					</tr>
				</tbody>
			</table>
			<p v-else>No hay PQRs respondidos.</p>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import { mapState } from 'vuex';

export default {
	computed: {
		...mapState(['usuario']),
	},
	data() {
		return {
			pqrs: [],
		};
	},
	created() {
		this.obtenerPqrsRespondidos();
	},
	methods: {
		async obtenerPqrsRespondidos() {
			try {
				const usuarioId = this.usuario.id;
				const response = await axios.get(`http://localhost:8000/usuarios/${usuarioId}/pqrs/respondidos`);
				this.pqrs = response.data;
			} catch (error) {
				console.error("Error al obtener PQRs respondidos:", error);
			}
		},
		volver() {
			this.$router.back();
		},
	},
};
</script>

<style scoped>
.contpri {
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

.pqrs-respondidos-container {
	max-width: 800px;
	margin: 30px auto;
	padding: 20px;
	background: #f9f9f9;
	border-radius: 12px;
	box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.pqrs-respondidos-container h1 {
	text-align: center;
	color: #333;
	font-size: 28px;
	font-weight: 600;
	margin-bottom: 20px;
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
	border: 1px solid #ddd;
}

th {
	background-color: #f4f4f4;
	font-weight: bold;
}

td {
	background-color: #fff;
}

tr:nth-child(even) td {
	background-color: #f9f9f9;
}

p {
	text-align: center;
	color: #555;
	font-size: 16px;
	margin-top: 20px;
}

p.v-else {
	font-style: italic;
}
</style>
