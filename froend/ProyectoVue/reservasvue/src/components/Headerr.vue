<template>
	<header>
		<div class="A-logo">
			<svg width="1103" height="996" viewBox="0 0 1103 996" fill="none" xmlns="http://www.w3.org/2000/svg">
				<path fill-rule="evenodd" clip-rule="evenodd"
					d="M410.988 255.56L0 995.337H189.802L505.141 427.427L410.988 255.56ZM1102.94 995.337L647.119 170.373L551.471 0L457.317 170.373L551.471 340.746L711.79 629.718H498.683L405.461 786.972H799.034L914.634 995.337H1102.94Z"
					fill="#FAFBFC" />
				<path fill-rule="evenodd" clip-rule="evenodd"
					d="M410.988 255.56L0 995.337H189.802L505.141 427.427L410.988 255.56ZM1102.94 995.337L647.119 170.373L551.471 0L457.317 170.373L551.471 340.746L711.79 629.718H498.683L405.461 786.972H799.034L914.634 995.337H1102.94Z"
					fill="#FAFBFC" />
			</svg>
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
	background-color: var(--primary);
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
</style>