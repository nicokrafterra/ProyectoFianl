<script setup>
//-------------------------------------------------------------------------------------------------------------
// Se realizan todas las importaciones correspondientes
import { ref, onMounted, onBeforeUnmount, computed } from 'vue'; // Importaciones de Vue
import { useStore } from 'vuex'; // Para manejar el estado global
import { useRouter } from 'vue-router'; // Para manejar la navegación
import { jwtDecode } from 'jwt-decode'; // Para decodificar tokens JWT
import { watch } from 'vue'; // Para observar cambios en las propiedades reactivas
//--------------------------------------------------------------------------------------------------------------

// Definición de variables reactivas
const isHidden = ref(true); // Controla la visibilidad del menú desplegable
const isFading = ref(false); // Controla la animación de desvanecimiento del menú
const Menu = ref(null); // Referencia al menú desplegable

const store = useStore(); // Acceso al store de Vuex
const router = useRouter(); // Acceso al router de Vue
const token = ref(localStorage.getItem("token")); // Obtiene el token del localStorage
const usuario = computed(() => store.state.usuario); // Obtiene el usuario del store
const imagenPorDefecto = ref("../assets/IMG/foto.png"); // Ruta de la imagen de perfil por defecto
//---------------------------------------------------------------------------------------------------------------
// Propiedad computada para obtener la URL de la imagen del store

watch(() => store.state.usuario?.imagen, (nuevaImagen, imagenAnterior) => {
  if (nuevaImagen !== imagenAnterior) {
    console.log("Nueva imagen detectada:", nuevaImagen);
  }
});

const imagenPerfil = computed(() => {
  const imagen = store.state.usuario?.imagen;
  console.log("URL de la imagen en el componente:", imagen); // Depuración
  return imagen
    ? `http://localhost:8000/${imagen}?${Date.now()}` // Timestamp para evitar caché
    : imagenPorDefecto.value;
});

// Observar cambios en el store para la imagen del usuario
watch(() => store.state.usuario?.imagen, (nuevaImagen) => {
  console.log("Nueva imagen en el store222:", nuevaImagen); // Depuración
});

// Función para alternar la visibilidad del menú desplegable
const toggleDropdown = () => {
    isHidden.value = !isHidden.value;
    isFading.value = !isHidden.value;
};

// Función para cerrar el menú desplegable al hacer clic fuera de él
const handleClickOutside = (event) => {
    if (Menu.value && !Menu.value.contains(event.target) && !event.target.classList.contains('perfil')) {
        isHidden.value = true;
        isFading.value = true;
    }
};

// Función para redirigir al inicio de sesión
const redirigirALogin = () => {
    router.push("/Iniciar");
};

// Función para cerrar sesión
const cerrarSesion = () => {
    localStorage.removeItem("token"); // Elimina el token del localStorage
    token.value = null; // Actualiza el estado del token
    store.commit("setUsuario", null); // Limpia el usuario en el store
    window.location.reload(); // Recarga la página
};

// Hook de ciclo de vida: cuando el componente se monta
onMounted(() => {
    document.addEventListener('click', handleClickOutside); // Escucha clics fuera del menú
    if (token.value) {
        try {
            const decoded = jwtDecode(token.value); // Decodifica el token JWT
            store.commit("setUsuario", decoded); // Guarda el usuario decodificado en el store
        } catch (error) {
            console.error("Error al decodificar el token:", error);
            localStorage.removeItem("token"); // Elimina el token corrupto
            token.value = null; // Actualiza el estado del token
            router.push("/Iniciar"); // Redirige al login si hay un error
        }
    }
});

// Hook de ciclo de vida: antes de que el componente se desmonte
onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside); // Elimina el listener de clics
});
</script>


