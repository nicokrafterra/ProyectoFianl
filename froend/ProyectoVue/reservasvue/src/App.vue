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
	background: linear-gradient(0deg, rgba(193,53,21,1) 0%, rgba(47,79,79,1) 49%, rgba(193,53,21,1) 100%);
	background-repeat: no-repeat;
	background-position: 100%;
}

</style>
