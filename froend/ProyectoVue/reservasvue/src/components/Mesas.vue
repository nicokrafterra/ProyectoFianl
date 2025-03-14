<template>
	<div class="contpri">
		<button class="back-button" @click="volver">
			<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
		</button>
		<section class="mesas-section">
			<div class="section-header">
				<h1 class="section-title">Explora Nuestras Mesas</h1>
				<p class="section-description">
					Encuentra la mesa perfecta para tus eventos, reuniones o cenas especiales.
				</p>
			</div>

			<div class="mesas-container">
				<div class="mesa-card" v-for="(mesa, index) in Mesas" :key="index">
					<div class="mesa-info">
						<h2 class="mesa-name">{{ mesa.nombre }}</h2>
						<p class="mesa-description">{{ mesa.descripcion }}</p>
						<div v-if="mesa.disponible">
              <p class="available-info">
                Quedan {{ mesa.cantidad_maxima-mesa.cantidad_actual }} disponibles
              </p>
						<button class="select-button" @click="seleccionarMesa(mesa)">
							Reservar
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
import { jwtDecode } from 'jwt-decode';

const router = useRouter();

// Obtenemos el usuario decodificando el token almacenado en localStorage
const usuario = computed(() => {
  const token = localStorage.getItem('token');
  if (token) {
    try {
      return jwtDecode(token);
    } catch (error) {
      console.error("Error al decodificar el token:", error);
      return null;
    }
  }
  return null;
});

// El ID del usuario se obtiene de la propiedad "sub" del token
const userId = computed(() => usuario.value ? usuario.value.sub : null);

// Variable para almacenar el plan seleccionado (simulando lo que podría estar en Vuex)
const tipoPlan = ref(null);

// Variable para almacenar las mesas disponibles
const Mesas = ref([]);

// Función para obtener el plan seleccionado desde localStorage
const obtenerTipoPlan = () => {
  const planGuardado = localStorage.getItem('tipoPlan');
  if (planGuardado) {
    tipoPlan.value = JSON.parse(planGuardado);
  }
};

// Función para obtener las mesas disponibles
const obtenerMesas = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/planes/Mesa/tipo");
    Mesas.value = response.data;
  } catch (error) {
    console.error("Error al obtener los lugares:", error);
    Swal.fire({
      icon: 'error',
      title: 'Error',
      text: 'No se pudieron cargar los lugares. Intenta nuevamente más tarde.',
    });
  }
};

// Función para manejar la selección de una mesa
const seleccionarMesa = (mesa) => {
  if (!userId.value) {
    Swal.fire({
      icon: 'warning',
      title: 'Inicia sesión',
      text: 'Debes iniciar sesión para reservar un lugar.',
    });
    return;
  }
  
  // Guardar la selección del plan en localStorage
  localStorage.setItem("tipoPlan", JSON.stringify(mesa));
  router.push("/reservas");
  
  Swal.fire({
    icon: 'success',
    title: 'Se guardó tu selección, completa el formulario',
    text: `Has reservado el lugar "${mesa.nombre}" para tu evento.`,
  }).then(() => {
    console.log(`Lugar reservado: ${mesa.nombre}`);
  });
};

// Función para volver a la página anterior
const volver = () => {
  router.back();
};

onMounted(() => {
  obtenerMesas();
  obtenerTipoPlan();
});
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

.mesas-section {

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

.mesas-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
}

.mesa-card {
  background: #FFFFFF; /* Fondo blanco */
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 40px 10px 20px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.mesa-card:hover {
  transform: translateY(-8px);
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.2);
}

.mesa-info {
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
  color: #2c3e50;
}

.mesa-name {
  font-size: 1.8em;
  margin-bottom: 10px;
  font-weight: bold;
  color: #6B8E23; /* Verde Oliva */
}

.mesa-description {
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

.select-button {
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

.select-button:hover {
  background: linear-gradient(135deg, #8B5A2B, #6B8E23); /* Marrón Tierra y Verde Oliva */
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .mesas-container {
    grid-template-columns: 1fr;
  }

  .section-title {
    font-size: 2.2em;
  }

  .section-description {
    font-size: 1em;
  }

  .select-button {
    font-size: 0.9em;
  }
}
</style>