<template>
	<header>
		<div class="A-logo">
			<img src="../assets/IMG/LogoFinal.png" alt="">
		</div>
		<span class="navegar__Usuario">
			<router-link class="icon-p" to="/pqr">
				<img class="icon" src="../assets/IMG/message.svg" alt="Mensaje" />
			</router-link>
			<router-link class="icon-p" to="/TablaPqrRes">
				<img class="icon" src="../assets/IMG/notification.svg" alt="Notificación" />
			</router-link>

			<!-- Botón de Iniciar sesión si no hay token -->
			<router-link v-if="!token" to="/Iniciar" class="login-button">
				Iniciar sesión
			</router-link>

			<!-- Menú desplegable si hay token -->
			<template v-else>
				<div :key="componentKey">
					<img class="perfil" :src="imagenPerfil" :key="imagenPerfil" alt="Imagen de perfil"
						@click="toggleDropdown" />
				</div>
			</template>
		</span>

		<!-- Menú desplegable (solo visible si hay token) -->
		<div v-if="token" class="Menu-desple" :class="{ hide: isHidden, 'Menu-desple-gable': isFading }" ref="Menu">
			<div class="Menu__group">
				<div class="nombre-usuario">{{ usuario?.nombre }}</div>
				<div class="email">{{ usuario?.correoElectronico }}</div>
			</div>
			<hr class="divider" />
			<nav>
				<ul>
					<router-link class="ramdon" to="/Perfil">
						<img src="../assets/IMG/profile.svg" alt="Perfil" /> Mi Perfil
					</router-link>
					<router-link class="ramdon" to="/conf">
						<img src="..//assets/IMG/settings.svg" alt="Ajustes" /> Ajustes
					</router-link>
				</ul>
				<hr class="divider" />
				<ul>
					<router-link class="ramdon" to="/Reservas">
						<img src="../assets/IMG/tutorials.svg" alt="Reservas" /> Mis reservas
					</router-link>
				</ul>
				<hr class="divider" />
				<ul>
					<router-link class="ramdon" to="/Iniciar" @click="cerrarSesion">
						<img src="../assets/IMG/logout.svg" alt="Log Out" /> Salir
					</router-link>
				</ul>
			</nav>
		</div>
	</header>

	<section class="banner">
		<div class="content-banner">
			<p>Lugares Hermosos</p>
			<h2>Comida deliciosa <br />Ingredientes 100% Naturales</h2>
			<!-- Botón de "Reserva ahora" -->
			<router-link v-if="token" to="/Reservas">Reserva ahora</router-link>
			<button v-else class="login-button" @click="redirigirALogin">Inicia sesión para reservar</button>
		</div>
	</section>

	<main class="main-content">
		<section class="container top-categories">
			<h1 class="heading-1">Nuestras Experiencias</h1>
			<div class="container-categories">
				<!-- Tarjeta 1: Camping -->
				<div class="card-category category-moca">
					<img class="Img-PrimerCard" src="../assets/IMG/campfire-896196_1280.jpg" alt="">
					<p>Camping a campo abierto</p>
					<router-link v-if="token" to="Camping"><span>Ver más</span></router-link>
					<button v-else class="login-button" @click="redirigirALogin">Inicia sesión para ver más</button>
				</div>

				<!-- Tarjeta 2: Recorrido guiado -->
				<div class="card-category category-moca">
					<img class="Img-PrimerCard" src="..\assets\IMG\bike-2388449_1280.jpg" alt="">
					<p>Recorrido guiado</p>
					<router-link v-if="token" to="Recorrido"><span>Ver más</span></router-link>
					<button v-else class="login-button" @click="redirigirALogin">Inicia sesión para ver más</button>
				</div>

				<!-- Tarjeta 3: Reserva lugares para eventos -->
				<div class="card-category category-moca">
					<img class="Img-PrimerCard" src="..\assets/IMG/Eventossss.jpg" alt="">
					<p>Reserva lugares para eventos</p>
					<router-link v-if="token" to="/Eventos"><span>Ver más</span></router-link>
					<button v-else class="login-button" @click="redirigirALogin">Inicia sesión para ver más</button>
				</div>

				<!-- Tarjeta 4: Reserva de Mesas -->
				<div class="card-category category-moca">
					<img class="Img-PrimerCard" src="..\assets\IMG\event-6927353_1280.jpg" alt="">
					<p>Reserva de Mesas</p>
					<router-link v-if="token" to="/Mesas"><span>Ver más</span></router-link>
					<button v-else class="login-button" @click="redirigirALogin">Inicia sesión para ver más</button>
				</div>
			</div>
		</section>

		<section class="container top-products">
			<h1 class="heading-1">Mejores Platos</h1>

			<div class="container-products">
				<!-- Producto 1 -->
				<div class="card-product">
					<div class="container-img">
						<img class="IMG-Platos" src="../assets/IMG/Currasco.png" alt="">
						<span class="discount">-13%</span>
						<div class="button-group">
						</div>
					</div>
					<div class="content-card-product">
						<h3>Churrasco</h3>
						<p class="price">$4.60 <span>$5.30</span></p>
						<router-link class="redirect-button" to="/Platos">Ver Plato</router-link>
					</div>
				</div>
				<!-- Producto 2 -->
				<div class="card-product">
					<div class="container-img">
						<img class="IMG-Platos" src="../assets/IMG/Pechuga.jpg" alt="">
						<span class="discount">-22%</span>
						<div class="button-group">
						</div>
					</div>
					<div class="content-card-product">
						<h3>Pechuga gratinada</h3>

						<p class="price">$5.70 <span>$7.30</span></p>
						<router-link class="redirect-button" to="/Platos">Ver Plato</router-link>
					</div>
				</div>
				<!-- Producto 3 -->
				<div class="card-product">
					<div class="container-img">
						<img class="IMG-Platos" src="../assets/IMG/Fetuchino.jpg" alt="">
						<div class="button-group">
						</div>
					</div>
					<div class="content-card-product">
						<h3>Fetuccini</h3>
						<p class="price">$3.20</p>
						<router-link class="redirect-button" to="/Platos">Ver Plato</router-link>
					</div>
				</div>
				<!-- Producto 4 -->
				<div class="card-product">
					<div class="container-img">
						<img class="IMG-Platos" src="../assets/IMG/Picada.jpg" alt="">
						<div class="button-group">
						</div>
					</div>
					<div class="content-card-product">
						<h3>Picadas</h3>
						<p class="price">$5.60</p>
						<router-link class="redirect-button" to="/Platos">Ver Plato</router-link>
					</div>
				</div>
			</div>
		</section>
		<section class="container specials">
			<h1 class="heading-1">Especiales</h1>

			<div class="container-products">
				<!-- Producto 1 -->
				<div class="card-product">
					<div class="container-img">
						<img class="IMG-Platos" src="../assets/IMG/Bagre.jpg" alt="">
						<span class="discount">-13%</span>
						<div class="button-group">
						</div>
					</div>
					<div class="content-card-product">
						<h3>Bagre frito</h3>
						<p class="price">$4.60 <span>$5.30</span></p>
						<router-link class="redirect-button" to="/Platos">Ver Plato</router-link>
					</div>
				</div>
				<!-- Producto 2 -->
				<div class="card-product">
					<div class="container-img">
						<img class="IMG-Platos" src="../assets/IMG/Lengua.jpg" alt="">
						<span class="discount">-22%</span>
						<div class="button-group">
						</div>
					</div>
					<div class="content-card-product">
						<h3>Lengua en salsa criolla</h3>
						<p class="price">$5.70 <span>$7.30</span></p>
						<router-link class="redirect-button" to="/Platos">Ver Plato</router-link>
					</div>
				</div>
				<!--  -->
				<div class="card-product">
					<div class="container-img">
						<img class="IMG-Platos" src="../assets/IMG/PuntaAnca.jpg" alt="">
						<span class="discount">-30%</span>
						<div class="button-group">
						</div>
					</div>
					<div class="content-card-product">
						<h3>Punta de anca</h3>
						<p class="price">$3.85 <span>$5.50</span></p>
						<router-link class="redirect-button" to="/Platos">Ver Plato</router-link>
					</div>
				</div>
				<!--  -->
				<div class="card-product">
					<div class="container-img">
						<img class="IMG-Platos" src="../assets/IMG/MOjarraDiabla.jpg" alt="">
						<div class="button-group">
						</div>
					</div>
					<div class="content-card-product">
						<h3>Mojarra a la diabla</h3>
						<p class="price">$5.60</p>
						<router-link class="redirect-button" to="/Platos">Ver Plato</router-link>
					</div>
				</div>
			</div>
		</section>
	</main>

	<footer class="footer">
		<div class="container container-footer">
			<div class="menu-footer">
				<div class="contact-info">
					<p class="title-footer">Información de Contacto</p>
					<ul>
						<li>
							Kilometro .....
						</li>
						<li>Teléfono: 313-430-9651</li>
						<li>EmaiL: Reservas@support.com</li>
					</ul>
				</div>
			</div>
		</div>
	</footer>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

