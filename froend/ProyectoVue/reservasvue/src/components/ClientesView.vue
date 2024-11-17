<template>
	<button class="back-button" @click="volver">
		<img src="../assets/IMG/arrow-left.svg" alt="Volver" />
	</button>
  <nav class="reservas-container">
    <h2>Usuarios</h2>
    <div class="user-table">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Email</th>
            <th>Teléfono</th>
            <th>Rol</th>
            <th>Status</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.nombre }}</td>
            <td>{{ user.correoElectronico }}</td>
            <td>{{ user.numeroCelular }}</td>
            <td>{{ user.esAdmin ? 'Admin' : 'Usuario' }}</td>
            <td :class="user.status === 'Activo' ? 'status-active' : 'status-inactive'">{{ user.status }}</td>
            <td>
              <button @click="abrirFormulario(user, 'editar')" class="action-button edit">✏️</button>
              <button @click="abrirFormulario(user, 'eliminar')" class="action-button delete">🗑️</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <UserForm
      v-if="mostrarFormulario"
      :usuario="usuarioSeleccionado"
      :modo="modoFormulario"
      @cerrar="cerrarFormulario"
      @actualizado="cargarUsuarios"
      @eliminado="cargarUsuarios"
    />
  </nav>
</template>

<style scoped>

.back-button{
	padding: 10px 15px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s;
}

.back-button:hover{
  background-color: #ff9800;
}
.reservas-container {
  width: 80%;
  margin: auto;
  margin-top: 20px;
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

h2 {
  text-align: center;
  color: #234666;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #234666;
  color: #fff;
}

tr:hover {
  background-color: #f1f1f1;
}

button {
  padding: 10px 15px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #ff9800;
}

.action-button {
  padding: 8px 12px;
  font-size: 14px;
  margin: 5px;
  cursor: pointer;
}

.edit {
  background-color: #4caf50;
}

.edit:hover {
  background-color: #ff9800;
}

.delete {
  background-color: #f44336;
}

.delete:hover {
  background-color: #e53935;
}

.status-active {
  color: #4caf50;
}

.status-inactive {
  color: #f44336;
}
</style>
  
  <script>
  import axios from 'axios';
  import UserForm from './UserForm.vue';
  
  
  export default {
    components: { UserForm },
    data() {
      return {
        users: [],
        mostrarFormulario: false,
        usuarioSeleccionado: null,
        modoFormulario: 'editar' // o 'eliminar'
      };
    },
    methods: {
      async cargarUsuarios() {
        try {
          const response = await axios.get("http://127.0.0.1:8000/usuarios");
          console.log(response.data)
          this.users = response.data;
        } catch (error) {
          console.error("Error al obtener la lista de usuarios:", error);
        }
      },
      abrirFormulario(usuario, modo) {
        this.usuarioSeleccionado = { ...usuario };
        this.modoFormulario = modo;
        this.mostrarFormulario = true;
      },
      cerrarFormulario() {
        this.mostrarFormulario = false;
        this.usuarioSeleccionado = null;
      },
	  volver() {
			this.$router.back();
		},
    },
    mounted() {
      this.cargarUsuarios(); // Cargar los usuarios cuando se monte el componente
    }
  };
  </script>
  
  