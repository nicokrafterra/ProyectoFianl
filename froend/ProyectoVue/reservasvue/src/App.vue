<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import Headerr from './components/Headerr.vue';

const route = useRoute();
</script>



<template>
	<Headerr v-if="route.meta.showHeader"/>
	<RouterView />
</template>

<style>
body{
	background-image: url("./assets/IMG/BackgraudPagina12345.jpg");
	background-size: cover;
	background-repeat: no-repeat;
	background-position: 100%;
}

</style>
