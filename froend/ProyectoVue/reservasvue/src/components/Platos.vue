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
	width: 700px;
	margin: 0 auto;
	padding: 20px;
	margin-top: 90px;
	text-align: center;
	position: relative;
	background-color: #ffffffa1;
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
	color: #333;
	font-size: 2.5rem;
	margin-bottom: 30px;
}

.cards-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  justify-content: center;
  gap: 20px;
}

.card {
  width: 200px; /* Ancho fijo */
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.2s ease; /* Transición simple */
}

.card:hover {
  transform: scale(1.05); /* Efecto de escalado suave al pasar el mouse */
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}

.card-image {
  width: 100%;
  height: 150px; /* Ajusté la altura para que se vea mejor en tarjetas pequeñas */
  object-fit: cover;
  border-bottom: 5px solid #ff9800;
}

.card-content {
  padding: 15px;
  text-align: center;
}

h3 {
  color: #ff9800;
  font-size: 1.2rem;
  margin-bottom: 5px;
}

p {
  color: #555;
  font-size: 0.9rem;
}

.price {
  font-size: 1rem;
  font-weight: bold;
  color: #4caf50;
  margin-top: 5px;
}

@media (max-width: 768px) {
	h2 {
		font-size: 2rem;
	}
	.card-content {
		padding: 15px;
		grid-template-columns: repeat(2, 1fr);
	}
	.price {
		font-size: 1rem;
	}
}

@media (max-width: 480px) {
	h2 {
		font-size: 1.5rem;
	}
	.card-content {
		padding: 10px;
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