:root {
	--primary: #C1440E; /* Rojo Terracota */
	--secondary: #6B8E23; /* Verde Oliva */
	--accent: #D4A017; /* Amarillo Mostaza */
	--neutral: #F5DEB3; /* Beige Arena */
	--text: #8B5A2B; /* Marrón Tierra */
	--text-gray: #5A678C;
	--error: #E3452F;
}

.A-logo{
	filter: brightness(0.6) sepia(0.4) hue-rotate(60deg) saturate(1.5);
}

.login-button {
	padding: 8px 16px;
	background-color: var(--secondary);
	color: white;
	border-radius: 4px;
	border: none;
	cursor: pointer;
	text-decoration: none;
	display: inline-block;
	margin-top: 10px;
}

.login-button:hover {
	background-color: #5A7D1A;
}

header {
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	height: 80px;
	padding: 0 16px;
	width: 100%;
	display: flex;
	align-items: center;
	background-color: var(--primary);
	justify-content: end;
	z-index: 1000;
}

.navegar__Usuario {
	display: flex;
	gap: 18px;
	align-items: center;
	margin-right: 20px;
}

.navegar__Usuario>.icon {
	cursor: pointer;
	width: 50px;
	height: 50px;
	transition: all 0.5s ease-in-out;
}

.navegar__Usuario>.icon:hover {
	transform: scale(1.1);
	filter: brightness(0.6) sepia(0.4) hue-rotate(60deg) saturate(1.5);
}

