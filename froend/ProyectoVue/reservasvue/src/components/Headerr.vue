<template>
	<header>
		<div class="A-logo">
				<img class="LogoFianl" src="../assets/IMG/LogoFinal.png" alt="">
		</div>
		<span class="navegar__Usuario">
			<!--<router-link to="#" class="Links">Contactanos</router-link>-->
			<!--<router-link to="#" class="Links">Sobre Nosotros</router-link>-->
		</span>
	</header>>

</template>
<script setup>

</script>

<style>
header {
	position: sticky;
	top: 0;
	left: 0;
	right: 0;
	height: 80px;
	padding: 0 16px;
	width: 100%;
	display: flex;
	align-items: center;
	background-color: #c13515;
	z-index: 1000;
}

.Links {
	list-style: none;
	color: rgb(255, 255, 255);
	font: bold;
	text-decoration: none;
	font-family: 'Courier New', Courier, monospace;
	text-decoration: none;
	padding: 3px;
	border-radius: 5px;
	transition: background-color 0.3s ease, color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
}

.Links:hover {
	color: rgb(0, 0, 0);
	background-color: white;
	padding: 3px;
	border-radius: 5px;
	box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
	transform: translateY(-2px);
}

.navegar__Usuario {
	margin-right: 20px;
}

.LogoFinal{
	height: 50px;
	width: 50px;
}

.A-logo{
	margin-top: 15px;
	height: 150px;
	width: 150px;
}
</style>