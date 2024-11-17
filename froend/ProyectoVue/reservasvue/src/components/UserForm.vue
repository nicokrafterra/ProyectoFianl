<template>
    <div class="user-form">
      <h2>{{ modo === 'editar' ? 'Editar Usuario' : 'Eliminar Usuario' }}</h2>
      <form v-if="modo === 'editar'" @submit.prevent="actualizarUsuario">
        <label for="nombre">Nombre:</label>
        <input v-model="localUsuario.nombre" type="text" id="nombre" required />
  
        <label for="correoElectronico">Email:</label>
        <input v-model="localUsuario.correoElectronico" type="email" id="correoElectronico" required />
  
        <label for="numeroCelular">Teléfono:</label>
        <input v-model="localUsuario.numeroCelular" type="text" id="numeroCelular" required />
  
        <!-- Otros campos necesarios -->
  
        <button type="submit">Guardar Cambios</button>
        <button type="button" @click="$emit('cerrar')">Cancelar</button>
      </form>
  
      <div v-else>
        <p>¿Estás seguro de que deseas eliminar a este usuario?</p>
        <button @click="eliminarUsuario" class="confbtn">Sí, eliminar</button>
        <button @click="$emit('cerrar')" class="confbtn">Cancelar</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Swal from 'sweetalert2'; 
  
  export default {
	props: {
	  usuario: Object,
	  modo: String 
	},
	data() {
	  return {
		localUsuario: { ...this.usuario }
	  };
	},
	watch: {
	  usuario: {
		handler(newValue) {
		  this.localUsuario = { ...newValue };
		},
		deep: true
	  }
	},
	methods: {
	  async actualizarUsuario() {
		try {
		  await axios.put(`http://127.0.0.1:8000/usuarios/${this.usuario.id}`, this.localUsuario);
		  
		  Swal.fire({
			title: 'Éxito!',
			text: 'Usuario actualizado con éxito.',
			icon: 'success',
			confirmButtonText: 'Aceptar'
		  });
  
		  this.$emit('actualizado');
		} catch (error) {
		  console.error("Error al actualizar el usuario:", error);
		  
		  Swal.fire({
			title: 'Error!',
			text: 'Hubo un error al actualizar el usuario.',
			icon: 'error',
			confirmButtonText: 'Aceptar'
		  });
		}
	  },
	  async eliminarUsuario() {
		try {
		  await axios.delete(`http://127.0.0.1:8000/usuarios/${this.usuario.id}`);
		  
		  Swal.fire({
			title: 'Éxito!',
			text: 'Usuario eliminado con éxito.',
			icon: 'success',
			confirmButtonText: 'Aceptar'
		  });
  
		  this.$emit('eliminado');
		} catch (error) {
		  console.error("Error al eliminar el usuario:", error);
		  
		  Swal.fire({
			title: 'Error!',
			text: 'Hubo un error al eliminar el usuario.',
			icon: 'error',
			confirmButtonText: 'Aceptar'
		  });
		}
	  }
	}
  };
  </script>
  
  <style scoped>
  .user-form {
    max-width: 400px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
    font-family: Arial, sans-serif;
  }
  
  h2 {
    text-align: center;
    color: #333;
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
    color: #555;
  }
  
  input {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
    transition: border-color 0.3s;
  }
  
  input:focus {
    border-color: #007bff;
    outline: none;
  }
  
  button {
    width: 48%;
    padding: 10px;
    margin: 5px 1%;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    color: #ffffff;
    transition: background-color 0.3s;
		background-color: #007bff;
  }
  
  button[type="submit"] {
    background-color: #28a745;
  }
  
  button[type="button"] {
    background-color: #dc3545;
  }
  
  button:hover {
    opacity: 0.9;
  }
  
  p {
    text-align: center;
    margin-bottom: 20px;
    color: #555;
  }
  
  @media (max-width: 500px) {
    .user-form {
      width: 90%;
    }
  }
  </style>
  