.navegar__Usuario>.icon-p:hover {
	transform: scale(1.3);
	filter: brightness(0.6) sepia(0.4) hue-rotate(60deg) saturate(1.5);
}

.nombre-usuario {
	font-size: 14px;
	font-weight: 700;
	text-align: left;
	color: var(--text);
}

.perfil {
	display: block;
	object-fit: cover;
	width: 50px;
	height: 50px;
	cursor: pointer;
	border: 2px solid #ffffff;
	filter: drop-shadow(-20px 0 10px rgba(0, 0, 0, 0.1));
	border-radius: 50%
}

.perfil:hover {
	transform: scale(1.1);
	transition: all 0.4s ease-in-out;
	border: 3.5px solid var(--accent);
}

.email {
	color: var(--text-gray);
}

.Menu-desple {
	width: 240px;
	top: 88px;
	right: 16px;
	position: absolute;
	border-radius: 8px;
	border: 1px solid var(--text-gray);
	display: flex;
	flex-direction: column;
	gap: 4px;
	animation: fadeOutAnimation ease-in-out 0.3s forwards;
	background-color: var(--neutral);
}

.Menu-desple-gable {
	animation: fadeInAnimation ease-in-out 0.3s forwards;
}

.hide {
	opacity: 0;
	visibility: hidden;
	animation: fadeOutAnimation ease-in-out 0.3s forwards;
}

