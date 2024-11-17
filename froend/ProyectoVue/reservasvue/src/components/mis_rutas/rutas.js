import { createRouter, createWebHistory } from "vue-router";
import Perfil from "../Perfil.vue";
import Reserva from "../Reserva.vue";
import Platos from "../Platos.vue";
import Pricipal from "../Pricipal.vue";
import Register from "../Register.vue";
import Singin from "../Singin.vue";
import Pqr from "../Pqr.vue";
import Configuracion from "../Configuracion.vue";
import ReservasVer from "../ReservasVer.vue";
import { compile } from "vue";
import VistaAD from "../VistaAD.vue";
import UserForm from "../UserForm.vue";
import ReservasView from "../ReservasView.vue";
import ClientesView from "../ClientesView.vue";
import FormRespuestaPqr from "../formRespuestaPqr.vue";
import TablaPqrs from "../tablaPqrs.vue";
import TablaPqrsRespondidos from "../TablaPqrsRespondidos.vue";
import UpdateContra from "../updateContra.vue";
import UpdateCorreo from "../updateCorreo.vue";

const routes = [
    {
        path: "/index",
        name: "index",
        component: Pricipal
    },
    {
        path: "/Perfil",
        name: "Perfil",
        component: Perfil
    },
    {
        path: "/Reservas",
        name: "Reservas",
        component: Reserva
    },
    {
        path: "/Platos",
        name: "Platos",
        component: Platos
    },
    {
        path: '/',
        redirect: '/Registrar',
        meta: { showHeader: true }, 
    },
    {
        path: '/Registrar',
        name: 'Register',
        component: Register,
        meta: { showHeader: true }, 
    },
    {
        path: '/Iniciar',
        name: 'Iniciar',
        component: Singin,
        meta: { showHeader: true },  
    },
    {
        path: '/pqr',
        name: 'pqr',
        component : Pqr,
    },
    {
        path: '/conf',
        name: 'conf',
        component: Configuracion,
    },
    {
        path: '/ResVer',
        name: 'ResVer',
        component: ReservasVer,
    },
    {
        path: '/VistaAd',
        name: 'VisataAd',
        component:VistaAD,
    },
    {
        path: '/UserForm',
        name: 'UserForm',
        component:UserForm,
    },
    {
        path: '/ReservasView',
        name: 'ReservasView',
        component:ReservasView,
    },
    {
        path: '/ClientesVer',
        name: 'Clientes',
        component:ClientesView
    },
    {
        path: '/formResp',
        name: 'formResp',
        component:FormRespuestaPqr
    },
    {
        path: '/TablaPqrAd',
        name: 'TablapqrAd',
        component:TablaPqrs
    },
    {
        path: '/TablaPqrRes',
        name: 'TablaPqrsRes',
        component:TablaPqrsRespondidos
    },
    {
        path: '/updateContra',
        name: 'updateContra',
        component:UpdateContra
    },
    {
        path: '/updateCorreo',
        name: 'ipdateCorreo',
        component:UpdateCorreo
    }
];
const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;