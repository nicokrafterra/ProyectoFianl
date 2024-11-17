<template>
	<div class="contp">
	<button class="back-button" @click="volver">
		<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
	<div id="Container-Perfil">
		<h1>Nombre: {{ usuario.nombre }}</h1>
		<p>Rol: {{ usuario.esAdmin? "Administrador":"Usuario" }}</p>
		<p>Correo:{{ usuario.correoElectronico }}</p>
		<p>Telefono: {{ usuario.numeroCelular }}</p>

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

.contp{
	height: 100vh;
}
#Container-Perfil {
	text-align: center;
	padding: 20px;
	margin-top: 100px;
	background-color: #ffffffb2;
	width: 300px;
	justify-self: center;
}

h1 {
	margin: 0;
	font-size: 24px;
	color: #000000;
}

p {
	font-size: 18px;
	color: #000000;
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

.back-button:hover{
	transform: scale(1.05);
	box-shadow: 6px 6px 10px rgba(0, 0, 0, 1),
		1px 1px 10px rgba(255, 255, 255, 0.6),
		inset 2px 2px 10px rgba(0, 0, 0, 1),
		inset -1px -1px 5px rgba(255, 255, 255, 0.6);
		background-color: #002e02;
		border-radius: 6px;
}

.back-button img {
	width: 24px;
	height: 24px;
	transition: transform 0.2s ease;
}
</style>