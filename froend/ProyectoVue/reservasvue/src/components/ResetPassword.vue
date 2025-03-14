<template>
  <div class="reset-container">
    <h2>Restablecer contraseña</h2>
    <form @submit.prevent="resetPassword" class="reset-form">
      <label>Nueva contraseña:</label>
      <input type="password" v-model="newPassword" required class="reset-input" />
      <button type="submit" class="reset-button">Restablecer</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { useRoute, useRouter } from "vue-router";
import { ref } from "vue"; // Importa ref para manejar el estado

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const token = route.query.token;
    const newPassword = ref(""); // Usa ref para manejar newPassword

    const resetPassword = async () => {
  try {
    const datos = {
      token: token,
      nueva_contraseña: newPassword.value,
    };

    console.log("Datos enviados:", datos); // Verifica los datos antes de enviar

    const response = await axios.post("http://localhost:8000/reset-password", datos);
    alert("Contraseña restablecida correctamente.");
    router.push("/Iniciar");
  } catch (error) {
    console.error("Error en la solicitud:", error.response?.data); // Muestra el error del backend
    alert("Error al restablecer contraseña.");
  }
};

    return { newPassword, resetPassword }; // Expone newPassword y resetPassword al template
  },
};
</script>

<style scoped>
.reset-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 35px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.reset-container h2 {
  text-align: center;
  color: #333;
  margin-bottom: 25px;
}

.reset-form label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
  color: #555;
}

.reset-input {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

.reset-button {
  width: 100%;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.reset-button:hover {
  background-color: #45a049;
}
</style>