@keyframes fadeInAnimation {
	0% {
		opacity: 0;
		visibility: hidden;
		width: 160px;
	}

	100% {
		opacity: 1;
		visibility: visible;
		width: 240px;
	}
}

@keyframes fadeOutAnimation {
	0% {
		opacity: 1;
		width: 240px;
		visibility: visible;
	}

	100% {
		opacity: 0;
		width: 160px;
		visibility: hidden;
	}
}

.Menu__group {
	padding: 12px;
}

.divider {
	width: 100%;
	padding: 0;
	margin: 0;
}

nav>ul {
	list-style-type: none;
	padding: 0;
	margin: 0;
	gap: 4px;
}

nav>ul>li {
	height: 40px;
	display: flex;
	flex-direction: row;
	align-items: center;
	gap: 16px;
	padding-left: 8px;
	width: 100%;
}

.ramdon {
	height: 40px;
	display: flex;
	flex-direction: row;
	align-items: center;
	gap: 16px;
	padding-left: 8px;
	width: 100%;
	color: var(--text);
	list-style: none;
	text-decoration: none;
}

.ramdon:hover {
	cursor: pointer;
	text-decoration: underline;
	background-color: var(--neutral);
}

nav>ul>li>img {
	height: 24px;
	width: 24px;
}

nav>ul>li:hover {
	cursor: pointer;
	text-decoration: underline;
}

.A-logo {
	display: flex;
	gap: 1rem;
	flex-grow: 1;
}

.A-logo svg {
	stroke: var(--text);
	stroke-width: 0.5rem;
	width: 3rem;
	height: 3rem;
}

.gallery {
	display: flex;
	flex-wrap: wrap;
	gap: 1rem;
}

.card {
	position: relative;
	left: 0;
	width: 6rem;
	border-radius: 1.2rem;
	height: 20rem;
	overflow: hidden;
	background: var(--neutral);
	transition: 0.4s ease-in-out;
	box-shadow: 0 5px 12px rgba(0, 0, 0, 0.3);
	flex: 0.25;
}

.card img {
	width: 100%;
	height: auto;
	object-fit: cover;
}

.card:hover {
	flex: 2;
	font-weight: bold;
	cursor: pointer;
	border-radius: 1rem;
}

.banner {
	background-image: url('tu-imagen-de-fondo.jpg');
	background-size: cover;
	background-position: center;
	padding: 100px 0;
	color: var(--neutral);
	text-align: center;
}

.content-banner p {
	font-size: 24px;
	margin-bottom: 20px;
}

.content-banner h2 {
	font-size: 48px;
	line-height: 1.2;
	margin-bottom: 20px;
}

.content-banner a {
	display: inline-block;
	padding: 10px 30px;
	background-color: var(--accent);
	color: var(--neutral);
	text-decoration: none;
	border-radius: 5px;
	transition: background-color 0.3s;
}

.content-banner a:hover {
	background-color: #B38915;
}

.main-content {
	padding: 60px 0;
	background-color: var(--neutral);
}

.container {
	max-width: 1200%;
	margin: 0 auto;
	padding: 0 15px;
}

.heading-1 {
	font-size: 36px;
	text-align: center;
	margin-bottom: 40px;
	color: var(--text);
}

.top-categories .container-categories {
	display: flex;
	justify-content: space-between;
}

.Img-PrimerCard {
	height: 200px;
	width: 100%;
}

.card-category {
	background-color: var(--neutral);
	border-radius: 20px;
	text-align: center;
	flex-basis: 80%;
	transition: transform 0.3s, box-shadow 0.3s;
	margin: 10px;
	padding-bottom: 15px;
	box-shadow: 40px 20px 30px rgba(0, 0, 0, 0.199);
}

.card-category:hover {
	transform: translateY(-10px);
	box-shadow: 10px 20px 30px rgba(0, 0, 0, 0.1);
}

