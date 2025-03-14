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

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { jwtDecode } from 'jwt-decode';
import axios from 'axios';

const router = useRouter();
const pqrs = ref([]);
const usuarioId = ref(null);

// 🔹 Obtener el ID de usuario desde el token JWT
const obtenerUsuarioDesdeJWT = () => {
	const token = localStorage.getItem('token');
	if (token) {
		try {
			const decodedToken = jwtDecode(token);
			usuarioId.value = decodedToken.sub; // Ajusta esto según cómo envía el backend el ID del usuario en el token
		} catch (error) {
			console.error('Error al decodificar el token:', error);
			usuarioId.value = null;
		}
	}
};

// 🔹 Obtener PQRs respondidos con autenticación JWT
const obtenerPqrsRespondidos = async () => {
	if (!usuarioId.value) {
		console.error("No se pudo obtener el ID del usuario desde el token.");
		return;
	}

	try {
		const token = localStorage.getItem('token');
		const response = await axios.get(`http://localhost:8000/usuarios/${usuarioId.value}/pqrs/respondidos`, {
			headers: {
				Authorization: `Bearer ${token}`, // 🔹 Se incluye el token JWT en la solicitud
			},
		});
		pqrs.value = response.data;
	} catch (error) {
		console.error("Error al obtener PQRs respondidos:", error.response ? error.response.data : error.message);
	}
};

// 🔹 Ejecutar la función al montar el componente
onMounted(() => {
	obtenerUsuarioDesdeJWT();
	obtenerPqrsRespondidos();
});

// 🔹 Función para volver atrás
const volver = () => {
	router.go(-1);
};
</script>


<style scoped>
.contpri {
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center; /* Fondo blanco para el contenedor principal */
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
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.3),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 0.3),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
	background-color: #6B8E23; /* Verde Oliva como fondo al hacer hover */
	border-radius: 6px;
}

.back-button img {
	width: 24px;
	height: 24px;
	transition: transform 0.2s ease;
}

.pqrs-respondidos-container {
	max-width: 800px;
	width: 90%;
	padding: 20px;
	background: #FFFFFF; /* Fondo blanco para el contenedor */
	border-radius: 12px;
	box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
	border: 1px solid #8B5A2B; /* Marrón Tierra para el borde */
}

.pqrs-respondidos-container h1 {
	text-align: center;
	color: #6B8E23; /* Verde Oliva para el título */
	font-size: 28px;
	font-weight: 600;
	margin-bottom: 20px;
}

table {
	width: 100%;
	border-collapse: collapse;
	margin-top: 20px;
	background-color: #F5DEB3; /* Beige Arena como fondo de la tabla */
	border-radius: 8px;
	overflow: hidden;
}

th,
td {
	padding: 12px;
	text-align: left;
	border: 1px solid #8B5A2B; /* Marrón Tierra para los bordes de la tabla */
}

th {
	background-color: #D4A017; /* Amarillo Mostaza para el fondo de los encabezados */
	font-weight: bold;
	color: #FFFFFF; /* Texto blanco para contrastar */
}

td {
	background-color: #FFFFFF; /* Fondo blanco para las celdas */
}

tr:nth-child(even) td {
	background-color: #F5DEB3; /* Beige Arena para filas pares */
}

p {
	text-align: center;
	color: #6B8E23; /* Verde Oliva para el texto */
	font-size: 16px;
	margin-top: 20px;
}

p.v-else {
	font-style: italic;
	color: #C1440E; /* Rojo Terracota para texto adicional */
}
/*------------- responsive  -------------------------------------------*/
@media (max-width: 768px) {
    .contpri {
        padding: 10px;
    }

    .back-button {
        top: 10px;
        left: 10px;
        width: 36px;
        height: 36px;
    }

    .back-button img {
        width: 20px;
        height: 20px;
    }

    .pqrs-respondidos-container {
        max-width: 100%; 
        padding: 28px;
        margin: 120px auto;
        font-size: 14px;
    }

    table {
        font-size: 12px;
        overflow-x: auto;
        display: block;
        width: 100%;
    }

    th, td {
        padding: 8px;
        font-size: 12px;
        word-wrap: break-word;
    }

    h1 {
        font-size: 25px;
    }

    p.v-else {
        font-size: 20px;
    }
}
/* Agregado extra*/
.pqrs-respondidos-container {
    animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
