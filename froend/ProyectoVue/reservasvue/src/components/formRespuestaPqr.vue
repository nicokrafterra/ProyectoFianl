<template>
	<div class="form-respuesta-pqr">
		<h3>Responder PQR #{{ pqr.id }}</h3>
		<textarea v-model="respuesta" placeholder="Escribe tu respuesta aquí"></textarea>
		<button @click="enviarRespuesta">Enviar Respuesta</button>
		<button @click="$emit('close')">Cancelar</button>
	</div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const props = defineProps({
  pqr: Object
});


const emit = defineEmits();

const respuesta = ref('');

const enviarRespuesta = async () => {
  try {
    const response = await fetch(`http://localhost:8000/pqrs/${props.pqr.id}/respuesta`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ respuesta: respuesta.value }) 
    });

    if (!response.ok) throw new Error("Error al responder PQR");

	Swal.fire({
			title: 'Éxito!',
			text: 'Respuesta enviada con éxito.',
			icon: 'success',
			confirmButtonText: 'Aceptar'
		  });
    respuesta.value = '';
    emit('close'); 
  } catch (error) {
    console.error("Error al enviar respuesta:", error);
  }
};
</script>


<style scoped>
.form-respuesta-pqr {
	max-width: 500px;
	margin: auto;
	padding: 20px;
	background: #f9f9f9;
	border-radius: 15px;
	box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.form-respuesta-pqr h3 {
	text-align: center;
	color: #333;
	font-size: 22px;
	font-weight: 600;
	margin-bottom: 15px;
}

.form-respuesta-pqr textarea {
	width: 100%;
	padding: 12px;
	border: 1px solid #ddd;
	border-radius: 8px;
	font-size: 16px;
	background-color: #fff;
	box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
	transition: border 0.3s ease;
	min-height: 120px;
	resize: vertical;
}

.form-respuesta-pqr textarea:focus {
	border-color: #4caf50;
	outline: none;
	box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
}

.form-respuesta-pqr button {
	width: 100%;
	padding: 12px;
	margin-top: 10px;
	background-color: #4caf50;
	color: white;
	border: none;
	border-radius: 8px;
	cursor: pointer;
	font-weight: bold;
	font-size: 16px;
	transition: background-color 0.3s ease;
}

.form-respuesta-pqr button:hover {
	background-color: #45a049;
}

.form-respuesta-pqr button:last-of-type {
	background-color: #d9534f;
}

.form-respuesta-pqr button:last-of-type:hover {
	background-color: #c9302c;
}
</style>