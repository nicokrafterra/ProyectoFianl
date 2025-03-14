<template>
	<div class="contp">
		<button class="back-button" @click="volver">
			<i class="fas fa-arrow-left"></i> <!-- Icono de FontAwesome -->
		</button>
		<div class="card-container">
			<div class="profile-card">
				<div class="profile-header">
					<i class="fas fa-user-circle"></i> <!-- Icono de usuario -->
					<h1>{{ usuario.nombre }}</h1>
				</div>
				<div class="profile-info">
					<p><i class="fas fa-user-tag"></i> Rol: {{ usuario.esAdmin ? "Administrador" : "Usuario" }}</p>
					<p><i class="fas fa-envelope"></i> Correo: {{ usuario.correoElectronico }}</p>
					<p><i class="fas fa-phone"></i> Teléfono: {{ usuario.numeroCelular }}</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { mapState } from 'vuex';

export default {
	computed: {
		...mapState(['usuario']),
	},
	methods: {
		volver() {
			this.$router.back();
		},
	},
};
</script>

<style scoped>
/* Importar FontAwesome */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.contp {
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center;
}

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
}

.back-button:hover {
	transform: scale(1.05);
	color: #8B5A2B; /* Marrón Tierra al hacer hover */
}

.card-container {
	display: flex;
	justify-content: center;
	align-items: center;
	width: 100%;
}

.profile-card {
	background-color: #F5DEB3; /* Beige Arena como fondo principal */
	border-radius: 15px;
	box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Sombra suave */
	padding: 30px;
	width: 300px;
	text-align: center;
	animation: fadeInUp 0.8s ease-out; /* Animación de entrada */
}

.profile-header {
	margin-bottom: 20px;
}

.profile-header i {
	font-size: 60px;
	color: #6B8E23; /* Verde Oliva */
}

.profile-header h1 {
	margin: 10px 0;
	font-size: 24px;
	color: #6B8E23; /* Verde Oliva */
}

.profile-info p {
	font-size: 16px;
	color: #8B5A2B; /* Marrón Tierra */
	margin: 10px 0;
	display: flex;
	align-items: center;
	justify-content: center;
}

.profile-info i {
	margin-right: 10px;
	color: #D4A017; /* Amarillo Mostaza */
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