.card-category p {
	font-size: 20px;
	margin-bottom: 18px;
	color: var(--text);
}

.card-category span {
	display: inline-block;
	padding: 8px 30px;
	background-color: var(--accent);
	color: var(--neutral);
	border-radius: 8px;
	cursor: pointer;
	transition: background-color 0.3s;
}

.card-category span:hover {
	background-color: #B38915;
}

.top-products,
.specials {
	margin-top: 60px;
}

.container-options {
	display: flex;
	justify-content: center;
	margin-bottom: 30px;
}

.container-options span {
	margin: 0 15px;
	cursor: pointer;
	color: var(--text);
	font-size: 18px;
	position: relative;
}

.container-options .active {
	font-weight: bold;
}

.container-products {
	display: flex;
	flex-wrap: wrap;
	gap: 20px;
	justify-content: space-between;
}

.card-product {
	background-color: var(--neutral);
	border-radius: 10px;
	flex-basis: 22%;
	transition: transform 0.3s, box-shadow 0.3s;
	position: relative;
	box-shadow: 40px 20px 40px rgba(0, 0, 0, 0.199);
}

.card-product:hover {
	transform: translateY(-10px);
	box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.1);
}

.IMG-Platos {
	height: 100%;
	width: 100%;
}

.container-img {
	position: relative;
	display: flex;
}

.discount {
	position: absolute;
	top: 10px;
	left: 10px;
	background-color: var(--accent);
	color: var(--neutral);
	padding: 5px 10px;
	border-radius: 5px;
}

.button-group {
	display: flex;
	justify-content: space-between;
	margin-top: 10px;
}

.button-group span {
	cursor: pointer;
	color: var(--text);
	font-size: 16px;
}

.content-card-product {
	padding: 20px;
	text-align: center;
}

.stars i {
	color: var(--accent);
}

.price {
	font-size: 18px;
	margin-top: 15px;
}

.price span {
	text-decoration: line-through;
	color: var(--text-gray);
}

.add-cart {
	cursor: pointer;
	background-color: var(--accent);
	color: var(--neutral);
	padding: 5px 10px;
	border-radius: 5px;
	position: absolute;
	right: 10px;
	bottom: 10px;
	transition: background-color 0.3s;
}

.add-cart:hover {
	background-color: #B38915;
}

.container-blogs {
	display: flex;
	flex-wrap: wrap;
	gap: 20px;
	justify-content: space-around;
}

.card-blog {
	background-color: var(--neutral);
	border-radius: 10px;
	flex-basis: 30%;
	transition: transform 0.3s, box-shadow 0.3s;
}

