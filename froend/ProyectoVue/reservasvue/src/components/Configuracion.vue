<template>
	<button class="back-button" @click="volver">
		<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<div class="configuracion">
		<div class="menu">
			<h2>Configuración</h2>
			<router-link class="config-button" to="/updateCorreo">Actualizar Correo</router-link>
			<router-link class="config-button" to="/updateContra">Actualizar Contraseña</router-link>
			<button class="config-button" @click="seleccionarImagen">Cambiar Foto</button>
			<button class="config-button eliminar-button" @click="eliminarCuenta">Eliminar Cuenta</button>
			<input type="file" ref="imagenInput" @change="cambiarFoto" style="display: none;" />
		</div>
	</div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex'; // Importa useStore
import axios from 'axios';
import Swal from 'sweetalert2';
import { jwtDecode } from 'jwt-decode';

const router = useRouter();
const store = useStore(); // Obtén el store
const imagenInput = ref(null);
const userId = ref(null); // Se extraerá desde el token JWT

// Función para obtener el user_id desde el token JWT
function obtenerUserId() {
	const token = localStorage.getItem('token');
	if (token) {
		try {
			const decodedToken = jwtDecode(token);
			userId.value = decodedToken.sub; // "sub" suele ser el ID del usuario
		} catch (error) {
			console.error('Error al decodificar el token:', error);
			userId.value = null;
		}
	}
}

// Seleccionar imagen
const seleccionarImagen = () => {
	imagenInput.value.click();
};

// Subir imagen de perfil
const cambiarFoto = async (event) => {
  const archivo = event.target.files[0];
  if (!archivo) return;

  const formData = new FormData();
  formData.append("file", archivo);

  try {
    const response = await axios.put(
      `http://localhost:8000/usuarios/${userId.value}/actualizar-foto`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      }
    );

    // Llama a la acción para actualizar el token y el usuario en el store
    await store.dispatch("actualizarFoto", response);

    Swal.fire({
      icon: 'success',
      title: 'Imagen actualizada',
      text: 'Tu foto de perfil se ha actualizado correctamente.',
    });
  } catch (error) {
    console.error("Error al subir la imagen:", error);
    Swal.fire({
      icon: 'error',
      title: 'Error',
      text: error.response?.data?.detail || 'No se pudo actualizar la foto de perfil.',
    });
  }
};
      
// Eliminar cuenta
const eliminarCuenta = async () => {
	Swal.fire({
		title: '¿Estás seguro?',
		text: 'Esta acción no se puede deshacer.',
		icon: 'warning',
		showCancelButton: true,
		confirmButtonColor: '#d33',
		cancelButtonColor: '#3085d6',
		confirmButtonText: 'Sí, eliminar',
		cancelButtonText: 'Cancelar',
	}).then(async (result) => {
		if (result.isConfirmed) {
			try {
				await axios.delete(`http://localhost:8000/usuarios/${userId.value}`, {
					headers: {
						Authorization: `Bearer ${localStorage.getItem('token')}`,
					},
				});


				Swal.fire({
					icon: 'success',
					title: 'Cuenta eliminada',
					text: 'Tu cuenta ha sido eliminada con éxito.',
					timer: 2000,
					showConfirmButton: false,
				}).then(() => {
					router.push('/login');
				});

			} catch (error) {
				console.error("Error al eliminar la cuenta:", error);
				Swal.fire({
					icon: 'error',
					title: 'Error',
					text: error.response?.data?.detail || 'No se pudo eliminar la cuenta.',
				});
			}
		}
	});
};

const volver = () => {
	router.go(-1); // Esto regresa a la página anterior en el historial
};

// Obtener el userId cuando el componente se monta
onMounted(() => {
	obtenerUserId();
});
</script>


<style scoped>
/* Importar FontAwesome para iconos */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

/* Botón de regresar */
.back-button {
	position: absolute;
	top: 20px;
	left: 20px;
	background: none;
	border: none;
	cursor: pointer;
	transition: 0.35s;
	font-size: 24px;
	color: #6B8E23; /* Verde Oliva */
	width: 50px;
	height: 40px;
}

.back-button:hover {
	transform: scale(1.05);
	background-color: #8B5A2B; /* Marrón Tierra al hacer hover */
	border-radius: 10px;
}

/* Contenedor central */
.configuracion {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 100vh;

}

/* Menú de configuración */
.menu {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	gap: 20px;
	padding: 40px 30px;
	border-radius: 15px;
	background-color: #F5DEB3; /* Beige Arena como fondo principal */
	box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Sombra suave */
	width: 400px;
	animation: fadeInUp 0.8s ease-out; /* Animación de entrada */
}

.menu h2 {
	margin-bottom: 25px;
	color: #6B8E23; /* Verde Oliva */
	font-weight: bold;
	font-size: 1.5em;
	font-family: 'Courier New', Courier, monospace;
	text-align: center;
}

/* Botones */
.config-button,
.eliminar-button {
	width: 300px; /* Mismo ancho para todos los botones */
	padding: 12px 20px;
	cursor: pointer;
	border-radius: 6px;
	border: 2px solid transparent;
	font-size: 15px;
	font-weight: bold;
	transition: 0.35s;
	text-align: center;
	display: flex;
	align-items: center;
	justify-content: center;
	gap: 10px; /* Espacio entre icono y texto */
}

.config-button {
	background-color: #6B8E23; /* Verde Oliva */
	color: #FFFFFF; /* Texto blanco */
}

.config-button:hover {
	background-color: #8B5A2B; /* Marrón Tierra al hacer hover */
	transform: scale(1.05);
}

.eliminar-button {
	background-color: #C1440E; /* Rojo Terracota */
	color: #FFFFFF; /* Texto blanco */
}

.eliminar-button:hover {
	background-color: #A8380B; /* Rojo más oscuro al hacer hover */
	transform: scale(1.05);
}

/* Iconos dentro de los botones */
.config-button i,
.eliminar-button i {
	font-size: 18px;
}

/* Animaciones */
@keyframes fadeInUp {
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