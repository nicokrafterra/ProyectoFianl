<template>
	<div class="contpri">
		<button class="back-button" @click="volver">
			<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
		</button>

		<section class="campings-section">
			<div class="section-header">
				<h1 class="section-title">Nuestros Campings</h1>
				<p class="section-description">
					Explora nuestros campings seleccionados para una experiencia inolvidable en la naturaleza.
				</p>
			</div>

			<div class="campings-container">
				<div class="camping-card" v-for="(camping, index) in Lugares" :key="index">
					<div class="camping-info">
						<h2 class="camping-name">{{ camping.nombre }}</h2>
						<p class="camping-description">{{ camping.descripcion }}</p>
						<div v-if="camping.disponible">
              <p class="available-info">
                Quedan {{ camping.cantidad_maxima-camping.cantidad_actual }} disponibles
              </p>
							<button class="reserve-button" @click="hacerReserva(camping)">
							Reservar Ahora
						</button>
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
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import Swal from 'sweetalert2';
import axios from 'axios';

// Acceso al store y router
const store = useStore();
const router = useRouter();


const usuario = computed(() => store.state.usuario);

const volver = () => {
	router.back();
};

const Lugares = ref({})

const obtenerCamping = async () => {
	try {
		const response = await axios.get("http://127.0.0.1:8000/planes/Camping/tipo");
		Lugares.value = response.data;
	} catch (error) {
		console.error("Error al obtener los lugares:", error);
		Swal.fire({
			icon: 'error',
			title: 'Error',
			text: 'No se pudieron cargar los lugares. Intenta nuevamente más tarde.',
		});
	}
};

// Función para manejar la reserva
const hacerReserva = async (camping) => {
	// Verificar si el usuario ha iniciado sesión
	if (!usuario.value) {
		await Swal.fire({
			icon: 'warning',
			title: 'Inicia sesión',
			text: 'Debes iniciar sesión para reservar un camping.',
		});
		return;
	}

	try {
		// Enviar la información del camping al backend para procesar la reserva
		await store.dispatch("guardarTipoPlan", camping);
		
		// Redirigir al formulario de reservas
		router.push("/reservas");

		// Mostrar mensaje de éxito
		await Swal.fire({
			icon: 'success',
			title: 'Reserva registrada',
			text: `Has seleccionado el camping "${camping.nombre}" para tu experiencia.`,
		});
	} catch (error) {
		// Manejo de errores
		console.error("Error al realizar la reserva:", error);
		await Swal.fire({
			icon: 'error',
			title: 'Error',
			text: 'No se pudo procesar la reserva. Intenta nuevamente más tarde.',
		});
	}
};


onMounted(obtenerCamping)
</script>

<style scoped>
.contpri {
  padding: 20px;
  background: linear-gradient(135deg, #74b9ff, #a29bfe);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

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

.campings-section {
  background-color: #ffffff;
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
  color: #2d3436;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.section-description {
  font-size: 1.2em;
  color: #636e72;
  line-height: 1.5;
}

.campings-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
}

.camping-card {
  background: #ffffff;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.camping-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
}

.camping-info {
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
  color: #2c3e50;
}

.camping-name {
  font-size: 1.8em;
  margin-bottom: 10px;
  font-weight: bold;
  color: #1e272e;
}

.camping-description {
  font-size: 1.1em;
  color: #636e72;
  margin-bottom: 20px;
  line-height: 1.6;
}

.available-info {
  font-size: 1em;
  font-weight: bold;
  color: #27ae60;
  margin-bottom: 10px;
}

.unavailable-info {
  font-size: 1em;
  font-weight: bold;
  color: #d63031;
}

.reserve-button {
  background: linear-gradient(135deg, #27ae60, #2ecc71);
  color: #ffffff;
  border: none;
  padding: 12px 20px;
  border-radius: 8px;
  font-size: 1em;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s ease, transform 0.2s ease;
}

.reserve-button:hover {
  background: linear-gradient(135deg, #2ecc71, #27ae60);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .campings-container {
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