.card-blog:hover {
	transform: translateY(-10px);
	box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.container-img {
	height: 200px;
	background-color: #eaeaea;
	border-radius: 10px 10px 0 0;
	position: relative;
}

.button-group-blog {
	position: absolute;
	top: 10px;
	right: 10px;
	display: flex;
	gap: 10px;
}

.button-group-blog span {
	cursor: pointer;
	color: var(--neutral);
	background-color: rgba(0, 0, 0, 0.5);
	padding: 5px;
	border-radius: 50%;
}

.content-blog {
	padding: 20px;
}

.content-blog h3 {
	font-size: 24px;
	margin-bottom: 10px;
}

.content-blog span {
	display: block;
	font-size: 14px;
	color: var(--text-gray);
	margin-bottom: 15px;
}

.btn-read-more {
	margin-top: 20px;
	padding: 10px;
	background-color: var(--accent);
	color: var(--neutral);
	text-align: center;
	border-radius: 5px;
	cursor: pointer;
	transition: background-color 0.3s;
}

.btn-read-more:hover {
	background-color: #B38915;
}

.footer {
	background: linear-gradient(135deg, var(--text), #444);
	color: var(--neutral);
	padding: 80px 0;
	font-family: 'Poppins', sans-serif;
}

.container-footer {
	display: flex;
	flex-wrap: wrap;
	justify-content: space-between;
	gap: 2rem;
}

.menu-footer {
	flex-basis: 22%;
	margin-bottom: 20px;
}

.title-footer {
	font-size: 20px;
	margin-bottom: 24px;
	font-weight: 600;
	color: var(--accent);
}

.menu-footer ul {
	list-style: none;
	padding: 0;
}

.menu-footer li {
	margin-bottom: 12px;
}

.menu-footer a {
	color: #ccc;
	text-decoration: none;
	font-size: 16px;
	transition: color 0.3s;
}

.menu-footer a:hover {
	color: var(--accent);
}

.social-icons {
	display: flex;
	gap: 20px;
	margin-top: 30px;
}

.social-icons span {
	cursor: pointer;
	font-size: 20px;
	color: #ccc;
	transition: transform 0.3s ease, color 0.3s ease;
}

.social-icons span:hover {
	transform: scale(1.2);
	color: var(--accent);
}

.newsletter input {
	width: 100%;
	padding: 12px;
	border-radius: 5px;
	border: none;
	margin-top: 15px;
	background-color: #555;
	color: var(--neutral);
	font-size: 16px;
}

.footer::before {
	content: '';
	display: block;
	height: 4px;
	width: 80px;
	background-color: var(--accent);
	margin: 0 auto 40px;
}

.redirect-button {
	display: inline-block;
	padding: 10px 20px;
	background-color: var(--primary);
	color: var(--neutral);
	text-transform: uppercase;
	text-decoration: none;
	font-weight: 600;
	font-size: 16px;
	border-radius: 5px;
	border: none;
	cursor: pointer;
	transition: background-color 0.3s ease, transform 0.3s ease;
}

.redirect-button:hover {
	background-color: #A53A0C;
	transform: translateY(-5px);
}

.redirect-button:active {
	background-color: #8C320A;
	transform: translateY(0);
}

.redirect-button:disabled {
	background-color: #cccccc;
	cursor: not-allowed;
	color: #666;
}

@media (max-width: 768px) {
	header {
		height: 60px;
		padding: 0 10px;
	}

	.navegar__Usuario {
		gap: 10px;
	}

	.nombre-usuario {
		font-size: 12px;
	}

	.gallery {
		flex-wrap: wrap;
	}

	.card {
		width: 100%;
		height: auto;
	}

	.content-banner h2 {
		font-size: 32px;
	}

	.content-banner p {
		font-size: 18px;
	}

	.main-content {
		padding: 40px 0;
	}

	.top-categories .container-categories {
		display: flex;
		flex-wrap: wrap;
		gap: 20px;
		justify-content: center;
		align-items: center;
	}

	.card-category {
		flex-basis: 100%;
	}

	.container-products,
	.container-blogs {
		flex-direction: column;
		align-items: center;
	}

	.card-product,
	.card-blog {
		flex-basis: 100%;
		max-width: 100%;
	}

	.IMG-Platos {
		width: 300px;
	}
}

@media (max-width: 1024px) {
	header {
		height: 70px;
		padding: 0 12px;
	}

	.gallery {
		gap: 1rem;
	}

	.card {
		flex: 1 1 calc(50% - 1rem);
		height: 16rem;
	}

	.content-banner h2 {
		font-size: 40px;
	}

	.content-banner p {
		font-size: 20px;
	}

	.top-categories .container-categories {
		display: flex;
		flex-wrap: wrap;
		gap: 20px;
		justify-content: center;
		align-items: center;
	}

	.card-category {
		flex-basis: 90%;
		width: 200px;
	}

	.container-products {
		flex-wrap: wrap;
		justify-content: space-evenly;
	}

	.card-product {
		width: 300px;
	}

	.card-blog {
		flex-basis: 48%;
	}

	.IMG-Platos {
		width: 300px;
		height: 200px;
	}
}
</style>