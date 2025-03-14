<template>
	<div class="contpri">
		<button class="back-button" @click="volver" aria-label="Volver a la página anterior">
			<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
		</button>
		<section class="eventos-section">
			<div class="section-header">
				<h1 class="section-title">Lugares Disponibles para Eventos</h1>
				<p class="section-description">
					Elige el lugar ideal para realizar tu evento y resérvalo ahora.
				</p>
			</div>

			<div class="eventos-container">
				<div v-for="evento in Lugares" :key="evento.id" class="evento-card">
					<div class="evento-info">
						<h2 class="evento-name">Nombre: {{ evento.nombre }}</h2>
						<p class="evento-description">Ubicación: {{ evento.descripcion }}</p>
						<div v-if="evento.disponible">
              <p class="available-info">
                Quedan {{ evento.cantidad_maxima-evento.cantidad_actual }} disponibles
              </p>
							<button class="reserve-button" @click="reservar(evento)">Reservar</button>
            </div>
            <div v-else>
              <p class="unavailable-info">No disponible</p>
            </div>
						
					</div>
				</div>
			</div>
		</section>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Swal from 'sweetalert2';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

const router = useRouter();
const Lugares = ref([]);

// Computed para obtener el usuario decodificando el token JWT
const usuario = computed(() => {
  const token = localStorage.getItem('token');
  if (token) {
    try {
      return jwtDecode(token); // Se espera que el token tenga la información del usuario
    } catch (error) {
      console.error('Error al decodificar el token:', error);
      return null;
    }
  }
  return null;
});

// Función para mostrar alertas con SweetAlert
const mostrarAlerta = (icono, titulo, texto) => {
  Swal.fire({
    icon: icono,
    title: titulo,
    text: texto,
  });
};

const volver = () => {
  router.back();
};

// Obtener los lugares disponibles para eventos
const obtenerLugares = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/planes/Evento/tipo");
    Lugares.value = response.data;
  } catch (error) {
    console.error("Error al obtener los lugares:", error);
    mostrarAlerta('error', 'Error', 'No se pudieron cargar los lugares. Intenta nuevamente más tarde.');
  }
};

// Reservar un lugar para un evento
const reservar = (evento) => {
  if (!usuario.value) {
    mostrarAlerta('warning', 'Inicia sesión', 'Debes iniciar sesión para reservar un lugar.');
    return;
  }

  // Guardar el plan seleccionado en localStorage (simulando la acción de Vuex)
  localStorage.setItem("tipoPlan", JSON.stringify(evento));
  router.push("/reservas");

  mostrarAlerta('success', 'Lugar reservado', `Has seleccionado el lugar "${evento.nombre}" para tu evento.`);
};

onMounted(obtenerLugares);
</script>


<style scoped>
/* Contenedor principal */
.contpri {
  padding: 20px;
  background-color: #FFFFFF; /* Fondo blanco */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Botón de retroceso */
.back-button {
  background: none;
  border: none;
  cursor: pointer;
  margin-bottom: 20px;
  transition: transform 0.2s ease-in-out;
}

.back-button img {
  width: 35px;
  height: 35px;
  filter: drop-shadow(0px 2px 3px rgba(0, 0, 0, 0.2));
}

.back-button:hover {
  transform: scale(1.1);
}

/* Sección de eventos */
.eventos-section {
	background: linear-gradient(135deg, #F5DEB3, #D4A017); /* Beige Arena y Amarillo Mostaza */
  padding: 40px 30px;
  border-radius: 15px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  width: 100%;
  max-width: 1200px;
}

.section-header {
  text-align: center;
  margin-bottom: 50px;
}

.section-title {
  font-size: 2.8em;
  margin-bottom: 15px;
  color: #6B8E23; /* Verde Oliva */
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.section-description {
  font-size: 1.2em;
  color: #8B5A2B; /* Marrón Tierra */
  line-height: 1.5;
}

/* Contenedor de eventos */
.eventos-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
}

/* Tarjetas de eventos */
.evento-card {
  background: #FFFFFF; /* Fondo blanco */
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.evento-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
}

.evento-info {
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
  color: #2c3e50;
}

.evento-name {
  font-size: 1.8em;
  margin-bottom: 10px;
  font-weight: bold;
  color: #6B8E23; /* Verde Oliva */
}

.evento-description {
  font-size: 1.1em;
  color: #8B5A2B; /* Marrón Tierra */
  margin-bottom: 20px;
  line-height: 1.6;
}

.available-info {
  font-size: 1em;
  font-weight: bold;
  color: #4CAF50; /* Verde para disponibilidad */
  margin-bottom: 10px;
}

.unavailable-info {
  font-size: 1em;
  font-weight: bold;
  color: #C1440E; /* Rojo Terracota para no disponibilidad */
}

/* Botón de reserva */
.reserve-button {
  background: linear-gradient(135deg, #6B8E23, #8B5A2B); /* Verde Oliva y Marrón Tierra */
  color: #FFFFFF; /* Texto blanco */
  border: none;
  padding: 12px 20px;
  border-radius: 8px;
  font-size: 1em;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s ease, transform 0.2s ease;
}

.reserve-button:hover {
  background: linear-gradient(135deg, #8B5A2B, #6B8E23); /* Marrón Tierra y Verde Oliva */
  transform: translateY(-2px);
}

/* Responsividad */
@media (max-width: 768px) {
  .eventos-container {
    grid-template-columns: 1fr;
  }

  .section-title {
    font-size: 2.2em;
  }

  .section-description {
    font-size: 1em;
  }

  .reserve-button {
    font-size: 0.9em;
  }
}
</style>