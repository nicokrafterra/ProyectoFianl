<template>
	<div class="plato-list">
		<!-- Botón de volver -->
		<button class="back-button" @click="volver">
			<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
		</button>

		<h2>Lista de Platos</h2>
		<div class="cards-container">
			<!-- Cada card de plato está escrito de manera explícita -->
			<div class="card">
				<img src="../assets/IMG/Bagre.jpg" alt="Bagre" class="card-image" />
				<div class="card-content">
					<h3>Bagre</h3>
					<p>Delicioso bagre frito.</p>
					<p class="price">15 €</p>
				</div>
			</div>

			<div class="card">
				<img src="../assets/IMG/Currasco.png" alt="Tacos" class="card-image" />
				<div class="card-content">
					<h3>Tacos</h3>
					<p>Tacos al pastor con salsa.</p>
					<p class="price">10 €</p>
				</div>
			</div>

			<div class="card">
				<img src="../assets/IMG/Fetuchino.jpg" alt="Pizza" class="card-image" />
				<div class="card-content">
					<h3>Pizza</h3>
					<p>Pizza margarita con albahaca fresca.</p>
					<p class="price">12 €</p>
				</div>
			</div>

			<div class="card">
				<img src="../assets/IMG/Lengua.jpg" alt="Sushi" class="card-image" />
				<div class="card-content">
					<h3>Sushi</h3>
					<p>Variado de sushi fresco.</p>
					<p class="price">20 €</p>
				</div>
			</div>

			<div class="card">
				<img src="../assets/IMG/MOjarraDiabla.jpg" alt="Hamburguesa" class="card-image" />
				<div class="card-content">
					<h3>Hamburguesa</h3>
					<p>Hamburguesa clásica con queso.</p>
					<p class="price">8 €</p>
				</div>
			</div>

			<div class="card">
				<img src="../assets/IMG/Picada.jpg" alt="Ceviche" class="card-image" />
				<div class="card-content">
					<h3>Ceviche</h3>
					<p>Ceviche de pescado fresco.</p>
					<p class="price">14 €</p>
				</div>
			</div>

			<div class="card">
				<img src="../assets/IMG/Pechuga.jpg" alt="Ramen" class="card-image" />
				<div class="card-content">
					<h3>Ramen</h3>
					<p>Ramen con caldo de pollo.</p>
					<p class="price">11 €</p>
				</div>
			</div>

			<div class="card">
				<img src="../assets/IMG/PuntaAnca.jpg" alt="Curry" class="card-image" />
				<div class="card-content">
					<h3>Curry</h3>
					<p>Curry tailandés con arroz.</p>
					<p class="price">13 €</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const volver = () => {
	router.back();
};
</script>

<style scoped>
.plato-list {
	width: 90%; /* Ajuste para ocupar más espacio */
	max-width: 1200px; /* Límite máximo para no estirarse demasiado */
	margin: 0 auto;
	padding: 40px 20px; /* Más padding para mejor espaciado */
	margin-top: 90px;
	text-align: center;
	position: relative;
	background-color: #F5DEB3; /* Beige Arena como fondo */
	border-radius: 15px; /* Bordes redondeados */
	box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Sombra suave */
}

.back-button {
	position: absolute;
	top: 20px;
	left: 20px;
	background-color: transparent;
	border: none;
	cursor: pointer;
	transition: transform 0.2s ease;
}

.back-button img {
	width: 30px;
	height: 30px;
}

.back-button:hover {
	transform: scale(1.1);
}

h2 {
	color: #6B8E23; /* Verde Oliva para el título */
	font-size: 2.5rem;
	margin-bottom: 30px;
}

.cards-container {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); /* Responsive */
	justify-content: center;
	gap: 20px;
	padding: 20px; /* Espaciado interno */
}

.card {
	width: 100%; /* Ocupa el 100% del espacio disponible */
	background-color: #FFFFFF; /* Fondo blanco para las tarjetas */
	border-radius: 15px;
	box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
	overflow: hidden;
	transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
	transform: scale(1.05);
	box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}

.card-image {
	width: 100%;
	height: 150px;
	object-fit: cover;
	border-bottom: 5px solid #D4A017; /* Amarillo Mostaza para el borde inferior */
}

.card-content {
	padding: 15px;
	text-align: center;
}

h3 {
	color: #8B5A2B; /* Marrón Tierra para el título de la tarjeta */
	font-size: 1.2rem;
	margin-bottom: 5px;
}

p {
	color: #555; /* Texto gris oscuro */
	font-size: 0.9rem;
}

.price {
	font-size: 1rem;
	font-weight: bold;
	color: #C1440E; /* Rojo Terracota para el precio */
	margin-top: 5px;
}

@media (max-width: 768px) {
	h2 {
		font-size: 2rem;
	}
	.cards-container {
		grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* Ajuste para tablets */
	}
	.price {
		font-size: 1rem;
	}
}

@media (max-width: 480px) {
	h2 {
		font-size: 1.5rem;
	}
	.card {
		width: 100%;
	}
	.price {
		font-size: 0.9rem;
	}
	.back-button img {
		width: 25px;
		height: 25px;
	}
}
</style>
