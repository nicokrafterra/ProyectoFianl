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
import { useRouter } from 'vue-router';
import Swal from 'sweetalert2';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode'; // Importación por defecto

// Instanciar router
const router = useRouter();

// Computed para obtener el usuario decodificando el token almacenado en localStorage
const usuario = computed(() => {
  const token = localStorage.getItem("token");
  if (token) {
    try {
      return jwtDecode(token); // Se espera que el token contenga el ID en "sub" y otros datos
    } catch (error) {
      console.error("Error al decodificar el token:", error);
      return null;
    }
  }
  return null;
});

// Función para volver atrás
const volver = () => {
  router.back();
};

// Lista de lugares (campings)
const Lugares = ref([]);

// Función para obtener los campings disponibles
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

// Función para reservar un camping
const hacerReserva = (camping) => {
  // Verificar si el usuario está autenticado (obtenido desde el token JWT)
  if (!usuario.value) {
    Swal.fire({
      icon: 'warning',
      title: 'Inicia sesión',
      text: 'Debes iniciar sesión para reservar un camping.',
    });
    return;
  }
  
  // Guardamos la selección del camping en localStorage
  localStorage.setItem("tipoPlan", JSON.stringify(camping));
  
  // Redirigir al formulario de reservas
  router.push("/reservas");

  Swal.fire({
    icon: 'success',
    title: 'Se guardó tu selección, completa el formulario',
    text: `Has reservado el camping "${camping.nombre}" para tu experiencia.`,
  }).then(() => {
    console.log(`Camping reservado: ${camping.nombre}`);
  });
};

onMounted(obtenerCamping);
</script>



<style scoped>
.contpri {
  padding: 20px;
  background-color: #FFFFFF; /* Fondo blanco */
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

.campings-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
}

.camping-card {
  background: #FFFFFF; /* Fondo blanco */
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
  color: #6B8E23; /* Verde Oliva */
}

.camping-description {
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